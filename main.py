from tkinter import *
import threading
from stars import Star
import time

class Interface:
    def __init__(self, *arg):
        self.window = Tk()
        self.window.title("Galaxy")
        self.window.config(bg="black")
        self.window.resizable(0,0)

        #center interface
        width = self.window.winfo_screenwidth() #x
        height = self.window.winfo_screenheight() #y
        self.x = (width - 800) // 2
        self.y = (height - 500) // 2
        self.window.geometry(f"800x500+{self.x}+{self.y}")

        self.text_label = Label(self.window,text="Stars", fg="white", bg="black")
        self.text_label.place(x=10, y=10)

        self.text_entry = Entry(self.window)
        self.text_entry.place(x=50, y=10)

        self.qt_stars = Button(self.window, text="Generate", fg="white", bg="black", 
            command=lambda: threading.Thread(target=self.star.run_generate).start())
        self.qt_stars.place(x=200, y=8)

        self.explode_stars_button = Button(self.window, text="Explode All", fg="white", bg="black",
            command=lambda: threading.Thread(target=self.star.run_explode).start())
        self.explode_stars_button.place(x=270, y=8)

        self.star = Star(self.window, self.text_entry, self.qt_stars, self.explode_stars_button)

        self.window.mainloop()

if __name__ == "__main__":
    Interface()
