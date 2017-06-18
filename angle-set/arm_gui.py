#!/bin/env python3

from  arm import arm
import tkinter as tk

class Appication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "FUck you\n(Come on)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="FUCK",fg = "red",command=root.destroy)
        self.quit.pack(side="bottom")

        self.jiba = tk.Entry(self)
        self.jiba.pack()
    def say_hi(self):
        print("fuck!")


root = tk.Tk()
root.title="Jiba"
app = Appication(master=root)
app.mainloop()
