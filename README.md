# Automated README & LinkedIn Post Generator for Jupyter Notebooks  

## Overview  
This repository provides a lightweight, end‑to‑end pipeline that automatically generates a professional GitHub README and an engaging LinkedIn post directly from a Jupyter Notebook (`.ipynb`). By leveraging **LangChain**, **LangGraph**, and **Groq’s LLM** (open‑source `gpt‑oss‑120b`), the solution extracts the notebook’s markdown and code cells, feeds them to carefully crafted prompts, and returns ready‑to‑publish documentation. The workflow is fully reproducible and can be invoked programmatically or interactively within a notebook.  

## Problem Statement  
Data‑focused projects often start with exploratory notebooks. Translating the insights, methodology, and results of those notebooks into a polished README and a concise social‑media summary is a manual, error‑prone step that consumes valuable time. Teams need a reliable way to keep documentation in sync with the source notebook while maintaining a tone that resonates with data analysts, data scientists, ML engineers, and AI developers.  

## Approach  
1. **Notebook Extraction** – `nbformat` reads the notebook and concatenates all markdown and code cells into a single string.  
2. **Prompt Engineering** – Two `PromptTemplate` objects define the exact wording for:  
   * a comprehensive README (sections: title, overview, problem, approach, tech stack, structure, results, installation, usage, future improvements)  
   * an attention‑grabbing LinkedIn post that mirrors the README’s key points.  
3. **LLM Invocation** – `ChatGroq` (Groq’s `gpt‑oss‑120b` model) processes the prompts with a modest temperature (`0.3`) to ensure factual, consistent output.  
4. **State‑Graph Orchestration** – `langgraph.StateGraph` models the workflow as two nodes: `generate_readme` → `generate_linkedin_post`. The graph guarantees deterministic execution and easy extensibility.  
5. **Persistence** – The generated README and LinkedIn post are written to `README_generated.md` and `linkedin_post.txt` respectively for immediate use.  

## Tech Stack  
| Category | Library / Tool | Version (example) |
|----------|----------------|-------------------|
| Language | Python | ≥ 3.9 |
| Notebook handling | `nbformat` | 5.x |
| Environment variables | `python-dotenv` | 1.x |
| Prompt & LLM orchestration | `langchain-core`, `langchain-groq` | 0.2.x |
| Workflow graph | `langgraph` | 0.0.x |
| LLM provider | Groq (`gpt‑oss‑120b`) | API |
| Visualization | `IPython.display` (Mermaid PNG) | – |
| Dependency management | `pip` / `requirements.txt` | – |

## Project Structure  

```
├── main.ipynb                # Core notebook implementing the pipeline
├── README_generated.md       # Output file – auto‑generated README
├── linkedin_post.txt         # Output file – auto‑generated LinkedIn post
├── .env                      # Stores GROQ_API_KEY (not committed)
├── requirements.txt          # Python dependencies
└── utils.py (optional)       # Helper functions (load_notebook, run_pipeline)
```

*`main.ipynb`* contains the full implementation, from environment loading to graph compilation and result persistence.  

## Results  
Running the notebook with a valid Groq API key produces two artefacts:

* **`README_generated.md`** – a fully‑formatted README covering all required sections, ready to replace the repository’s default README.  
* **`linkedin_post.txt`** – a concise, professional LinkedIn post that highlights the project’s purpose, tech stack, and a concrete next step for improvement.  

Both outputs follow the tone guidelines (natural, formal, straightforward) and are tailored to a data‑oriented audience.  

## Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your‑username/auto-readme-generator.git
   cd auto-readme-generator
   ```

2. **Create a virtual environment (recommended)**  
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Groq API key**  
   Create a `.env` file in the project root:  
   ```dotenv
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Verify the setup** (optional)  
   ```bash
   python -c "import os; print('API key loaded' if os.getenv('GROQ_API_KEY') else 'Missing key')"
   ```

## Usage  

### From the Notebook  
Open `main.ipynb` in JupyterLab / VS Code and run all cells. The pipeline will:

1. Load `main.ipynb` (or any notebook you point `file_path` to).  
2. Generate `README_generated.md` and `linkedin_post.txt`.  
3. Display the workflow graph as a PNG for visual confirmation.  

### Programmatically  

```python
from utils import load_notebook, run_pipeline

# Load any notebook you wish to document
nb_content = load_notebook("path/to/your_notebook.ipynb")

# Execute the graph and retrieve results
result = run_pipeline(nb_content)

print("README:\n", result["readme"])
print("\nLinkedIn Post:\n", result["linkedin_post"])
```

Replace `"path/to/your_notebook.ipynb"` with the target notebook. The `run_pipeline` function encapsulates the graph invocation, making it easy to integrate into CI/CD pipelines or automated reporting scripts.  

## Future Improvements  

| Area | Proposed Enhancement |
|------|----------------------|
| **Prompt Customization** | Allow users to supply their own templates (e.g., additional sections, branding guidelines). |
| **Multi‑modal Output** | Generate HTML or PDF versions of the README for richer documentation portals. |
| **Batch Processing** | Extend the pipeline to accept a directory of notebooks and produce a documentation bundle. |
| **Interactive UI** | Build a lightweight Streamlit / Gradio front‑end for non‑technical users to upload notebooks and download artefacts. |
| **Model Flexibility** | Support alternative LLM providers (OpenAI, Anthropic, HuggingFace) with a simple config switch. |
| **Testing & Validation** | Add unit tests that verify the presence of required sections and enforce length limits for LinkedIn posts. |

Contributions that address any of the above (or introduce new capabilities) are welcome—please open an issue or submit a pull request.  

---  

*Happy documenting!*  