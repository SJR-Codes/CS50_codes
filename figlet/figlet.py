"""
* CS50P Problem Set 4
* Frank, Ian and Glen’s Letters
* by Samu Reinikainen 25.07.2022
"""

import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
#You can then get a list of available fonts with code like this:

fonts = figlet.getFonts()

#You can set the font with code like this, wherein f is the font’s name as a str:
figlet.setFont(font=f)

#And you can output text in that font with code like this, wherein s is that text as a str:
print(figlet.renderText(s))