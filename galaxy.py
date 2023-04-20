from tkinter import *
import time
import threading
import random

class Galaxy:
    def __init__(self, qnt):
        self.win = Tk()
        self.win.geometry("800x500")
        self.win.title("Galaxy")
        self.win.resizable(0,0)
        self.win.config(bg="black")
        self.gen = False
        self.t = time.sleep

        self.win.mainloop()

if __name__ == "__main__":
    threading.Thread(Galaxy()).start()
