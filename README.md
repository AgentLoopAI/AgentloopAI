<a name="readme-top"></a>

![Pypi Downloads](https://img.shields.io/pypi/dm/pyautogen?label=PyPI%20downloads)
[![PyPI version](https://badge.fury.io/py/autogen.svg)](https://badge.fury.io/py/autogen)
[![Build](https://github.com/agentloopai/agentloop/actions/workflows/python-package.yml/badge.svg)](https://github.com/agentloopai/agentloop/actions/workflows/python-package.yml)
![Python Version](https://img.shields.io/badge/3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)
[![Discord](https://img.shields.io/discord/1153072414184452236?logo=discord&style=flat)](https://discord.gg/pAbnFJrkgZ)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/cloudposse.svg?style=social&label=Follow%20%40agentloopai)](https://x.com/agentloopai)

<!-- [![NuGet version](https://badge.fury.io/nu/AutoGen.Core.svg)](https://badge.fury.io/nu/AutoGen.Core) -->

# [AgentLoop](https://github.com/agentloopai/agentloop)

[📚 Cite paper](#related-papers).
<!-- <p align="center">
    <img src="https://github.com/agentloopai/agentloop/blob/main/website/static/img/flaml.svg"  width=200>
    <br>
</p> -->

> **:tada: IMPORTANT**
>
> :fire: :tada: **Nov 11, 2024:** We are evolving AutoGen into **AgentLoop**!
> A new organization [AgentLoopAI](https://github.com/agentloopai) is created to host the development of AgentLoop and related projects with open governance. Check [AgentLoop's new look](https://agentloop.ai/).
>
> We invite collaborators from all organizations and individuals to join the development.


:fire: :tada: AgentLoop is available via `pyautogen` (or its alias  `autogen` or  `agentloop`)  on PyPI!

```
pip install pyautogen
```

📄 **License:**
We adopt the Apache 2.0 license from v0.3. This enhances our commitment to open-source collaboration while providing additional protections for contributors and users alike.


:tada: May 29, 2024: DeepLearning.ai launched a new short course [AI Agentic Design Patterns with AutoGen](https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen), made in collaboration with Microsoft and Penn State University, and taught by AutoGen creators [Chi Wang](https://github.com/sonichi) and [Qingyun Wu](https://github.com/qingyun-wu).

:tada: May 24, 2024: Foundation Capital published an article on [Forbes: The Promise of Multi-Agent AI](https://www.forbes.com/sites/joannechen/2024/05/24/the-promise-of-multi-agent-ai/?sh=2c1e4f454d97) and a video [AI in the Real World Episode 2: Exploring Multi-Agent AI and AutoGen with Chi Wang](https://www.youtube.com/watch?v=RLwyXRVvlNk).

:tada: May 13, 2024: [The Economist](https://www.economist.com/science-and-technology/2024/05/13/todays-ai-models-are-impressive-teams-of-them-will-be-formidable) published an article about multi-agent systems (MAS) following a January 2024 interview with [Chi Wang](https://github.com/sonichi).

:tada: May 11, 2024: [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://openreview.net/pdf?id=uAjxFFing2) received the best paper award at the [ICLR 2024 LLM Agents Workshop](https://llmagents.github.io/).

<!-- :tada: Apr 26, 2024: [AutoGen.NET](https://docs.agentloop.ai/agentloop-for-net/) is available for .NET developers! -->

:tada: Apr 17, 2024: Andrew Ng cited AutoGen in [The Batch newsletter](https://www.deeplearning.ai/the-batch/issue-245/) and [What's next for AI agentic workflows](https://youtu.be/sal78ACtGTc?si=JduUzN_1kDnMq0vF) at Sequoia Capital's AI Ascent (Mar 26).

:tada: Mar 3, 2024: What's new in AutoGen? 📰[Blog](https://docs.agentloop.ai/blog/2024-03-03-AutoGen-Update); 📺[Youtube](https://www.youtube.com/watch?v=j_mtwQiaLGU).

<!-- :tada: Mar 1, 2024: the first AutoGen multi-agent experiment on the challenging [GAIA](https://huggingface.co/spaces/gaia-benchmark/leaderboard) benchmark achieved the No. 1 accuracy in all the three levels. -->

<!-- :tada: Jan 30, 2024: AutoGen is highlighted by Peter Lee in Microsoft Research Forum [Keynote](https://t.co/nUBSjPDjqD). -->

:tada: Dec 31, 2023: [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework](https://arxiv.org/abs/2308.08155) is selected by [TheSequence: My Five Favorite AI Papers of 2023](https://thesequence.substack.com/p/my-five-favorite-ai-papers-of-2023).

<!-- :fire: Nov 24: pyautogen [v0.2](https://github.com/agentloopai/agentloop/releases/tag/v0.2.0) is released with many updates and new features compared to v0.1.1. It switches to using openai-python v1. Please read the [migration guide](https://docs.agentloop.ai/docs/installation/Installation). -->

<!-- :fire: Nov 11: OpenAI's Assistants are available in AutoGen and interoperatable with other AutoGen agents! Checkout our [blogpost](https://docs.agentloop.ai/blog/2023-11-13-OAI-assistants) for details and examples. -->

:tada: Nov 8, 2023: AutoGen is selected into [Open100: Top 100 Open Source achievements](https://www.benchcouncil.org/evaluation/opencs/annual.html) 35 days after spinoff from [FLAML](https://github.com/microsoft/FLAML).

<!-- :tada: Nov 6, 2023: AutoGen is mentioned by Satya Nadella in a [fireside chat](https://youtu.be/0pLBvgYtv6U). -->

<!-- :tada: Nov 1, 2023: AutoGen is the top trending repo on GitHub in October 2023. -->

<!-- :tada: Oct 03, 2023: AutoGen spins off from [FLAML](https://github.com/microsoft/FLAML) on GitHub. -->

<!-- :tada: Aug 16: Paper about AutoGen on [arxiv](https://arxiv.org/abs/2308.08155). -->

:tada: Mar 29, 2023: AutoGen is first created in [FLAML](https://github.com/microsoft/FLAML).

<!--
:fire: FLAML is highlighted in OpenAI's [cookbook](https://github.com/openai/openai-cookbook#related-resources-from-around-the-web).

:fire: [autogen](https://docs.agentloop.ai/) is released with support for ChatGPT and GPT-4, based on [Cost-Effective Hyperparameter Optimization for Large Language Model Generation Inference](https://arxiv.org/abs/2303.04673).

:fire: FLAML supports Code-First AutoML & Tuning – Private Preview in [Microsoft Fabric Data Science](https://learn.microsoft.com/en-us/fabric/data-science/). -->

## What is AgentLoop

AgentLoop (formerly AutoGen) is an open-source programming framework for building AI agents and facilitating cooperation among multiple agents to solve tasks. AgentLoop aims to streamline the development and research of agentic AI, much like PyTorch does for Deep Learning. It offers features such as agents capable of interacting with each other, facilitates the use of various large language models (LLMs) and tool use support, autonomous and human-in-the-loop workflows, and multi-agent conversation patterns.

**Open Source Statement**: The project welcomes contributions from developers and organizations worldwide. Our goal is to foster a collaborative and inclusive community where diverse perspectives and expertise can drive innovation and enhance the project's capabilities. Whether you are an individual contributor or represent an organization, we invite you to join us in shaping the future of this project. Together, we can build something truly remarkable.

The project is currently maintained by a [dynamic group of volunteers](MAINTAINERS.md) from several organizations. Contact project administrators Chi Wang and Qingyun Wu via [support@agentloop.ai](mailto:support@agentloop.ai) if you are interested in becoming a maintainer.


![AutoGen Overview](https://media.githubusercontent.com/media/agentloopai/agentloop/refs/heads/main/website/static/img/autogen_agentchat.png)


<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
  <a href="#readme-top" style="text-decoration: none; color: blue; font-weight: bold;">
    ↑ Back to Top ↑
  </a>
</p>

<!--
## Roadmaps
-->

## Quickstart
The easiest way to start playing is
1. Click below to use the GitHub Codespace

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/agentloopai/agentloop?quickstart=1)

 2. Copy OAI_CONFIG_LIST_sample to ./notebook folder, name to OAI_CONFIG_LIST, and set the correct configuration.
 3. Start playing with the notebooks!

*NOTE*: OAI_CONFIG_LIST_sample lists gpt-4o as the default model. If you use a different model, you may need to revise various system prompts (especially if using weaker models like gpt-4o-mini). Proceed with caution when updating this default and be aware of additional risks related to alignment and safety.

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
  <a href="#readme-top" style="text-decoration: none; color: blue; font-weight: bold;">
    ↑ Back to Top ↑
  </a>
</p>

## [Installation](https://docs.agentloop.ai/docs/installation/Installation)

### Option 1. Install and Run AgentLoop in Docker

Find detailed instructions for users [here](https://docs.agentloop.ai/docs/installation/Docker#step-1-install-docker), and for developers [here](https://docs.agentloop.ai/docs/contributor-guide/docker).

### Option 2. Install AgentLoop Locally

AgentLoop requires **Python version >= 3.9, < 3.14**. It can be installed from pip:

```bash
pip install agentloop
```

Minimal dependencies are installed without extra options. You can install extra options based on the feature you need.

<!-- For example, use the following to install the dependencies needed by the [`blendsearch`](https://microsoft.github.io/FLAML/docs/Use-Cases/Tune-User-Defined-Function#blendsearch-economical-hyperparameter-optimization-with-blended-search-strategy) option.
```bash
pip install "autogen[blendsearch]"
``` -->

Find more options in [Installation](https://docs.agentloop.ai/docs/Installation#option-2-install-autogen-locally-using-virtual-environment).

<!-- Each of the [`notebook examples`](https://github.com/agentloopai/agentloop/tree/main/notebook) may require a specific option to be installed. -->

Even if you are installing and running AgentLoop locally outside of docker, the recommendation and default behavior of agents is to perform [code execution](https://docs.agentloop.ai/docs/FAQ#if-you-want-to-run-code-execution-in-docker) in docker. Find more instructions and how to change the default behaviour [here](https://docs.agentloop.ai/docs/FAQ#if-you-want-to-run-code-execution-locally).

For LLM inference configurations, check the [FAQs](https://docs.agentloop.ai/docs/FAQ#set-your-api-endpoints).

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
  <a href="#readme-top" style="text-decoration: none; color: blue; font-weight: bold;">
    ↑ Back to Top ↑
  </a>
</p>

## Multi-Agent Conversation Framework

AgentLoop enables the next-gen LLM applications with a generic [multi-agent conversation](https://docs.agentloop.ai/docs/Use-Cases/agent_chat) framework. It offers customizable and conversable agents that integrate LLMs, tools, and humans.
By automating chat among multiple capable agents, one can easily make them collectively perform tasks autonomously or with human feedback, including tasks that require using tools via code.

Features of this use case include:

- **Multi-agent conversations**: AgentLoop agents can communicate with each other to solve tasks. This allows for more complex and sophisticated applications than would be possible with a single LLM.
- **Customization**: AgentLoop agents can be customized to meet the specific needs of an application. This includes the ability to choose the LLMs to use, the types of human input to allow, and the tools to employ.
- **Human participation**: AgentLoop seamlessly allows human participation. This means that humans can provide input and feedback to the agents as needed.

For [example](https://github.com/agentloopai/agentloop/blob/main/test/twoagent.py),

```python
from autogen import AssistantAgent, UserProxyAgent, config_list_from_json
# Load LLM inference endpoints from an env variable or a file
# See https://docs.agentloop.ai/docs/FAQ#set-your-api-endpoints
# and OAI_CONFIG_LIST_sample
config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")
# You can also set config_list directly as a list, for example, config_list = [{'model': 'gpt-4o', 'api_key': '<your OpenAI API key here>'},]
assistant = AssistantAgent("assistant", llm_config={"config_list": config_list})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding", "use_docker": False}) # IMPORTANT: set to True to run code in docker, recommended
user_proxy.initiate_chat(assistant, message="Plot a chart of NVDA and TESLA stock price change YTD.")
# This initiates an automated chat between the two agents to solve the task
```

This example can be run with

```python
python test/twoagent.py
```

After the repo is cloned.
The figure below shows an example conversation flow with AgentLoop.

![Agent Chat Example](https://media.githubusercontent.com/media/agentloopai/agentloop/refs/heads/main/website/static/img/chat_example.png)


Alternatively, the [sample code](https://github.com/agentloopai/build-with-agentloop/blob/main/samples/simple_chat.py) here allows a user to chat with an AgentLoop agent in ChatGPT style.
Please find more [code examples](https://docs.agentloop.ai/docs/Examples#automated-multi-agent-chat) for this feature.

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
  <a href="#readme-top" style="text-decoration: none; color: blue; font-weight: bold;">
    ↑ Back to Top ↑
  </a>
</p>

## Enhanced LLM Inferences

AgentLoop also helps maximize the utility out of the expensive LLMs such as gpt-4o. It offers [enhanced LLM inference](https://docs.agentloop.ai/docs/Use-Cases/enhanced_inference#api-unification) with powerful functionalities like caching, error handling, multi-config inference and templating.

<!-- For example, you can optimize generations by LLM with your own tuning data, success metrics, and budgets.

```python
# perform tuning for openai<1
config, analysis = autogen.Completion.tune(
    data=tune_data,
    metric="success",
    mode="max",
    eval_func=eval_func,
    inference_budget=0.05,
    optimization_budget=3,
    num_samples=-1,
)
# perform inference for a test instance
response = autogen.Completion.create(context=test_instance, **config)
```

Please find more [code examples](https://docs.agentloop.ai/docs/Examples#tune-gpt-models) for this feature. -->

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
  <a href="#readme-top" style="text-decoration: none; color: blue; font-weight: bold;">
    ↑ Back to Top ↑
  </a>
</p>

## Documentation

You can find detailed documentation about AgentLoop [here](https://docs.agentloop.ai/).

In addition, you can find:

- [Research](https://docs.agentloop.ai/docs/Research), [blogposts](https://docs.agentloop.ai/blog) around AgentLoop, and [Transparency FAQs](https://github.com/
