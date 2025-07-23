from backend.services.telegram.bot import TelegramNewsBot

def test_format_message(monkeypatch):
    class DummyTemplate:
        def render(self, article):
            return f"Headline: {article['title']}"
    bot = TelegramNewsBot()
    bot.template = DummyTemplate()
    article = {"title": "Test Headline", "summary": "Summary", "source_url": "http://example.com"}
    msg = bot.format_message(article)
    assert "Test Headline" in msg
