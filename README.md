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
Multi-agent workflows built using **[CrewAI](https://docs.crewai.com/)**.

#### **a. `debators/`**
- **Oppose Agent** – argues *against* a given motion.
- **Support Agent** – argues *for* a given motion.
- **Judge Agent** – evaluates both arguments and decides the winner based solely on the debate content.

#### **b. `financial_researcher/`**
- A CrewAI project focused on market and financial data research.
- Gathers, processes, and summarises financial trends and insights.
- Uses multi-agent orchestration for research, analysis, and report generation.

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