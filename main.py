from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
import config


"""Global State"""
buttons = []
current_width = 800
current_height = 450
current_radius = int((min(current_width, current_height) * (20 / 100)) / 2)

"""
The Configuration for each button, NOT where
each of the buttons are stored (buttons = [])
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

"""configuring varibles because of any changes from config file"""


def create_buttons(window):
    for button_config in BUTTONS:
        button = QPushButton(window)
        update_stylesheet(button)
        buttons.append(button)


def update_stylesheet(button):
    radius = int(button.width() / 2)
    border_width = int(radius / 5)
    stylesheet = """
            QPushButton {
                background-color: """ + config.button_background + """;
                border: """ + str(border_width) + """px solid """ + config.button_outline + """;
                border-radius:""" + str(radius) + """px;
                color: """ + config.button_text + """;
            }
            QPushButton:pressed {
                background-color: """ + config.button_glow + """;
                color: """ + config.button_glow_text + """;
            }
        """
    button.setStyleSheet(stylesheet)


def update_positions():
    for button, button_config in zip(buttons, BUTTONS):
        position = button_config["position"]
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


def main():
    app = QApplication([])
    win = QWidget()
    win.resize(current_width, current_height)

    create_buttons(win)
    update_positions()

    win.resizeEvent = lambda event: on_resize(event, win)

    win.show()
    app.exec()


if __name__ == "__main__":
    main()
