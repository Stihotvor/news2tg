# NiceGUI Admin Panel
from nicegui import ui

def list_recent_articles():
    ui.label('Recent Articles')
    # Placeholder: Replace with real DB/API call
    with ui.table(columns=['ID', 'Title', 'Published', 'Status'], rows=[
        {'ID': 1, 'Title': 'Sample News', 'Published': '2025-07-23', 'Status': 'new'},
    ]):
        pass

def manage_sources():
    ui.label('Manage RSS/API Sources')
    ui.input('Add new source URL')
    ui.button('Add Source')
    # Placeholder: List sources
    ui.table(columns=['Source', 'Type'], rows=[{'Source': 'https://example.com/rss', 'Type': 'RSS'}])

def schedule_posts():
    ui.label('Schedule Posts (Celery Beat)')
    ui.input('Cron Expression', value='*/15 * * * *')
    ui.button('Update Schedule')
    # Placeholder: List scheduled jobs
    ui.table(columns=['Task', 'Schedule'], rows=[{'Task': 'Fetch News', 'Schedule': '*/15 * * * *'}])

def settings():
    ui.label('Settings: Languages & Channels')
    ui.input('Supported Languages', value='en,uk,ru')
    ui.input('Telegram Channels', value='@news_channel')
    ui.button('Save Settings')

with ui.tabs() as tabs:
    with ui.tab('Articles'):
        list_recent_articles()
    with ui.tab('Sources'):
        manage_sources()
    with ui.tab('Schedule'):
        schedule_posts()
    with ui.tab('Settings'):
        settings()

ui.run()
