#########
# Imports
#########
import tkinter as tk
from tkinter import *
from addPointsPlayerOne import addPointsP1
from addPointsPlayerTwo import addPointsP2


def addPoints():
    # Create the master object
    root = tk.Tk()
    root.configure(bg="turquoise")
    root.geometry("450x600")
    root.title("Lvl^")
    col_count, row_count = root.grid_size()
    for col in range(col_count):
        root.grid_columnconfigure(col, minsize=20)
    for row in range(row_count):
        root.grid_rowconfigure(row, minsize=20)

    addPointsLabel = tk.Label(text="Add points:", bg="mediumturquoise", fg="black", font="10", width=50, pady=20)
    addPointsLabel.grid(row=0, columnspan=2, sticky=EW)

    ########################
    # Change Window Function
    ########################

    def changeWindow(page):
        if page == "main":
            root.destroy()
            from main import mainPage
            mainPage()
        else:
            root.destroy()
            page()

    #########
    # Buttons
    #########
    addP1Button = Button(root, text="Lindsey", command=lambda *args: changeWindow(addPointsP1), width="40", height="3")
    addP1Button.grid(row=1, columnspan=6, pady=4, padx=20)
    addP2Button = Button(root, text="Pedro", command=lambda *args: changeWindow(addPointsP2), width="40", height="3")
    addP2Button.grid(row=2, columnspan=6, pady=4, padx=20)
    goBackButton = Button(root, text="Go back", command=lambda *args: changeWindow("main"), width="40", height="3")
    goBackButton.grid(row=3, columnspan=6, pady=4, padx=20)
    quitButton = Button(root, text="Quit", command=root.destroy, width="40", height="3")
    quitButton.grid(row=4, columnspan=6, pady=4, padx=20)

    root.mainloop()
