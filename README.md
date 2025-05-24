# 🧠 Research Paper Assistant (AI Agent System)

This is an AI-powered multi-agent system that helps researchers find and understand the most relevant academic papers on arXiv. It fetches research paper abstracts, summarizes them, infers their topic, and filters out those that don’t match the user’s intent — providing a smarter and more semantic alternative to basic keyword-based search.

---

## ✨ Features

- 🔍 **arXiv Paper Retrieval**: Uses the arXiv API to retrieve paper titles, abstracts, authors, and publication dates based on a user query.
- 📝 **Abstract Summarization**: Leverages the `google/pegasus-xsum` transformer to produce concise summaries of dense research abstracts.
- 🧠 **Topic Inference**: Uses GPT-4 to generate a specific research topic from the abstract.
- ✅ **Relevance Filtering**: Uses GPT-4 to determine whether a paper is actually relevant to the user's query, with a short reason for the decision.
- 📦 **CSV Export**: Outputs a CSV file (`data/results.csv`) with title, summary, topic, and filtering rationale for each relevant paper.

---

## 🧰 Tech Stack

- **Python 3.8+**
- [LangChain](https://www.langchain.com/) (`langchain-openai`)
- [OpenAI GPT-4](https://platform.openai.com/)
- [Hugging Face Transformers](https://huggingface.co/)
  - `google/pegasus-xsum` for summarization
- [arxiv Python package](https://pypi.org/project/arxiv/)
- `pandas` for data handling

---


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/research-assistant-agent.git
cd research-assistant-agent
```
### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set OpenAI API Key
Create a folder named 'data'.
Create `.env` file or edit `config.py`:
```bash
OPENAI_API_KEY = "your-openai-api-key"
```

### 5. usage
```bash
python main.py
```
This will:

- Search arXiv for a default query (you can edit it in main.py)

- Summarize each abstract

- Determine semantic relevance to the query using GPT-4

- Infer a topic for each relevant paper

- Save final results to data/results.csv



## Future Plans

 - Parse full PDFs to go beyond abstracts
  
 - Add GPT-4-powered insights agent to extract key contributions and limitations

 - Build an interactive Streamlit UI
