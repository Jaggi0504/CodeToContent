# Automated README & LinkedIn Post Generator (LLM‑Powered)

## Overview
This project demonstrates how to automatically generate a professional GitHub README and a LinkedIn post directly from a Jupyter Notebook. Leveraging **LangChain**, **LangGraph**, and the **Groq** LLM (OpenAI gpt‑oss‑120b), the workflow parses notebook cells, feeds the content to prompt templates, and produces polished documentation without manual effort.

## Problem Statement
Creating high‑quality READMEs and accompanying social‑media announcements is time‑consuming and often inconsistent across projects. Developers must repeatedly rewrite similar sections (overview, tech stack, usage) for each new notebook, leading to duplicated work and potential omissions.

## Approach
1. **Notebook Extraction** – `load_notebook()` reads a `.ipynb` file, concatenating markdown and code cells into a single string.  
2. **State Management** – A `ProjectState` TypedDict tracks the notebook content, generated README, and LinkedIn post.  
3. **Prompt Engineering** – Two `PromptTemplate`s define the exact wording for the README and LinkedIn post, ensuring consistent structure and tone.  
4. **LLM Invocation** – `ChatGroq` calls the Groq API with the prepared prompts, returning the generated markdown/text.  
5. **Workflow Orchestration** – `LangGraph` builds a directed graph:  
   - `generate_readme` → `generate_linkedin_post` → `END`.  
   This guarantees the README is produced before the LinkedIn post.  
6. **Output** – The final README and LinkedIn post are saved to `README_generated.md` and `linkedin_post.txt` respectively.

## Tech Stack
| Component | Technology / Library |
|-----------|----------------------|
| Language | Python 3.10+ |
| Notebook handling | `nbformat` |
| Environment variables | `python-dotenv` |
| Prompt templating | `langchain_core.prompts.PromptTemplate` |
| LLM provider | `langchain_groq.ChatGroq` (model: `openai/gpt-oss-120b`) |
| Workflow orchestration | `langgraph.StateGraph` |
| Visualization | `IPython.display.Image` (Mermaid diagram) |
| Dependency management | `requirements.txt` (see below) |

## Project Structure
```
├── .env                # GROQ_API_KEY definition
├── main.ipynb          # Source Jupyter Notebook (example)
├── generate_readme.py  # Core script (the code shown above)
├── README_generated.md # Auto‑generated README (output)
├── linkedin_post.txt   # Auto‑generated LinkedIn post (output)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Results
Running the script produces:
- A fully‑formatted `README_generated.md` containing sections such as Overview, Problem Statement, Tech Stack, Installation, Usage, etc.
- A concise, technically‑oriented LinkedIn post ready for publishing.

Both artifacts are generated in seconds, demonstrating the feasibility of LLM‑driven documentation pipelines.

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/auto-readme-generator.git
   cd auto-readme-generator
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API key**
   - Sign up for a Groq account and obtain an API key.
   - Create a `.env` file in the project root:
     ```
     GROQ_API_KEY=your_groq_api_key_here
     ```

## Usage
```bash
python generate_readme.py
```
The script will:
1. Load `main.ipynb` (or any notebook you point `file_path` to).
2. Generate `README_generated.md` and `linkedin_post.txt` in the project root.
3. Display a Mermaid diagram of the LangGraph workflow.

You can also import the functions into another notebook or script to process multiple notebooks in batch.

## Future Improvements
- **Batch Processing** – Accept a directory of notebooks and generate documentation for each.
- **Customizable Templates** – Provide CLI flags or a config file to modify section ordering, tone, or branding.
- **Multi‑LLM Support** – Plug in alternative providers (OpenAI, Anthropic, Cohere) with a unified interface.
- **Rich Output** – Export README in additional formats (PDF, HTML) and schedule LinkedIn posts via the LinkedIn API.
- **Testing Suite** – Add unit tests for notebook parsing, prompt formatting, and graph execution to ensure reliability.