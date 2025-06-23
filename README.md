# 🧠 Research Paper Assistant (AI Agent System)

This is lightweight AI research assistant agent that helps researchers find and understand the most relevant academic papers on arXiv. It fetches research paper abstracts, summarizes them, infers their topic, and filters out those that don’t match the user’s intent — providing a smarter and more semantic alternative to basic keyword-based search.

[🌐 View the Live App on hosted on Streamlit](https://research-assistant-agent-gyhymztxkt68zthbafj7co.streamlit.app/)


---

## ✨ Features

- 🔍 **arXiv Paper Retrieval**: Uses the arXiv API to retrieve paper titles, abstracts, authors, and publication dates based on a user query.
- 📝 **Abstract Summarization**: Leverages the `facebook/bart-large-cnn` transformer to produce concise summaries of dense research abstracts.
- 🧠 **Topic Inference**: Uses GPT-4 to generate a specific research topic from the abstract.
- ✅ **Relevance Filtering**: Uses GPT-4 to determine whether a paper is actually relevant to the user's query, with a short reason for the decision.
- 📦 **CSV Download**: Saves a CSV file (`data/results.csv`) with title, summary, topic, and filtering rationale for each relevant paper and allows users to download it.

---

## 🧰 Tech Stack

- **Python 3.11**
- [OpenAI GPT-4](https://platform.openai.com/)
- [Hugging Face Transformers](https://huggingface.co/)
  - `facebook/bart-large-cnn` for summarization
- [arxiv Python package](https://pypi.org/project/arxiv/)
- Streamlit for UI

---


