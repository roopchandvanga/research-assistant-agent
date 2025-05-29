import arxiv
import pandas as pd
from typing import List

def search_arxiv(query: str, max_results: int = 10) -> List[dict]:
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance
    )

    results = []
    for result in search.results():
        results.append({
            "title": result.title.strip().replace('\n', ' '),
            "authors": ", ".join(author.name for author in result.authors),
            "published": result.published.strftime('%Y-%m-%d'),
            "summary": result.summary.strip().replace('\n', ' '),
            "url": result.entry_id
        })

    return results

def save_results_to_csv(results: List[dict], output_path: str = "data/results.csv"):
    df = pd.DataFrame(results)
    df.to_csv(output_path, index=False)
    print(f"Saved {len(results)} papers to {output_path}")

import pandas as pd
import io
from typing import List

def get_csv_download_link(results: List[dict]) -> bytes:
    df = pd.DataFrame(results)
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    return buffer.getvalue().encode("utf-8")

