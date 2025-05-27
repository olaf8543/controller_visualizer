biggerUpBtn = True

# Colors for the buttons. supports hex, rgba, or verbal color names
# eg. button_background = "green"
#     button_background = "#FF0000"
#     button_background = "rgba(50, 50, 50, 1)"
button_background = "rgba(200, 200, 200, 1)"
button_text = "rgba(30, 30, 30, 1)"
button_outline = "rgba(6, 0, 43, 1)"
button_glow = "rgba(0, 255, 167, 1)"
button_glow_text = "rgba(0, 0, 0, 1)"


# Button mappings in case the buttons are not in the correct order
controller_config = {
    "button_map": {
        "a": 0,
        "b": 1,
        "x": 2,
        "y": 3,
        "lb": 4,
        "rb": 5,
        "lt": 6,
        "rt": 7,
    },
    "axis_map": {
        "lt": 2,
        "rt": 5,
    },
    "trigger_threshold": 0.5
}
