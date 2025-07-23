import pytest
from backend.services.parser.google_pse_parser import GooglePSENewsTool

class DummyGoogleService:
    def cse(self):
        class DummyCSE:
            def list(self, q, cx, num):
                class DummyExecute:
                    def execute(self):
                        return {"items": [
                            {"link": "http://example.com", "title": "Test Article", "snippet": "Test snippet."}
                        ]}
                return DummyExecute()
        return DummyCSE()

def test_google_pse_news_tool(monkeypatch):
    tool = GooglePSENewsTool()
    monkeypatch.setattr('backend.services.parser.google_pse_parser.build', lambda *a, **kw: DummyGoogleService())
    results = tool._run("test query")
    assert isinstance(results, list)
    assert results[0]["title"] == "Test Article"
