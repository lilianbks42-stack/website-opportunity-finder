import os

from dotenv import load_dotenv
from tavily import TavilyClient


load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise RuntimeError("TAVILY_API_KEY is missing from the .env file")


client = TavilyClient(api_key=TAVILY_API_KEY)


def search_web(query, max_results=5):
    response = client.search(
        query=query,
        max_results=max_results,
        search_depth="basic",
    )

    return response.get("results", [])


if __name__ == "__main__":
    results = search_web(
        '"looking for a website developer" Kenya'
    )

    print("\nWebsite Opportunity Finder - Search Test")
    print("-----------------------------------------")

    for result in results:
        print("\nTitle:", result.get("title"))
        print("URL:", result.get("url"))
        print("Content:", result.get("content", "")[:500])