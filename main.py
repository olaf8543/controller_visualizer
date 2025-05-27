from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtCore import pyqtSignal, QObject, Qt
import pygame
import threading
import os
import config


# Class that sends that allows the signla to send the button that was pressed
class ControllerSignals(QObject):
    button_pressed = pyqtSignal(str, bool)


"""Global State"""
buttons = dict()
current_width = 800
current_height = 450
current_radius = int((min(current_width, current_height) * (20 / 100)) / 2)
signals = ControllerSignals()

"""
The Configuration for each button, NOT where
each of the buttons are stored (buttons dictionary)
"""
BUTTONS = [
    # Movement Buttons
    {"name": "Left", "position": (0.005, 0.041)},
    {"name": "Down", "position": (0.160, 0.041)},
    {"name": "Right", "position": (0.278, 0.229)},
    {"name": "Up", "position": (0.341, 0.655)},

    # Attack Buttons
    {"name": "x", "position": (0.423, 0.109)},
    {"name": "a", "position": (0.409, 0.377)},
    {"name": "y", "position": (0.565, 0.005)},
    {"name": "b", "position": (0.551, 0.273)},
    {"name": "rb", "position": (0.710, 0.024)},
    {"name": "rt", "position": (0.697, 0.292)},
    {"name": "lb", "position": (0.855, 0.062)},
    {"name": "lt", "position": (0.841, 0.340)},
]


def create_buttons(window):
    for button_config in BUTTONS:
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
    for button_key, button_config in zip(buttons, BUTTONS):
        position = button_config["position"]
        button = buttons[button_key]
        name = button_config["name"]
        x = int(current_width * position[0])
        y = int(current_height * position[1])
        diameter = int(min(current_width, current_height)
                       * (24 / 100))
        # leverless controllers have 24mm buttons and a 30mm up button,
        # So I will be keeping the same ratio here
        if (name == "Up"):
            if (config.biggerUpBtn):
                ratio = diameter / 24
                diameter = (int)(ratio * 30)
        button.setGeometry(x, y, diameter, diameter)
        update_stylesheet(button)


def on_resize(event, widget):
    global current_width, current_height
    current_width = widget.width()
    current_height = widget.height()
    update_positions()


def handle_button_press(name, pressed):
    if name in buttons:
        button = buttons[name]
        button.setDown(pressed)


# Run a constant threaded loop that checks the controller
# for button presses.
def controller_loop():
    os.environ["SDL_VIDEODRIVER"] = "dummy"
    pygame.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        # No controller detected
        return

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    prev_states = {
        "lt": False,
        "rt": False
    }

    button_map = config.controller_config["button_map"]
    axis_map = config.controller_config["axis_map"]
    threshold = config.controller_config["trigger_threshold"]

    running = True
    while running:
        lt_state = joystick.get_axis(axis_map["lt"]) > threshold
        rt_state = joystick.get_axis(axis_map["rt"]) > threshold

        if lt_state != prev_states["lt"]:
            signals.button_pressed.emit("lt", lt_state)
            prev_states["lt"] = lt_state

        if rt_state != prev_states["rt"]:
            signals.button_pressed.emit("rt", rt_state)
            prev_states["rt"] = rt_state

        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                button_name = list(button_map.keys())[
                    list(button_map.values()).index(event.button)]
                handle_button_press(button_name, True)
            elif event.type == pygame.JOYBUTTONUP:
                button_name = list(button_map.keys())[
                    list(button_map.values()).index(event.button)]
                handle_button_press(button_name, False)
            elif event.type == pygame.JOYHATMOTION:
                x, y = event.value
                signals.button_pressed.emit("Left", x == -1)
                signals.button_pressed.emit("Right", x == 1)
                signals.button_pressed.emit("Up", y == 1)
                signals.button_pressed.emit("Down", y == -1)
        pygame.event.pump()
        pygame.time.wait(10)


def main():
    app = QApplication([])
    win = QWidget()
    win.resize(current_width, current_height)
    # Transparent background
    win.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    create_buttons(win)
    update_positions()

    signals.button_pressed.connect(handle_button_press)

    # Start Controller Thread
    controller_thread = threading.Thread(target=controller_loop, daemon=True)
    controller_thread.start()

    win.resizeEvent = lambda event: on_resize(event, win)
    win.show()
    app.exec()


if __name__ == "__main__":
    main()
