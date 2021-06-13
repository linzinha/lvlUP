# lvlUP
Healthy habits competition app in python using Tkinter

# Requirements:

txt file isn't populating on Pycharm so it's possible nothing is needed but in the code you'll find these imports:

import json
import tkinter as tk
from tkinter import *

# To Run:

1. Make sure you're running the program from within the lvlUP folder, otherwise the json file won't be found
2. run `python3 main.py`


# Notes
* It's currently hardcoded to myself/my husbands names because this is a personal project, but I'm looking to change that (see https://github.com/linzinha/lvlUP/issues/2). 
* All point data added to the game will increase that category by that value. If you make a mistake, you can currently revert to the previous save by checking for the appropriately timestamped JSON file, and copy/pasting it's content into the stats.json file.
* You can also try decreasing value with a negative number for categories that allow that, though I'm considering adding override rewrite capability for all activities
