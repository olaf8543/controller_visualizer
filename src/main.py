import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QObject, pyqtSignal
from controller_ui import create_window, on_resize, handle_button_press
from input_handler import start_controller_thread

# Minimal signal class (necessary for cross-thread communication)


class ControllerSignals(QObject):
    button_pressed = pyqtSignal(str, bool)


def main():
    app = QApplication(sys.argv)

    # Create UI
    win = create_window()

    # Setup signals
    signals = ControllerSignals()
    signals.button_pressed.connect(handle_button_press)

    # Start controller thread with callback
    start_controller_thread(signals.button_pressed.emit)

    # Connect resize handler
    win.resizeEvent = lambda event: on_resize(event, win)

    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
