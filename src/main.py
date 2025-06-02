import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QObject, pyqtSignal
from controller_ui import create_window, on_resize, handle_button_press
from input_handler import start_controller_thread


class ControllerSignals(QObject):
    button_pressed = pyqtSignal(str, bool)


def main():
    app = QApplication(sys.argv)

    win = create_window()

    signals = ControllerSignals()
    signals.button_pressed.connect(handle_button_press)

    start_controller_thread(signals.button_pressed.emit)

    win.resizeEvent = lambda event: on_resize(event, win)

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
