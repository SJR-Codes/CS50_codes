"""
* CS50P Final project
* Final Project Representer
* by Samu Reinikainen 01.08.2022
"""

from PIL import Image, ImageTk
import tkinter as tk
import pyttsx3

def main():
    n = int(input("Give n: "))

    for s in sheep(n):
        print(s)




if __name__ == "__main__":
    main()