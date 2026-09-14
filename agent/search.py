import os

from dotenv import load_dotenv
from tavily import TavilyClient


load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise RuntimeError("TAVILY_API_KEY is missing from the .env file")


client = TavilyClient(api_key=TAVILY_API_KEY)


REDDIT_QUERIES = [
    "site:reddit.com looking for someone to build a website",
    "site:reddit.com looking to hire a web designer",
    "site:reddit.com can anyone recommend a web designer",
    "site:reddit.com need someone to build a website",
    "site:reddit.com looking for a website developer for my business",
    "site:reddit.com looking to pay someone to build a website",
    "site:reddit.com need a website for my business",
    "site:reddit.com looking to build a website for my business",
]


def search_web(query, max_results=5):
    response = client.search(
        query=query,
        max_results=max_results,
        search_depth="advanced",
        include_answer=False,
        include_raw_content=True,
    )

    return response.get("results", [])


def search_reddit(max_results_per_query=5):
    results = []

    for query in REDDIT_QUERIES:
        print(f"\nSearching Reddit for: {query}")

        search_results = search_web(
            query,
            max_results=max_results_per_query,
        )

        results.extend(search_results)

    return results


if __name__ == "__main__":
    results = search_reddit(max_results_per_query=3)

    print("\n")
    print("Website Opportunity Finder - Reddit Discovery Test")
    print("--------------------------------------------------")

    for result in results:
        print("\nTITLE:", result.get("title"))
        print("URL:", result.get("url"))
        print("TEXT:", result.get("content", "")[:500])
