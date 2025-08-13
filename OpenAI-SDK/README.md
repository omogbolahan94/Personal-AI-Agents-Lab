# Debate Crew

Debate Crew project is powered by [crewAI](https://crewai.com). This template is designed to help set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. The goal is to enable agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

Run this command in a VS code/Cursor Terminal in the project root directory using UV in order to run the Crew commands:
```bash
uv tool install crewai
```
And in case Crew as been installed before, it might be worth doing this to make sure the latest exist:
uv tool upgrade crewai
```bash
uv tool upgrade crewai
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Initialize Debate Crew Project
* Create the project folder (`debate`): `crewai create crew dabate`

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/debate/config/agents.yaml` to define your agents
- Modify `src/debate/config/tasks.yaml` to define your tasks
- Modify `src/debate/crew.py` to add your own logic, tools and specific args
- Modify `src/debate/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the debate Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The debate Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

