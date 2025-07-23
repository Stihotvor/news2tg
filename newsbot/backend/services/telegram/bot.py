import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from python_telegram_bot import Bot

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates')
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')

class TelegramNewsBot:
    def __init__(self, template_name='news_message.j2'):
        self.env = Environment(
            loader=FileSystemLoader(TEMPLATES_DIR),
            autoescape=select_autoescape(['j2', 'html'])
        )
        self.template = self.env.get_template(template_name)
        self.bot = Bot(token=TELEGRAM_BOT_TOKEN)
        self.channel_id = TELEGRAM_CHANNEL_ID

    def format_message(self, article: dict) -> str:
        """Render the news message from template and article dict."""
        return self.template.render(article=article)

    def send_message(self, article: dict):
        """Format and send the news message to the Telegram channel."""
        message = self.format_message(article)
        self.bot.send_message(chat_id=self.channel_id, text=message, parse_mode='HTML')
