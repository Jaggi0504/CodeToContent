# Automated README & LinkedIn Post Generator for Jupyter Notebooks  

## Overview  
This repository provides an end‑to‑end pipeline that reads a Jupyter Notebook (`.ipynb`), extracts its code and markdown cells, and leverages a large language model (LLM) via LangChain to automatically generate a polished GitHub README and an engaging LinkedIn post. The solution is fully reproducible, requires minimal configuration, and is designed for data‑focused professionals who want to streamline documentation and social‑media sharing of their notebook‑based projects.  

## Problem Statement  
Data analysts, data scientists, ML engineers, and AI developers frequently create notebooks to explore data, prototype models, and share insights. However, crafting a comprehensive README and a compelling LinkedIn announcement is often manual, time‑consuming, and inconsistent. The lack of automated, high‑quality documentation can hinder project onboarding, reproducibility, and visibility.  

## Approach  
1. **Notebook Extraction** – Load the target notebook with `nbformat`, concatenate all markdown and code cells into a single string.  
2. **State Management** – Define a typed state (`ProjectState`) that holds the notebook content, generated README, and LinkedIn post.  
3. **Prompt Engineering** – Create two `PromptTemplate` objects:  
   * `readme_prompt` instructs the LLM to produce a structured README.  
   * `linkedin_prompt` asks the LLM to craft a professional LinkedIn post based on the README.  
4. **Graph Workflow** – Use `langgraph.StateGraph` to orchestrate two nodes:  
   * `generate_readme` → calls the LLM with `readme_prompt`.  
   * `generate_linkedin_post` → consumes the generated README and produces the LinkedIn copy.  
5. **Execution & Persistence** – Invoke the graph, print both outputs, and write them to `README_generated.md` and `linkedin_post.txt`.  

The pipeline is encapsulated in a single function `run_pipeline(notebook_content)` for easy reuse.  

## Tech Stack  
| Component | Library / Service | Version* |
|-----------|-------------------|----------|
| Notebook parsing | `nbformat` | >=5.0 |
| Environment variables | `python-dotenv` | >=1.0 |
| LLM integration | `langchain-core`, `langchain-groq` | latest |
| Graph orchestration | `langgraph` | latest |
| LLM model | Groq `openai/gpt-oss-120b` | – |
| Visualization | `IPython.display` (for graph PNG) | – |
| Language | Python 3.9+ | – |

\*Exact versions are defined in `requirements.txt`.  

## Project Structure  

```
├── main.ipynb                # Example notebook used as input
├── generate_readme.py        # Core pipeline (the code shown above)
├── README_generated.md       # Auto‑generated README (output)
├── linkedin_post.txt         # Auto‑generated LinkedIn post (output)
├── .env                      # Stores GROQ_API_KEY (not committed)
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```  

*`generate_readme.py`* contains all logic: loading the notebook, defining prompts, building the state graph, and persisting results.  

## Results  
Running the pipeline on `main.ipynb` produces:  

* A fully‑formatted GitHub README that follows best‑practice sections (title, overview, problem statement, etc.).  
* A concise, professional LinkedIn post ready for publishing, highlighting the project's purpose, tools, and next steps.  

Both artifacts are saved automatically, eliminating manual copy‑paste and ensuring consistency between documentation and social media messaging.  

## Installation  

```bash
# Clone the repository
git clone https://github.com/your-username/auto-readme-generator.git
cd auto-readme-generator

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your Groq API key:
# GROQ_API_KEY=your_groq_api_key_here
```  

## Usage  

```python
from generate_readme import run_pipeline, load_notebook

# Load any notebook you wish to document
notebook_path = "./my_analysis.ipynb"
content = load_notebook(notebook_path)

# Run the automated pipeline
result = run_pipeline(content)

# Access generated artifacts
print(result["readme"])          # Prints the README markdown
print(result["linkedin_post"])   # Prints the LinkedIn post

# Files are also written to README_generated.md and linkedin_post.txt
```  

You can also execute the notebook directly (e.g., via Jupyter) to see the graph visualization and interactive outputs.  

## Future Improvements  

| Area | Planned Enhancement |
|------|----------------------|
| **Model Flexibility** | Allow switching between Groq, OpenAI, Anthropic, or local LLMs via configuration. |
| **Customizable Prompts** | Expose prompt templates as external YAML/JSON files for project‑specific wording. |
| **Multi‑Notebook Support** | Batch process a directory of notebooks and generate a consolidated documentation site. |
| **CI/CD Integration** | Add GitHub Actions to auto‑generate README on each push/PR. |
| **Rich Media Extraction** | Detect and embed images/plots from notebook cells into the README. |
| **User Interface** | Provide a lightweight Streamlit or FastAPI front‑end for non‑technical users. |

---  

*Happy documenting!*  