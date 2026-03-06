# AI‑Powered README & LinkedIn Post Generator for Jupyter Notebooks  

## Overview  
This repository contains a **self‑contained Jupyter notebook** that automatically generates a professional GitHub README and a LinkedIn post from any Jupyter Notebook (`.ipynb`). By leveraging the Groq LLM (via LangChain) and a lightweight state‑graph workflow (LangGraph), the tool extracts the notebook’s markdown and code cells, feeds them to a prompt‑engineered LLM, and writes the resulting artifacts to disk.  

## Problem Statement  
Creating high‑quality documentation and social‑media summaries for data‑science or ML projects is time‑consuming and often inconsistent. Developers must manually:  

1. Read through the notebook to understand its purpose.  
2. Draft a structured README that covers project context, tech stack, usage, etc.  
3. Write a concise LinkedIn post to showcase the work.  

These steps are repetitive, error‑prone, and distract from core development work.  

## Approach  
1. **Load the target notebook** (`main.ipynb`) with `nbformat` and concatenate all markdown and code cells.  
2. **Define two PromptTemplates** (one for the README, one for the LinkedIn post) that instruct the LLM to produce the required output format.  
3. **Build a LangGraph state‑machine** with two nodes:  
   - `generate_readme` – calls the LLM to create the README.  
   - `generate_linkedin_post` – uses the freshly generated README as context to craft a LinkedIn post.  
4. **Execute the graph**, capture the results, and persist them as `README_generated.md` and `linkedin_post.txt`.  
5. **Visualise the workflow** using Mermaid PNG rendering for easy debugging and documentation.  

## Tech Stack  

| Category | Tool / Library | Purpose |
|----------|----------------|---------|
| Language | **Python 3.10+** | Core implementation |
| Notebook handling | `nbformat` | Parse `.ipynb` files |
| Environment variables | `python-dotenv` | Load `GROQ_API_KEY` |
| LLM integration | `langchain-core`, `langchain-groq` | Prompt templating & LLM calls |
| Workflow orchestration | `langgraph` | State‑graph execution |
| Visualization | `IPython.display`, Mermaid | Render graph diagram |
| LLM provider | **Groq** (model `openai/gpt-oss-120b`) | Generate README & LinkedIn text |
| Version control | Git | Repository management |

## Project Structure  

```
├── main.ipynb               # Core notebook that runs the generation pipeline
├── README_generated.md      # Output – auto‑generated README (committed after run)
├── linkedin_post.txt        # Output – auto‑generated LinkedIn post
├── .env.example             # Template for required environment variables
├── requirements.txt         # Python dependencies
└── README.md                # This file (project documentation)
```

*Note:* `main.ipynb` can be renamed or reused to process any other notebook; just update the `file_path` variable.  

## Results  

Running the notebook produces:  

- A **complete, markdown‑formatted README** that follows the industry‑standard sections (title, overview, problem statement, etc.).  
- A **LinkedIn post** written in a technical tone, ready for copy‑pasting.  

Both artifacts are saved automatically, eliminating manual documentation effort.  

## Installation  

1. **Clone the repository**  

   ```bash
   git clone https://github.com/your‑username/ai-readme-generator.git
   cd ai-readme-generator
   ```

2. **Create a virtual environment** (optional but recommended)  

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # on Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**  

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Groq API key**  

   - Copy `.env.example` to `.env`  

     ```bash
     cp .env.example .env
     ```  

   - Add your Groq API key:  

     ```text
     GROQ_API_KEY=your_groq_api_key_here
     ```

5. **Launch the notebook**  

   ```bash
   jupyter lab main.ipynb
   ```

   Execute all cells. The generated files will appear in the repository root.  

## Usage  

- **Generate documentation for a different notebook**:  

  ```python
  file_path = "./path/to/your_notebook.ipynb"
  ```

- **Customise prompts**: Edit the `readme_prompt` or `linkedin_prompt` strings in the notebook to change tone, length, or sections.  

- **Run programmatically** (without Jupyter) – the core logic lives in the notebook cells and can be extracted into a `.py` script if desired.  

## Future Improvements  

| Idea | Description |
|------|-------------|
| **Support multiple LLM providers** | Add adapters for OpenAI, Anthropic, or local LLMs to give users flexibility. |
| **Batch processing** | Accept a directory of notebooks and generate README/LinkedIn files for each in parallel. |
| **Template customization UI** | Simple web UI (e.g., Streamlit) to let users edit prompts and preview output before saving. |
| **Extended output formats** | Generate PDF, HTML, or Confluence pages in addition to markdown. |
| **Automated CI/CD integration** | Hook into GitHub Actions to auto‑update README on each push to `main`. |
| **Error handling & logging** | More robust handling of missing API keys, malformed notebooks, and LLM rate limits. |

---  

*Happy documenting!* 🚀  