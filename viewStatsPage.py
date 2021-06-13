#########
# Imports
#########
import json
import time
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
p1 = my_dict['player1']
p2 = my_dict['player2']
items = list(p0.items())
bottom = len(items) + 1
timeStr = time.strftime("%Y-%m-%d_%H%M")

lxVarList = []
activityList = []

# Player 1
p1JSON = list(p1.items())
p1WeekStats = p1JSON[2]
p1MonthStats = p1JSON[3]
p1TotalJSON = p1JSON[4]
p1statListWeekScores = p1WeekStats[1]
p1statListMonthScores = p1MonthStats[1]
p1Totals = p1TotalJSON[1]
p1TotalWeek = p1Totals['total week']

# Player 2
p2JSON = list(p2.items())
p2WeekStats = p2JSON[2]
p2MonthStats = p2JSON[3]
p2TotalJSON = p2JSON[4]
p2statListWeekScores = p2WeekStats[1]
p2statListMonthScores = p2MonthStats[1]
p2Totals = p2TotalJSON[1]
p2TotalWeek = p2Totals['total week']


def viewStats():
    viewS = tk.Tk()
    viewS.configure(bg="turquoise")
    viewS.geometry("545x700")
    viewS.title("Lvl^")

    addPGreeting = tk.Label(text="Current Stats:", bg="mediumturquoise", fg="black", font="10", width=60, pady=20)
    addPGreeting.grid(row=0, columnspan=6, sticky=EW)

    ####################
    # Columns
    ####################
    # Players
    p1PlayerOne = tk.Label(viewS, text=p1['name'], width=6)
    p1PlayerOne.grid(row=1, column=1, columnspan=2, sticky=EW)
    p2PlayerTwo = tk.Label(viewS, text=p2['name'], width=6)
    p2PlayerTwo.grid(row=1, column=3, columnspan=2, sticky=EW)

    # Player1
    p1Week = tk.Label(viewS, text="Week", width=6)
    p1Week.grid(row=2, column=1, sticky=EW)
    p1Month = tk.Label(viewS, text="Month", width=6)
    p1Month.grid(row=2, column=2, sticky=EW)

    # Player2
    p2Week = tk.Label(viewS, text="Week", width=6)
    p2Week.grid(row=2, column=3, sticky=EW)
    p2Month = tk.Label(viewS, text="Month", width=6)
    p2Month.grid(row=2, column=4, sticky=EW)

    #############################
    # Populates the Activity List
    #############################
    row = 3
    for category in p1statListWeekScores:
        labelEntry = tk.Label(viewS, text=category, width=14)
        labelEntry.grid(row=row, column=0, sticky=EW, pady=3, padx=18)
        row += 1

    def changeWindow():
        viewS.destroy()
        from main import mainPage
        mainPage()

    ################
    # Player 1 Stats
    ################

    # week
    row = 3
    for stat in p1statListWeekScores:
        point = str(p1statListWeekScores[stat])
        p1WeekPoints = tk.Label(viewS, text=point, width=6)
        p1WeekPoints.grid(row=row, column=1, sticky=EW)
        row += 1

    # month
    row = 3
    for stat in p1statListMonthScores:
        point = str(p1statListMonthScores[stat])
        p1WeekPoints = tk.Label(viewS, text=point, width=6)
        p1WeekPoints.grid(row=row, column=2, sticky=EW)
        row += 1

    ################
    # Player 2 Stats
    ################

    # week
    row = 3
    for stat in p2statListWeekScores:
        point = str(p2statListWeekScores[stat])
        p2WeekPoints = tk.Label(viewS, text=point, width=6)
        p2WeekPoints.grid(row=row, column=3, sticky=EW)
        row += 1

    # month
    row = 3
    for stat in p2statListMonthScores:
        point = str(p2statListMonthScores[stat])
        p2WeekPoints = tk.Label(viewS, text=point, width=6)
        p2WeekPoints.grid(row=row, column=4, sticky=EW)
        row += 1

    ############
    # Clear Week
    ############
    def cWeek():
        row = 3
        for stat in p1statListWeekScores:
            p1statListWeekScores[stat] = 0
            p1WeekPoints = tk.Label(viewS, text=p1statListWeekScores[stat], width=6)
            p1WeekPoints.grid(row=row, column=1, sticky=EW)
            row += 1

        p1Totals['total week'] = 0

        row = 3
        for stat in p2statListWeekScores:
            p2statListWeekScores[stat] = 0
            p2WeekPoints = tk.Label(viewS, text=p2statListWeekScores[stat], width=6)
            p2WeekPoints.grid(row=row, column=3, sticky=EW)
            row += 1

        p2Totals['total week'] = 0

        a_file = open("stats.json", "w")
        json.dump(my_dict, a_file)
        a_file.close()

        archive = open("stats" + timeStr + ".json", "w")
        json.dump(my_dict, archive)
        archive.close()

    #############
    # Clear Month
    #############
    def cMonth():
        row = 3
        for stat in p1statListMonthScores:
            p1statListMonthScores[stat] = 0
            p1MonthPoints = tk.Label(viewS, text=p1statListMonthScores[stat], width=6)
            p1MonthPoints.grid(row=row, column=2, sticky=EW)
            row += 1

        p1Totals['total month'] = 0

        row = 3
        for stat in p2statListMonthScores:
            p2statListMonthScores[stat] = 0
            p2MonthPoints = tk.Label(viewS, text=p2statListMonthScores[stat], width=6)
            p2MonthPoints.grid(row=row, column=4, sticky=EW)
            row += 1

        p2Totals['total month'] = 0

        a_file = open("stats.json", "w")
        json.dump(my_dict, a_file)
        a_file.close()

        archive = open("stats" + timeStr + ".json", "w")
        json.dump(my_dict, archive)
        archive.close()

    ##########################
    # Go Back and Quit Buttons
    ##########################
    em1 = tk.Label(viewS, text="", width=40, bg="turquoise")
    em1.grid(row=bottom + 1, columnspan=5, sticky=EW, pady=3, padx=18)
    clearWeek = Button(viewS, text="Clear Week", command=cWeek, width=12)
    clearWeek.grid(row=bottom + 2, column=1, columnspan=2, sticky=EW, padx=6)
    clearMonth = Button(viewS, text="Clear Month", command=cMonth, width=12)
    clearMonth.grid(row=bottom + 2, column=3, columnspan=2, sticky=EW, padx=6)
    em2 = tk.Label(viewS, text="", width=40, bg="turquoise")
    em2.grid(row=bottom + 3, columnspan=5, sticky=EW, pady=3, padx=18)
    goBack = Button(viewS, text="Go back", command=lambda *args: changeWindow(), width=30)
    goBack.grid(row=bottom + 4, column=1, columnspan=4, sticky=EW, padx=10)
    quitG = Button(viewS, text="Quit", command=viewS.destroy, width=30)
    quitG.grid(row=bottom + 5, column=1, columnspan=4, sticky=EW, padx=10)

    viewS.mainloop()
