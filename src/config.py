# Button layout configuration
BUTTONS = [
    {"name": "Left", "position": (0.005, 0.041)},
    {"name": "Down", "position": (0.160, 0.041)},
    {"name": "Right", "position": (0.278, 0.229)},
    {"name": "Up", "position": (0.341, 0.655)},
    {"name": "x", "position": (0.423, 0.109)},
    {"name": "a", "position": (0.409, 0.377)},
    {"name": "y", "position": (0.565, 0.005)},
    {"name": "b", "position": (0.551, 0.273)},
    {"name": "rb", "position": (0.710, 0.024)},
    {"name": "rt", "position": (0.697, 0.292)},
    {"name": "lb", "position": (0.855, 0.062)},
    {"name": "lt", "position": (0.841, 0.340)},
]

# Visual settings
biggerUpBtn = True
transparentBackground = False
app_background = "rgba(255, 0, 255, 1)"
button_background = "rgba(200, 200, 200, 1)"
button_text = "rgba(30, 30, 30, 1)"
button_outline = "rgba(6, 0, 43, 1)"
button_glow = "rgba(0, 255, 167, 1)"
button_glow_text = "rgba(0, 0, 0, 1)"

# Controller mapping
controller_config = {
    "button_map": {
        0: "a",
        1: "b",
        2: "x",
        3: "y",
        4: "lb",
        5: "rb",
    },
    "axis_map": {
        "lt": 2,
        "rt": 5,
    },
    "trigger_threshold": 0.5
}
