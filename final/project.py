"""
* CS50P Final project
* Final Project Representer
* by Samu Reinikainen 01.08.2022
"""

from PIL import Image, ImageTk
import tkinter as tk
import pyttsx3
import time
import ast

def main():
    global engine

    slides = get_script()

    width = 1024
    height = 768

    w = window("Final Project Representer", width, height)
    c = canvas(w)

    engine = init_speak()

    slideshow(c, slides)

    w.mainloop()

def get_image(filen: str) -> object:
    """
    Open filepath and return pillow image object.

    :param filen: filepath
    :type filen: str
    :raise FileNotFoundError: If n is not found or is not image file
    :return: Photoimage image object
    :rtype: object
    """
    #img = ImageTk.PhotoImage(Image.open("ball.png"))  
    #canvas.create_image(20, 20, anchor=NW, image=img) 
    try:
        return ImageTk.PhotoImage(Image.open(filen))
    except FileNotFoundError:
        return False

def get_script(filen="script.txt"):
    try:
        with open(filen, "r") as file:
            script = ""
            for line in file:
                script += line.strip()
    except FileNotFoundError:
        exit("Error: script file not found")
           
    try:
        return ast.literal_eval(script)
    except SyntaxError:
        exit("Error: script syntax malformed")

def window(title, width=1024, height=768):
    w = tk.Tk()
    w.geometry(f"{width}x{height}")
    w.title(title)

    return w

def canvas(w):
    c = tk.Canvas(w, bg = '#f0d8c5')
    c.pack(fill="both", expand=True)
    
    return c

def canv_title(canv, width=1024):
    font = "Times 60 italic bold"

    return canv.create_text(width/2, 100, fill="#111354", font=font, justify="center")

def canv_text(canv, width=1024):
    font = "Times 30"

    return canv.create_text(width/2, 300, fill="#111354", font=font, justify="center", width=width-20)

def slideshow(c, slides):
    ctitle = canv_title(c)
    ctext = canv_text(c)

    for slide in slides:
        speak = slide.get("speak", False)
        title = slide.get("title", False)
        text = slide.get("text", False)
        image = slide.get("image", False)
        pause = slide.get("pause", 0)

        view_slide(c, ctitle, title, ctext, text, image, speak)

        time.sleep(pause)

def view_slide(c, ctitle, title, ctext, text, image, speak=False):
    if title:
        c.itemconfig(ctitle, text=title)
    if text:
        c.itemconfig(ctext, text=text)
    if image:
        img = get_image(image)
        if img:
            c.create_image(512, 240, anchor="n", image=img)
    c.update()

    if speak:
        say(speak)

def init_speak():
    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.setProperty("voice", "english-us+f5")
        #engine.setProperty("voice", "finnish")

        return engine
    except:
        exit("Error: speach synthetizer not found")

def say(text):
    global engine

    engine.say(text)
    engine.runAndWait()
    #time.sleep(2)

if __name__ == "__main__":
    main()
