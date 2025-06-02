from PyQt6.QtWidgets import QWidget, QPushButton
from PyQt6.QtCore import Qt
import config

# UI State
buttons = {}
current_width = 800
current_height = 450


def create_window():
    win = QWidget()
    win.resize(current_width, current_height)

    if config.transparentBackground:
        win.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    else:
        win.setStyleSheet(f"background-color: {config.app_background};")

    create_buttons(win)
    update_positions()

    return win


def create_buttons(window):
    for button_config in config.BUTTONS:
        button = QPushButton(window)
        update_stylesheet(button)
        buttons[button_config["name"]] = button


def update_stylesheet(button):
    radius = int(button.width() / 2)
    border_width = int(radius / 5)
    stylesheet = f"""
        QPushButton {{
            background-color: {config.button_background};
            border: {border_width}px solid {config.button_outline};
            border-radius: {radius}px;
            color: {config.button_text};
        }}
        QPushButton:pressed {{
            background-color: {config.button_glow};
            color: {config.button_glow_text};
        }}
    """
    button.setStyleSheet(stylesheet)


def update_positions():
    global current_width, current_height

    for button_name in buttons:
        button_config = next(
            b for b in config.BUTTONS if b["name"] == button_name)
        position = button_config["position"]
        button = buttons[button_name]

        x = int(current_width * position[0])
        y = int(current_height * position[1])
        diameter = int(min(current_width, current_height) * (24 / 100))

        if button_name == "Up" and config.biggerUpBtn:
            ratio = diameter / 24
            diameter = int(ratio * 30)

        button.setGeometry(x, y, diameter, diameter)
        update_stylesheet(button)


def on_resize(event, widget):
    global current_width, current_height
    current_width = widget.width()
    current_height = widget.height()
    update_positions()


def handle_button_press(name, pressed):
    if name in buttons:
        buttons[name].setDown(pressed)
