from langchain.tools import BaseTool
from googleapiclient.discovery import build
import os

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID')

class GooglePSENewsTool(BaseTool):
    name = "google_pse_news"
    description = "Fetch news articles using Google Programmable Search Engine. Returns a list of articles with URL, title, and snippet."

    def _run(self, query: str, **kwargs):
        service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
        res = service.cse().list(q=query, cx=GOOGLE_CSE_ID, num=10).execute()
        articles = []
        for item in res.get("items", []):
            articles.append({
                "url": item.get("link"),
                "title": item.get("title"),
                "snippet": item.get("snippet"),
            })
        return articles

    async def _arun(self, query: str, **kwargs):
        # For async support, fallback to sync for now
        return self._run(query, **kwargs)
