biggerUpBtn = True
# Doesn't work on windows
transparentBackground = False
# Background for the app, Look at README.md for more info
app_background = "rgba(255, 0, 255, 1)"

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
        # "a": 0,
        # "b": 1,
        # "x": 2,
        # "y": 3,
        # "lb": 4,
        # "rb": 5,
        0: "a",
        1: "b",
        2: "x",
        3: "y",
        4: "lb",
        5: "rb",
        # These are unneccessary on my build, but are included for reference,
        # if you would need to change anything
        # "lt": 6,
        # "rt": 7,
        # "Up": 8,
        # "Down": 9,
        # "Left": 10,
        # "Right": 11,
    },
    "axis_map": {
        # "lt": 2,
        # "rt": 5,
        2: "lt",
        5: "rt",
    },
    "trigger_threshold": 0.5
}
