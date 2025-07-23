from backend.services.summarizer import gemini

def test_summarize_article(monkeypatch):
    class DummyChain:
        def __call__(self, inputs):
            return {
                "summary": "Short summary.",
                "topic": "technology",
                "language": "en"
            }
    monkeypatch.setattr(gemini, 'summarizer_chain', DummyChain())
    result = gemini.summarize_article("Some article text.")
    assert result["summary"] == "Short summary."
    assert result["topic"] == "technology"
    assert result["language"] == "en"
