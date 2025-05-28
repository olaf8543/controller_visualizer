# Leverless Controller Visualizer
This is a visualizer for a leverless controller, meaning when you press a button on your
controller, the button on the visualizer will light up at the same time.
[Here is a demo](https://youtu.be/QLb7bwcPBwE)

### Installation
To use the visualizer, clone this repo and run `pip install -r requirements.txt`
from there, the visualizer might not work with your specific controller. 

You can run the visualizer with `python src/main.py`, And test to see if 
all of the buttons work. If they don't, run `python src/test_controller.py`
this will run a program in your terminal that will print the button value of
any button you press. This will make it easier to figure out which button is
which. From there, you can configure what button on your controller maps to 
each value by going to `src/config.py` and changing the values of the 
controller mappings to match your specific buttons. There are also ways
to configure various parts of the visualizer in the same file. 

### Transparency
In the demo, The background of the visualizer is transparent. This functionality
does not work on windows, but how I did it in the demo is to use OBS's color key
filters to remove either a magenta, cyan or any color background from an app, 
which is typical for something like this, because you usually don't want the 
visualizer to be blocking your sight while you are playing. You can adjust the 
transparency of the background in `src/config.py` if you are not on windows and
if you are, you can also change the color of the background in the same file in 
order to use OBS's color key filter.

