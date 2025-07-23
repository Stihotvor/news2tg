from nicegui import ui

ui.label('NewsBot Simple Admin Panel')
ui.link('Open FastAPI docs', 'http://localhost:8000/docs')

with ui.row():
    ui.button('Show Hello', on_click=lambda: ui.notify('Hello from NiceGUI!'))
    ui.button('Show Info', on_click=lambda: ui.notify('NewsBot is running.'))

ui.run(port=8080, host='0.0.0.0')
