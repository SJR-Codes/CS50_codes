"""
* CS50P Final project
* Final Project Representer
* by Samu Reinikainen 01.08.2022
"""

from PIL import Image, ImageTk
import tkinter as tk
import pyttsx3

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()



def main():
    #myapp = App()
    #myapp.master.title("My Do-Nothing Application")
    #myapp.master.maxsize(1000, 400)

    # start the program
    #myapp.mainloop()

    engine = pyttsx3.init()
    engine.say("We'll, um, hi, um, hello")
    engine.runAndWait()




if __name__ == "__main__":
    main()