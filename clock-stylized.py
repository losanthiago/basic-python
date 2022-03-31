# Digital Clock Stylized by Thiago
# Performing

from tkinter import *
import tkinter as tk

import datetime


class HomeScreen:
    def __init__(self, master=None):
        self.ourScreen = master
        self.lblClock = tk.Label(
            self.ourScreen, font=('Lucida Sans', '15'), fg='Black')
        self.lblClock.pack(pady=30, padx=30)
        self.change()
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.exit = Button(self.widget1)
        self.exit["text"] = "EXIT"
        self.exit["font"] = ('Lucida Sans', 10)
        self.exit["width"] = 5
        self.exit["command"] = self.widget1.quit
        self.exit.pack()

    def change(self):
        now = datetime.datetime.now()
        self.lblClock['text'] = now.strftime('%H:%M:%S')
        self.ourScreen.after(1000, self.change)


rootWindow = tk.Tk()
HomeScreen(rootWindow)
rootWindow.mainloop()
