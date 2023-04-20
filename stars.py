from tkinter import *
import random
import time
import threading

class Star:
    def __init__(self, window, entry, qt_button, ep_button):
        self.star_list = []
        self.t = time.sleep
        self.window = window
        self.entry = entry
        self.qt_button = qt_button
        self.ep_button = ep_button
    
    def generate_star(self):
            if self.entry.get() != "":
                try:
                    self.ep_button.config(state=DISABLED)
                    self.log = Label(self.window, text="Generating stars...", bg="black", fg="blue")
                    self.log.place(x=10, y=40)
                    self.qt_button.config(state=DISABLED)
                    for i in range(0, int(self.entry.get())):
                        self.t(0.5)
                        pos_x = random.randrange(20,780)
                        pos_y = random.randrange(100,450)   
                        self.star_label = Label(self.window, text=f"*", bg="black", fg="white")
                        self.star_label.place(x=pos_x, y=pos_y)
                        self.star_list.append(self.star_label)
                    self.t(0.3)
                    self.log.destroy()   
                    self.log_message("All stars was created!", 2, "Green")
                    self.ep_button.config(state=NORMAL)
                    self.qt_button.config(state=NORMAL)
                except:
                    self.qt_button.config(state=DISABLED)
                    self.error_message("Must be int", 3, "red")
                    self.qt_button.config(state=NORMAL)
            else:
                self.qt_button.config(state=DISABLED)
                self.error_message("Insert a valid value (int)", 3, "red")
                self.qt_button.config(state=NORMAL)
            self.count_stars()

    def explode_stars(self):
        print("Explode")
        if self.star_list != []:
            try:
                self.qt_button.config(state=DISABLED)   
                self.log = Label(self.window, text="Exploding stars...", bg="black", fg="blue")
                self.ep_button.config(state=DISABLED)
                self.log.place(x=10, y=40)
                for i in self.star_list:
                    self.t(0.2)
                    i.destroy()
                self.t(0.3)
                self.log.destroy()   
                self.error_message("All stars was exploded", 2, "Green")
                self.qt_button.config(state=NORMAL)
                self.ep_button.config(state=NORMAL)
            except:
                pass
        else:
            self.ep_button.config(state=DISABLED)
            self.log_message("No have any stars", 2, "Red")
            self.ep_button.config(state=NORMAL)

    def count_stars(self):
        for i in self.star_list:
            print(f"Created stars: {i}")

    def log_message(self, text, time, color):
        self.error = Label(self.window, text=text, bg="black", fg=color)
        self.error.place(x=10, y=40)
        self.t(time)
        self.error.destroy()

    def error_message(self, text, time, color):
        self.error = Label(self.window, text=text, bg="black", fg=color)
        self.error.place(x=10, y=40)
        self.t(time)
        self.error.destroy()
    
    def run_generate(self):
        threading.Thread(target=self.generate_star).start()

    def run_explode(self):
        threading.Thread(target=self.explode_stars).start()

