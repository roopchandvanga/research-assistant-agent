import streamlit as st
from agents.search_agent import search_arxiv, get_csv_download_link
from agents.summarizer_agent import summarize_text
from agents.topic_inference_agent import infer_topic
from agents.relevance_filter_agent import is_relevant_to_query

st.title("Research Paper Relevance Assistant")
st.markdown("Uses GPT-4 to filter, summarize, and classify arXiv papers.")

query = st.text_input("Enter your research topic:", "Data Science in Biomedical Research")
max_papers = st.slider("Number of papers to fetch", 1, 10, 5)

if st.button("Analyze"):
    st.info(f"Searching for: *{query}*")
    papers = search_arxiv(query, max_results=max_papers)

    filtered = []
    for i, paper in enumerate(papers, 1):
        with st.expander(f"📄 {i}. {paper['title']}", expanded=True):
            relevance_result = is_relevant_to_query(paper["summary"], query)

            if relevance_result["relevant"]:
                summary = summarize_text(paper["summary"])
                topic = infer_topic(paper["summary"])
                paper["summary_short"] = summary
                paper["topic"] = topic
                paper["reason"] = relevance_result["reason"]
                filtered.append(paper)

                st.success("✅ Relevant to the query")
                st.markdown(f"**Reason:** {relevance_result['reason']}")
                st.markdown(f"**Topic:** {topic}")
                st.markdown(f"**Summary:** {summary}")
                st.markdown(f"**📅 Published on:** {paper['published']}")


            else:
                st.error("❌ Not relevant to the query")
                st.markdown(f"**Reason:** {relevance_result['reason']}")

    if filtered:
        csv_data = get_csv_download_link(filtered)

        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="relevant_papers.csv",
            mime="text/csv"
)
    else:
        st.warning("No relevant papers found.")
