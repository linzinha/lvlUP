#########
# Imports
#########
import json
import tkinter as tk
from tkinter import *

################
# Open JSON File
# ##############
with open('stats.json', 'r') as string:
    my_dict = json.load(string)
string.close()

####################
# Global Variables
####################
p0 = my_dict['points']
items = list(p0.items())


def editGame():
    editG = tk.Tk()
    editG.configure(bg="turquoise")
    editG.geometry("450x600")
    editG.title("Lvl^: Edit Game")

    editGGreeting = tk.Label(text="Edit Game:", bg="mediumturquoise", fg="black", font="10", width=50, pady=20)
    editGGreeting.grid(row=0, columnspan=2, sticky=EW)

    listbox = Listbox(height=15, width=40, bg="cornsilk", activestyle='dotbox', font="10", fg="black")
    n = 0
    for item in items:
        n += 1
        key = str(item[0])
        value = str(item[1])
        listbox.insert(n, str(n) + ":) " + key + ": " + value)
        listbox.grid(row=1, columnspan=6, pady=4, padx=20)

    def changeWindow():
        editG.destroy()
        from main import mainPage
        mainPage()

    ################
    # Go Back and Quit Buttons
    ################
    goBack = Button(editG, text="Go back", command=lambda *args: changeWindow(), width=40)
    goBack.grid(row=10 + 1, columnspan=4, sticky=EW, padx=18)
    quitG = Button(editG, text="Quit", command=editG.destroy, width=40)
    quitG.grid(row=11 + 1, columnspan=4, sticky=EW, padx=18)

    editG.mainloop()
