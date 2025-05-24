from agents.search_agent import search_arxiv, save_results_to_csv
from agents.summarizer_agent import summarize_text
from agents.topic_inference_agent import infer_topic
from agents.relevance_filter_agent import is_relevant_to_query

if __name__ == "__main__":
    query = "Data Science in Biomedical Research"
    print(f"Searching for: {query}")
    papers = search_arxiv(query, max_results=5)

    print("\nEvaluating relevance, summarizing, and classifying...\n")

    filtered = []
    for paper in papers:
        relevance_result = is_relevant_to_query(paper["summary"], query)

        if relevance_result["relevant"]:
            summary = summarize_text(paper["summary"])
            topic = infer_topic(paper["summary"])

            paper["summary_short"] = summary
            paper["topic"] = topic
            paper["reason"] = relevance_result["reason"]

            filtered.append(paper)

            print(f"Relevant: {paper['title']}")
            print(f"Reason: {relevance_result['reason']}")
            print(f"Summary: {summary}")
            print(f"Topic: {topic}\n")

        else:
            print(f"Skipped: {paper['title']}")
            print(f"Reason: {relevance_result['reason']}\n")


    save_results_to_csv(papers)




"""
1. nxt iteration 1 - have llm rephrase the prompt and try different prompts in arxiv to find better papers.
2. Add a Streamlit UI - takes user input and gives related research papers 
3. nxt iteration 2 - understand content from pdfs. 
"""