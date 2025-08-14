# 🧪 AI Lab

A collection of mini AI projects exploring different AI frameworks and workflows.  
This repo contains experiments using **OpenAI SDK** and **CrewAI**, managed with the blazing-fast [`uv`](https://github.com/astral-sh/uv) package manager.

---

## 📂 Repository Structure

### **1. `OpenAI-SDK/`**
AI experiments built with the official **OpenAI Python SDK**.

- **Research Assistant**
  - An LLM-powered agent that answers questions and provides concise research summaries.
  - Uses the OpenAI API for text generation.
  - Demonstrates prompt design, context passing, and structured responses.

### **2. `CrewAI Framework/`**
Multi-agent workflows built using **[CrewAI](https://docs.crewai.com/)**. The following `crew` projects were created inside the `Crew AI Framework` directotry:

#### **a. `debators/`**
- **Oppose Agent** – argues *against* a given motion.
- **Support Agent** – argues *for* a given motion.
- **Judge Agent** – evaluates both arguments and decides the winner based solely on the debate content.

#### **b. `financial_researcher/`**
- A CrewAI project focused on health, history and current news of a given company.
- Gathers, processes, and summarises research findings.
- Uses multi-agent orchestration for research, analysis, and report generation.

#### **c. `stock_picker/`**
- Financial News Analyst agent that finds and lists trending companies in in a provided sector.
- Financial researcher that provides list of comprehensive analysis of each trending companies in a report.
- Picker that picks the best company with potential for investment.
- Manager who can delegate tasks in order to achieve the goal of picking the best company using CrewAI hierarchical processing.

#### **d. `coder/`**
This project is about a python coding assistant that:
- Plans the logic of the coding challenge
- Writes a clean and efficient code
- Test the code on docker in local machine

#### **e. `software_engineering_team/`**
The project has the following agents:
- Engineering Lead: for the engineering team, directing the work of the engineer
- Backend engineer: Python Engineer who can write code to achieve the design described by the engineering lead
- Frontend engineer: A Gradio expert to who can write a simple frontend to demonstrate a backend
- Test engineer: An engineer with python coding skills who can write unit tests for the given backend module 

---

## ⚡ Package Management
This repo uses **[`uv`](https://github.com/astral-sh/uv)** for Python environment and dependency management.

* Insall UV: follow instruction on this https://docs.astral.sh/uv/getting-started/installation/
* Confirm the version: `uv --version`
* Create virtual environment: `uv venv .venv`
* Activate virtual environment (linux): `source .venv/Scripts/activate`
* On jupyter notebook, the virtual environment is name: Python (myenv). Choose it to use the UV virtual environment on your notebook.

--- 

💡 Notes
Ensure you set up the necessary API keys (.env file) for OpenAI or other LLM providers. Keep .env in your .gitignore for security. Some CrewAI projects may require multiple LLM agents; check the project-specific README for details.