# Use this script to find out what buttons are mapped to what on your
# controller should it not be working.
import pygame

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Detected controller: {joystick.get_name()}")
print(f"Buttons: {joystick.get_numbuttons()}")
print(f"Axes: {joystick.get_numaxes()}")
print(f"Hats: {joystick.get_numhats()}")

try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")
            elif event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} released")
            elif event.type == pygame.JOYAXISMOTION:
                print(f"Axis {event.axis} value: {round(event.value, 2)}")
            elif event.type == pygame.JOYHATMOTION:
                print(f"Hat {event.hat} value: {event.value}")

except KeyboardInterrupt:
    pygame.quit()
