import pygame
import threading
import os
import config

# Input handling functions


def start_controller_thread(button_pressed_callback):
    thread = threading.Thread(
        target=controller_loop,
        args=(button_pressed_callback,),
        daemon=True
    )
    thread.start()


def controller_loop(button_pressed_callback):
    os.environ["SDL_VIDEODRIVER"] = "dummy"
    pygame.init()
    if os.name == 'nt':
        pygame.display.init()
    pygame.joystick.init()

    if pygame.joystick.get_count() == 0:
        return

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    prev_states = {"lt": False, "rt": False}
    button_map = config.controller_config["button_map"]
    axis_map = config.controller_config["axis_map"]
    threshold = config.controller_config["trigger_threshold"]

    running = True
    while running:
        lt_state = joystick.get_axis(axis_map["lt"]) > threshold
        rt_state = joystick.get_axis(axis_map["rt"]) > threshold

        if lt_state != prev_states["lt"]:
            button_pressed_callback("lt", lt_state)
            prev_states["lt"] = lt_state

        if rt_state != prev_states["rt"]:
            button_pressed_callback("rt", rt_state)
            prev_states["rt"] = rt_state

        for event in pygame.event.get():
            if event.type in (pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP):
                button_name = button_map.get(event.button)
                if button_name:
                    pressed = (event.type == pygame.JOYBUTTONDOWN)
                    button_pressed_callback(button_name, pressed)

            elif event.type == pygame.JOYHATMOTION:
                x, y = event.value
                button_pressed_callback("Left", x == -1)
                button_pressed_callback("Right", x == 1)
                button_pressed_callback("Up", y == 1)
                button_pressed_callback("Down", y == -1)

        pygame.event.pump()
        pygame.time.wait(10)
