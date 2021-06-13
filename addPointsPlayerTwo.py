#########
# Imports
#########
import json
import tkinter as tk
from tkinter import *
import math

# Open JSON File
with open('stats.json', 'r') as string:
    my_dict = json.load(string)
string.close()

##################
# global variables
##################
p0 = my_dict['points']
p2 = my_dict['player2']
items = list(p0.items())
back = len(items) + 1
p2JSON = list(p2.items())
p2WeekStats = p2JSON[2]
p2MonthStats = p2JSON[3]
p2TotalJSON = p2JSON[4]
p2statListWeekScores = p2WeekStats[1]
p2statListMonthScores = p2MonthStats[1]
p2Totals = p2TotalJSON[1]
lxVarList = []
activityList = []
caloriePointsTotal = 0
stepPointsTotal = 0
exercisePointsTotal = 0
meditationPointsTotal = 0
readingPointsTotal = 0
studyingPointsTotal = 0
teethPointsTotal = 0
facePointsTotal = 0
showerPointsTotal = 0
cleaningPointsTotal = 0
dishesPointsTotal = 0
cookingPointsTotal = 0
errandsPointsTotal = 0


def addPointsP2():
    ##############################
    # styling and page information
    ##############################
    root = tk.Tk()
    root.configure(bg="turquoise")
    root.geometry("450x700")
    # Title
    root.title("Lvl^: Calculate")

    addPGreeting = tk.Label(text="Add Points for Player Two:", bg="mediumturquoise", fg="black", font="10", width=50, pady=20)
    addPGreeting.grid(row=0, columnspan=4, sticky=EW)

    def changeWindow():
        root.destroy()
        from addPointsPage import addPoints
        addPoints()

    #####################################
    # Calculating individual point values
    #####################################
    def addNumbers():
        global caloriePointsTotal
        global stepPointsTotal
        global exercisePointsTotal
        global meditationPointsTotal
        global readingPointsTotal
        global studyingPointsTotal
        global teethPointsTotal
        global facePointsTotal
        global showerPointsTotal
        global cleaningPointsTotal
        global dishesPointsTotal
        global cookingPointsTotal
        global errandsPointsTotal
        # Calories eaten vs burned points
        try:
            subtractCalorieValues = int(e2.get()) - int(e1.get())
            calSub.set(subtractCalorieValues)
            if subtractCalorieValues > 450:
                calPoints.set(5)
                caloriePointsTotal = 5
            elif subtractCalorieValues > 100:
                calPoints.set(1)
                caloriePointsTotal = 1
            else:
                calPoints.set(0)
        except ValueError:
            calPoints.set(0)
            calSub.set(0)
        # Points from steps counted e4
        try:
            step = math.floor(int(e4.get()) * .001)
            stepPoints.set(step)
            stepPointsTotal = step
        except ValueError:
            stepPoints.set(0)
        # exercise Points e5
        try:
            subtractBMR = int(e2.get()) - 1946
            exSub.set(subtractBMR)
            exercises = math.floor((int(e2.get()) - 1946) * .02)
            exercisePoints.set(exercises)
            exercisePointsTotal = exercises
        except ValueError:
            exercisePoints.set(0)
            # meditation points e6
            meditationPoints.set(mVar.get())
            if mVar.get() == "3":
                meditationPointsTotal = 3
            else:
                meditationPointsTotal = 0
        # Points from reading e7
        try:
            read = math.floor((int(e7.get()) / 30) * 2)
            if read % 2 == 1:
                read -= 1
            readPoints.set(read)
            readingPointsTotal = read
        except ValueError:
            readPoints.set(0)
        # Points from Studying e8
        try:
            study = math.floor((int(e8.get()) / 30) * 3)
            if study % 3 == 1:
                study -= 1
            elif study % 3 == 2:
                study -= 2
            studyPoints.set(study)
            studyingPointsTotal = study
        except ValueError:
            studyPoints.set(0)
        # oral hygiene points e9
        if tVar.get() == "3 of 3":
            teethPoints.set(3)
            teethPointsTotal = 3
        elif tVar.get() == "2 of 3":
            teethPoints.set(2)
            teethPointsTotal = 2
        elif tVar.get() == "1 of 3":
            teethPoints.set(1)
            teethPointsTotal = 1
        else:
            teethPoints.set(0)
        # skincare points e10
        if fVar.get() == "3 of 3":
            facePoints.set(3)
            facePointsTotal = 3
        elif fVar.get() == "2 of 3":
            facePoints.set(2)
            facePointsTotal = 2
        elif fVar.get() == "1 of 3":
            facePoints.set(1)
            facePointsTotal = 1
        else:
            facePoints.set(0)
        # shower points e11
        showerPoints.set(sVar.get())
        if sVar.get() == "3":
            showerPointsTotal = 3
        else:
            showerPointsTotal = 0
        # Points earned cleaning e12
        try:
            cleanPts = math.floor((int(e12.get()) / 30) * 3)
            if cleanPts % 3 == 1:
                cleanPts -= 1
            elif cleanPts % 3 == 2:
                cleanPts -= 2
            cleanPoints.set(cleanPts)
            cleaningPointsTotal = cleanPts
        except ValueError:
            cleanPoints.set(0)
        # Dishes bonus e13
        dishPoints.set(dishVar.get())
        if dishVar.get() == "1":
            dishesPointsTotal = 1
        else:
            dishesPointsTotal = 0
        # Points earned cooking e14
        try:
            cookPts = math.floor((int(e14.get()) / 30) * 3)
            if cookPts % 3 == 1:
                cookPts -= 1
            elif cookPts % 3 == 2:
                cookPts -= 2
            cookPoints.set(cookPts)
            cookingPointsTotal = cookPts
        except ValueError:
            cookPoints.set(0)
        # Points for running errands e15
        if eVar.get() == "big":
            errandPoints.set(10)
            errandsPointsTotal = 10
        elif eVar.get() == "medium":
            errandPoints.set(5)
            errandsPointsTotal = 5
        elif eVar.get() == "small":
            errandPoints.set(3)
            errandsPointsTotal = 3
        else:
            errandPoints.set(0)

    #############################
    # Populates the Activity List
    #############################
    row = 0
    for item in items:
        row += 1
        key = str(item[0])
        labelEntry = tk.Label(root, text=key, width=15)
        labelEntry.grid(row=row, columnspan=2, sticky=W, pady=3, padx=18)
        labelText = labelEntry.cget("text")
        lxVarList.append(labelEntry)
        activityList.append(labelText)

    #################
    # Calories In/Out
    #################
    calPoints = StringVar()
    calSub = StringVar()
    calResult1 = Label(root, text="", textvariable=calSub, width=11, bg="papayawhip")
    calResult2 = Label(root, text="", textvariable=calPoints, width=8, bg="papayawhip")
    calResult1.grid(row=3, column=2, sticky=EW)
    calResult2.grid(row=3, column=3, padx=20, sticky=EW)
    e1 = Entry(root, width=10)
    e2 = Entry(root, width=10)
    e1.grid(row=1, column=2, pady=3, sticky=EW)
    e2.grid(row=2, column=2, pady=3, sticky=EW)

    #######
    # Steps
    #######
    stepPoints = StringVar()
    steps = Label(root, text="", textvariable=stepPoints, width=8, bg="papayawhip")
    steps.grid(row=4, column=3, padx=20, sticky=EW)
    e4 = Entry(root, width=10)
    e4.grid(row=4, column=2, pady=3, sticky=EW)

    ##########
    # Exercise
    ##########
    exercisePoints = StringVar()
    exSub = StringVar()
    exerciseResult = Label(root, text="", textvariable=exSub, width=11, bg="papayawhip")
    exerciseResult.grid(row=5, column=2, sticky=EW)
    exercise = Label(root, text="", textvariable=exercisePoints, width=8, bg="papayawhip")
    exercise.grid(row=5, column=3, padx=20, sticky=EW)

    ############
    # Meditation
    ############
    meditationPoints = StringVar(root)
    meditation = Label(root, text="", textvariable=meditationPoints, width=8, bg="papayawhip")
    meditation.grid(row=6, column=3, padx=20, sticky=EW)
    mVar = StringVar(root)
    mVar.set("---")  # default value
    e6 = Checkbutton(root, variable=mVar, onvalue=3, offvalue=0, bg="mediumslateblue")  # shower
    e6.grid(row=6, column=2, pady=3, sticky=EW)

    #########
    # Reading
    #########
    readPoints = StringVar()
    reading = Label(root, text="", textvariable=readPoints, width=8, bg="papayawhip")
    reading.grid(row=7, column=3, padx=20, sticky=EW)
    e7 = Entry(root, width=10)
    e7.grid(row=7, column=2, pady=3, sticky=EW)

    ##########
    # Studying
    ##########
    studyPoints = StringVar()
    studying = Label(root, text="", textvariable=studyPoints, width=8, bg="papayawhip")
    studying.grid(row=8, column=3, padx=20, sticky=EW)
    e8 = Entry(root, width=10)
    e8.grid(row=8, column=2, pady=3, sticky=EW)

    #######
    # Teeth
    #######
    teethPoints = StringVar()
    teeth = Label(root, text="", textvariable=teethPoints, width=8, bg="papayawhip")
    teeth.grid(row=9, column=3, padx=20, sticky=EW)
    tVar = StringVar(root)
    tVar.set("---")  # default value
    e9 = OptionMenu(root, tVar, "---", "3 of 3", "2 of 3", "1 of 3")
    e9.grid(row=9, column=2, pady=3, sticky=EW)

    ######
    # Face
    ######
    facePoints = StringVar()
    face = Label(root, text="", textvariable=facePoints, width=8, bg="papayawhip")
    face.grid(row=10, column=3, padx=20, sticky=EW)
    fVar = StringVar(root)
    fVar.set("---")  # default value
    e10 = OptionMenu(root, fVar, "---", "3 of 3", "2 of 3", "1 of 3")
    e10.grid(row=10, column=2, pady=3, sticky=EW)

    ########
    # Shower
    ########
    showerPoints = StringVar()
    shower = Label(root, text="", textvariable=showerPoints, width=8, bg="papayawhip")
    shower.grid(row=11, column=3, padx=20, sticky=EW)
    sVar = StringVar(root)
    sVar.set("---")  # default value
    e11 = Checkbutton(root, variable=sVar, onvalue=3, offvalue=0, bg="mediumslateblue")  # shower
    e11.grid(row=11, column=2, pady=3, sticky=EW)

    #######
    # Clean
    #######
    cleanPoints = StringVar()
    clean = Label(root, text="", textvariable=cleanPoints, width=8, bg="papayawhip")
    clean.grid(row=12, column=3, padx=20, sticky=EW)
    e12 = Entry(root, width=10)
    e12.grid(row=12, column=2, pady=3, sticky=EW)

    ########
    # Dishes
    ########
    dishPoints = StringVar()
    dishes = Label(root, text="", textvariable=dishPoints, width=8, bg="papayawhip")
    dishes.grid(row=13, column=3, padx=20, sticky=EW)
    dishVar = StringVar(root)
    dishVar.set("---")
    e13 = Checkbutton(root, variable=dishVar, onvalue=1, offvalue=0, bg="mediumslateblue")  # dishes
    e13.grid(row=13, column=2, pady=3, sticky=EW)

    ######
    # Cook
    ######
    cookPoints = StringVar()
    cook = Label(root, text="", textvariable=cookPoints, width=8, bg="papayawhip")
    cook.grid(row=14, column=3, padx=20, sticky=EW)
    e14 = Entry(root, width=10)
    e14.grid(row=14, column=2, pady=3, sticky=EW)

    #########
    # Errands
    #########
    errandPoints = StringVar()
    errands = Label(root, text="", textvariable=errandPoints, width=8, bg="papayawhip")
    errands.grid(row=15, column=3, padx=20, sticky=EW)
    eVar = StringVar(root)
    eVar.set("---")  # default value
    e15 = OptionMenu(root, eVar, "---", "none", "small", "medium", "big")
    e15.grid(row=15, column=2, pady=3, sticky=EW)

    ##################
    # Calculate Button
    ##################
    b = Button(root, text="Calculate", command=addNumbers)
    b.grid(row=1, column=3, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=25, pady=5)

    ###################
    # Totaling the data
    ###################
    def finalTally():
        physicalHealthPoints = caloriePointsTotal + stepPointsTotal + exercisePointsTotal
        mentalHealthAndGrowth = meditationPointsTotal + readingPointsTotal + studyingPointsTotal
        bodyCareTotal = teethPointsTotal + facePointsTotal + showerPointsTotal
        householdTotal = cleaningPointsTotal + dishesPointsTotal + cookingPointsTotal + errandsPointsTotal
        totalPointsEarned = physicalHealthPoints + mentalHealthAndGrowth + bodyCareTotal + householdTotal
        totalPoints.set(totalPointsEarned)

        dailyTally = [caloriePointsTotal, stepPointsTotal, exercisePointsTotal, meditationPointsTotal,
                      readingPointsTotal, studyingPointsTotal, teethPointsTotal, facePointsTotal, showerPointsTotal,
                      cleaningPointsTotal, dishesPointsTotal, cookingPointsTotal, errandsPointsTotal]

        pKeys = p2statListWeekScores.keys()
        pointCategories = []

        for pKey in pKeys:
            pointCategories.append(pKey)

        i = 0
        for cat in pointCategories:
            p2statListWeekScores[cat] += dailyTally[i]
            p2statListMonthScores[cat] += dailyTally[i]

            i += 1

        p2Totals['total week'] += totalPointsEarned
        p2Totals['total month'] += totalPointsEarned

        a_file = open("stats.json", "w")
        json.dump(my_dict, a_file)
        a_file.close()

    totalPoints = StringVar()
    total = Label(root, text="", textvariable=totalPoints, width=8, bg="papayawhip")
    total.grid(row=16, column=3, padx=20, pady=24, sticky=W)
    tPoints = tk.Button(root, text="Total Points", command=finalTally, width=15)
    tPoints.grid(row=back, columnspan=2, sticky=W, pady=12, padx=18)

    ################
    # Go Back Button
    ################
    goBack = Button(root, text="Go back", command=lambda *args: changeWindow(), width=40)
    goBack.grid(row=back + 1, columnspan=4, sticky=EW, padx=18)
    quitG = Button(root, text="Quit", command=root.destroy, width=40)
    quitG.grid(row=back + 2, columnspan=4, sticky=EW, padx=18)

    root.mainloop()
