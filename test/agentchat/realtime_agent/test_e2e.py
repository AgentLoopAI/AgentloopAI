# Copyright (c) 2023 - 2024, Owners of https://github.com/ag2ai
#
# SPDX-License-Identifier: Apache-2.0

from typing import Annotated, Any, Generator

import pytest
from anyio import sleep
from asyncer import create_task_group
from conftest import MOCK_OPEN_AI_API_KEY, reason, skip_openai  # noqa: E402
from fastapi import FastAPI, WebSocket
from fastapi.testclient import TestClient
from test_assistant_agent import KEY_LOC, OAI_CONFIG_LIST

import autogen
from autogen.agentchat.realtime_agent import RealtimeAgent, WebSocketAudioAdapter
from autogen.agentchat.realtime_agent.oai_realtime_client import OpenAIRealtimeClient


@pytest.mark.skipif(skip_openai, reason=reason)
class TestE2E:
    @pytest.fixture
    def llm_config(self) -> dict[str, Any]:
        config_list = autogen.config_list_from_json(
            OAI_CONFIG_LIST,
            filter_dict={
                "tags": ["gpt-4o-realtime"],
            },
            file_location=KEY_LOC,
        )
        assert config_list, "No config list found"
        return {
            "config_list": config_list,
            "temperature": 0.8,
        }

    @pytest.mark.asyncio()
    async def test_init(self, llm_config: dict[str, Any]) -> None:

        app = FastAPI()

        @app.websocket("/media-stream")
        async def handle_media_stream(websocket: WebSocket) -> None:
            """Handle WebSocket connections providing audio stream and OpenAI."""
            print("test_init() Waiting for connection to be accepted...", flush=True)
            await websocket.accept()
            print("test_init() Connection accepted.", flush=True)

            audio_adapter = WebSocketAudioAdapter(websocket)
            agent = RealtimeAgent(
                name="Weather Bot",
                system_message="Hello there! I am an AI voice assistant powered by Autogen and the OpenAI Realtime API. You can ask me about weather, jokes, or anything you can imagine. Start by saying 'How can I help you?'",
                llm_config=llm_config,
                audio_adapter=audio_adapter,
            )

            @agent.register_realtime_function(name="get_weather", description="Get the current weather")
            def get_weather(location: Annotated[str, "city"]) -> str:
                return "The weather is cloudy." if location == "Seattle" else "The weather is sunny."

            print("test_init() Running agent...", flush=True)
            async with create_task_group() as tg:
                tg.soonify(agent.run)()
                await sleep(3)
                tg.cancel_scope.cancel()

            # todo: the rest of the scenario
            ...

            await websocket.send_json({"msg": "Hello, World!"})

            print("test_init() Running agent finished", flush=True)
            await websocket.close()

        client = TestClient(app)
        with client.websocket_connect("/media-stream") as websocket:
            data = websocket.receive_json()
            assert data == {"msg": "Hello, World!"}
            print("test_init() client.websocket_connect() finished", flush=True)

        print("test_init() finished")
