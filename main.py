#########
# Imports
#########
import json
import tkinter as tk
from tkinter import *
from addPointsPage import addPoints
from editGamePage import editGame
from viewStatsPage import viewStats

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
p1 = my_dict['player1']
p2 = my_dict['player2']
keys = p0.keys()
values = p0.values()
items = list(p0.items())
back = len(items)
button_identities = []

# Player 1
p1JSON = list(p1.items())
p1WeekStats = p1JSON[2]
p1MonthStats = p1JSON[3]
p1TotalJSON = p1JSON[4]
p1statListWeekScores = p1WeekStats[1]
p1statListMonthScores = p1MonthStats[1]
p1Totals = p1TotalJSON[1]


# Player 2
p2JSON = list(p2.items())
p2WeekStats = p2JSON[2]
p2MonthStats = p2JSON[3]
p2TotalJSON = p2JSON[4]
p2statListWeekScores = p2WeekStats[1]
p2statListMonthScores = p2MonthStats[1]
p2Totals = p2TotalJSON[1]


###########
# Main Page
###########
def mainPage():
    root = tk.Tk()
    root.configure(bg="turquoise")
    root.geometry("450x600")
    root.title("Lvl^")

    col_count, row_count = root.grid_size()
    for col in range(col_count):
        root.grid_columnconfigure(col, minsize=20)
    for row in range(row_count):
        root.grid_rowconfigure(row, minsize=20)

    welcomePlayers = tk.Label(text="Welcome Players", bg="mediumturquoise", fg="black", font="10", width=50, pady=20)
    welcomePlayers.grid(row=0, columnspan=2, sticky=EW)

    ####################
    # Current Game Stats
    ####################
    # This week's score
    weekScore = tk.Label(root, text="This week's scores:", bg="turquoise", width=45, pady=10)
    weekScore.grid(row=1, columnspan=2, sticky=EW)
    # Player 1
    p1WeekPlayer = tk.Label(root, text=p1['name'] + ": ", width=22)
    p1WeekPlayer.grid(row=2, column=0)
    p1WeekScore = tk.Label(root, text=str(p1Totals['total week']), width=22)
    p1WeekScore.grid(row=2, column=1)
    # Player 2
    p2WeekPlayer = tk.Label(root, text=p2['name'] + ": ", width=22)
    p2WeekPlayer.grid(row=3, column=0)
    p2WeekScore = tk.Label(root, text=str(p2Totals['total week']), width=22)
    p2WeekScore.grid(row=3, column=1)

    # This month's score
    monthScore = tk.Label(root, text="This month's scores:", bg="turquoise", width=45, pady=10)
    monthScore.grid(row=4, column=0, columnspan=2, sticky=EW)
    # Player 1
    p1MonthPlayer = tk.Label(root, text=p1['name'] + ": ", width=22)
    p1MonthPlayer.grid(row=5, column=0)
    p1MonthScore = tk.Label(root, text=str(p1Totals['total month']), width=22)
    p1MonthScore.grid(row=5, column=1)
    # Player 2
    p2MonthPlayer = tk.Label(root, text=p2['name'] + ": ", width=22)
    p2MonthPlayer.grid(row=6, column=0)
    p2MonthScore = tk.Label(root, text=str(p2Totals['total month']), width=22)
    p2MonthScore.grid(row=6, column=1)

    ########################
    # Change Window Function
    ########################

    def changeWindow(page):
        root.destroy()
        page()

    #########
    # Buttons
    #########

    ###########################
    # Add the points of the day
    ###########################
    addPointsLabel = tk.Label(root, text="", bg="turquoise", width=45, pady=10)
    addPointsLabel.grid(row=7, column=0, columnspan=2, sticky=EW)
    addPointsButton = Button(root, text="Add Points", command=lambda *args: changeWindow(addPoints), width=40,
                             height="2")
    addPointsButton.grid(row=8, column=0, columnspan=2)

    ###################
    # Edit game details
    ###################
    editGameLabel = tk.Label(root, text="", bg="turquoise", width=45, pady=1)
    editGameLabel.grid(row=9, column=0, columnspan=2, sticky=EW)
    editGameButton = Button(root, text="Edit Game", command=lambda *args: changeWindow(editGame), width=40,
                            height="2")
    editGameButton.grid(row=10, column=0, columnspan=2)

    ######################
    # View game statistics
    ######################
    gameStatsLabel = tk.Label(root, text="", bg="turquoise", width=45, pady=1)
    gameStatsLabel.grid(row=11, column=0, columnspan=2, sticky=EW)
    gameStatsButton = Button(root, text="View Stats", command=lambda *args: changeWindow(viewStats), width=40,
                             height="2")
    gameStatsButton.grid(row=12, column=0, columnspan=2)

    ##############
    # Close Window
    ##############
    gameStatsLabel = tk.Label(root, text="", bg="turquoise", width=45, pady=1)
    gameStatsLabel.grid(row=13, column=0, columnspan=2, sticky=EW)
    gameStatsButton = Button(root, text="Quit", command=root.destroy, width=40, height="2")
    gameStatsButton.grid(row=14, column=0, columnspan=2)

    root.mainloop()


mainPage()
