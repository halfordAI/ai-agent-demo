<div align="center">

# **AI Agents Demo**

This crew is setup to create HTML landing pages!

Example outputs can be found in the `examples` folder.

## **For more information on crewAI:**

🤖 **crewAI**: Cutting-edge framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling complex tasks.

<h3>

[Homepage](https://www.crewai.io/) | [Documentation](https://docs.crewai.com/) | [Chat with Docs](https://chatg.pt/DWjSBZn) | [Examples](https://github.com/joaomdmoura/crewai-examples) | [Discord](https://discord.com/invite/X4JWnZnxPb)

</h3>

</div>

## Getting Started

To get started with this demo, setup a new python environment (using conda or similar) and target Python 3.11, then follow these simple steps:

### 1. Installation

```shell
pip install -r requirements.txt
```

### 2. Add your OpenAI API key

Rename `example.env` to `.env` and add your API key to the `OPENAI_API_KEY` variable.

### 3. Run your crew!

```shell
python main.py
```

## Demo project structure
There are 3 main files that make up this demo:
1. main.py
2. agents.py
3. tasks.py

In `main.py`, we setup the environment, instantiate the agents and tasks, then kick of the crew.

In `agents.py`, we define the 4 agents that make up our "crew". We also create and setup the "tools" that these agents will use.

In `tasks.py`, we define the tasks for our agents. This essentially becomes our "process" through which our crew delivers their "product".

Additionaly, this demo is currently setup to use the sequential process, you can also configure it to use the hierarchical process, which automatically assigns a manager to the defined crew to coordinate the planning and execution of tasks through delegation and validation of results. [See more about the processes here](https://docs.crewai.com/core-concepts/Processes/).

## Other CrewAI Examples

You can test different real life examples of AI crews in the [crewAI-examples repo](https://github.com/joaomdmoura/crewAI-examples?tab=readme-ov-file):

- [Trip Planner](https://github.com/joaomdmoura/crewAI-examples/tree/main/trip_planner)
- [Stock Analysis](https://github.com/joaomdmoura/crewAI-examples/tree/main/stock_analysis)

### Quick Tutorial

[![CrewAI Tutorial](https://img.youtube.com/vi/tnejrr-0a94/maxresdefault.jpg)](https://www.youtube.com/watch?v=tnejrr-0a94 "CrewAI Tutorial")

### Write Job Descriptions

[Check out code for this example](https://github.com/joaomdmoura/crewAI-examples/tree/main/job-posting) or watch a video below:

[![Jobs postings](https://img.youtube.com/vi/u98wEMz-9to/maxresdefault.jpg)](https://www.youtube.com/watch?v=u98wEMz-9to "Jobs postings")

### Trip Planner

[Check out code for this example](https://github.com/joaomdmoura/crewAI-examples/tree/main/trip_planner) or watch a video below:

[![Trip Planner](https://img.youtube.com/vi/xis7rWp-hjs/maxresdefault.jpg)](https://www.youtube.com/watch?v=xis7rWp-hjs "Trip Planner")

### Stock Analysis

[Check out code for this example](https://github.com/joaomdmoura/crewAI-examples/tree/main/stock_analysis) or watch a video below:

[![Stock Analysis](https://img.youtube.com/vi/e0Uj4yWdaAg/maxresdefault.jpg)](https://www.youtube.com/watch?v=e0Uj4yWdaAg "Stock Analysis")

## Connecting Your Crew to a Model

crewAI supports using various LLMs through a variety of connection options. By default your agents will use the OpenAI API when querying the model. However, there are several other ways to allow your agents to connect to models. For example, you can configure your agents to use a local model via the Ollama tool.

Please refer to the [Connect crewAI to LLMs](https://docs.crewai.com/how-to/LLM-Connections/) page for details on configuring you agents' connections to models.

## How CrewAI Compares

- **Autogen**: While Autogen does good in creating conversational agents capable of working together, it lacks an inherent concept of process. In Autogen, orchestrating agents' interactions requires additional programming, which can become complex and cumbersome as the scale of tasks grows.

- **ChatDev**: ChatDev introduced the idea of processes into the realm of AI agents, but its implementation is quite rigid. Customizations in ChatDev are limited and not geared towards production environments, which can hinder scalability and flexibility in real-world applications.

**CrewAI's Advantage**: CrewAI is built with production in mind. It offers the flexibility of Autogen's conversational agents and the structured process approach of ChatDev, but without the rigidity. CrewAI's processes are designed to be dynamic and adaptable, fitting seamlessly into both development and production workflows.

## Telemetry

CrewAI uses anonymous telemetry to collect usage data with the main purpose of helping us improve the library by focusing our efforts on the most used features, integrations and tools.

There is NO data being collected on the prompts, tasks descriptions agents backstories or goals nor tools usage, no API calls, nor responses nor any data that is being processed by the agents, nor any secrets and env vars.

Data collected includes:
- Version of crewAI
  - So we can understand how many users are using the latest version
- Version of Python
  - So we can decide on what versions to better support
- General OS (e.g. number of CPUs, macOS/Windows/Linux)
  - So we know what OS we should focus on and if we could build specific OS related features
- Number of agents and tasks in a crew
  - So we make sure we are testing internally with similar use cases and educate people on the best practices
- Crew Process being used
  - Understand where we should focus our efforts
- If Agents are using memory or allowing delegation
  - Understand if we improved the features or maybe even drop them
- If Tasks are being executed in parallel or sequentially
  - Understand if we should focus more on parallel execution
- Language model being used
  - Improved support on most used languages
- Roles of agents in a crew
  - Understand high level use cases so we can build better tools, integrations and examples about it
- Tools names available
  - Understand out of the publically available tools, which ones are being used the most so we can improve them

Users can opt-in sharing the complete telemetry data by setting the `share_crew` attribute to `True` on their Crews.

## License

CrewAI is released under the MIT License.