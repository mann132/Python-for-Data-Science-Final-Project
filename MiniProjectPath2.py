import pandas
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
import math
from sklearn.model_selection import train_test_split
''' 
The following is the starting code for path2 for data reading to make your first step easier.
'dataset_2' is the clean data for path1.
'''
dataset_2 = pandas.read_csv('NYC_Bicycle_Counts_2016.csv')
dataset_2['Brooklyn Bridge']      = pandas.to_numeric(dataset_2['Brooklyn Bridge'].replace(',','', regex=True))
dataset_2['Manhattan Bridge']     = pandas.to_numeric(dataset_2['Manhattan Bridge'].replace(',','', regex=True))
dataset_2['Queensboro Bridge']    = pandas.to_numeric(dataset_2['Queensboro Bridge'].replace(',','', regex=True))
dataset_2['Williamsburg Bridge']  = pandas.to_numeric(dataset_2['Williamsburg Bridge'].replace(',','', regex=True))
dataset_2['Williamsburg Bridge']  = pandas.to_numeric(dataset_2['Williamsburg Bridge'].replace(',','', regex=True))

print(dataset_2.to_string()) #This line will print out your data
dataMatrix = pandas.DataFrame.to_numpy(dataset_2) #converts data to np array
averageBikers = []
dayTotal = []
for i in range(len(dataMatrix)):
    temp = (dataMatrix[i][-1]).replace(",", "")
    temp = int(temp)
    dayTotal.append(temp)
    averageBikers.append(temp / 5)
#this outputs an array of the average number of bikers on a bridge for one day
#print(averageBikers)
def part1(dataMatrix, averageBikers):
    countB = 0
    countM = 0
    countW = 0
    countQ = 0
    for i in range(len(dataMatrix)):
        brooklyn = dataMatrix[i][-5]
        manhattan = dataMatrix[i][-4]
        williamsburg = dataMatrix[i][-3]
        queensboro = dataMatrix[i][-2]
        avg = averageBikers[i]
        diffB = abs(brooklyn - avg)
        diffM = abs(manhattan - avg)
        diffW = abs(williamsburg - avg)
        diffQ = abs(queensboro - avg)
        out = min(diffB, diffM, diffW, diffQ)
        if out == diffB:
            countB += 1
        elif out == diffM:
            countM += 1
        elif out == diffW:
            countW += 1
        else:
            countQ += 1
    print("Brooklyn Bridge", countB)
    print("Manhattan Bridge", countM)
    print("Williamsburg Bridge", countW)
    print("Queensboro Bridge", countQ)

    print("the three bridges we will install sensors on are Queensboro, Brooklyn, and Manhattan.  \nUsing this analysis we can tell that Queensboro is the best refleciton of the average number of people on every bridge per day.  \nThe second closest is Brooklyn followed by Manhattan.")

def part2(dataMatrix, dayTotal, dataset_2):
    highTemp = []
    lowTemp = []
    rain = []

    for i in range(len(dayTotal)):
        highTemp.append(dataMatrix[i][2])
        lowTemp.append(dataMatrix[i][3])
        rain.append(dataMatrix[i][4])


    x = dataset_2[['High Temp', 'Low Temp', 'Precipitation']]
    y = dayTotal
    model = linear_model.LinearRegression()
    model.fit(x, y)
    cf = model.coef_
    ic = model.intercept_
    print(cf)
    print(ic)

    cf1 = float(cf[0])
    cf2 = float(cf[1])
    cf3 = float(cf[2])
    modelGuess = []
    for i in range(len(dayTotal)):
        temp = cf1 * highTemp[i] + cf2 * lowTemp[i] + cf3 * rain[i] + ic
        modelGuess.append(temp)
    mse = math.sqrt(mean_squared_error(dayTotal, modelGuess))
    print("error:", mse)

def part3(dataMatrix, dayTotal):
    weekday = []
    for i in range(len(dataMatrix)):
        temp = dataMatrix[i][1]
        weekday.append(temp)

    dict = {'Sunday': 1, 'Monday': 2, 'Tuesday': 3, 'Wednesday': 4, 'Thursday': 5, 'Friday': 6, 'Saturday': 7}
    weekdayNumbers = [dict[x] for x in weekday]

    sunday = 0; monday = 0; tuesday = 0; wednesday = 0; thursday = 0; friday = 0; saturday = 0
    sundayCount = 0; mondayCount = 0; tuesdayCount = 0; wednesdayCount = 0; thursdayCount = 0; fridayCount = 0; saturdayCount = 0

    for i in range(len(weekdayNumbers)):
        if weekdayNumbers[i] == 1:
            sunday += dayTotal[i]
            sundayCount += 1
        if weekdayNumbers[i] == 2:
            monday = monday + dayTotal[i]
            mondayCount = mondayCount + 1
        if weekdayNumbers[i] == 3:
            tuesday = tuesday + dayTotal[i]
            tuesdayCount = tuesdayCount + 1
        if weekdayNumbers[i] == 4:
            wednesday = wednesday + dayTotal[i]
            wednesdayCount = wednesdayCount + 1
        if weekdayNumbers[i] == 5:
            thursday = thursday + dayTotal[i]
            thursdayCount = thursdayCount + 1
        if weekdayNumbers[i] == 6:
            friday = friday + dayTotal[i]
            fridayCount = fridayCount + 1
        if weekdayNumbers[i] == 7:
            saturday = saturday + dayTotal[i]
            saturdayCount = saturdayCount + 1

    sundayAvg = sunday / sundayCount
    mondayAvg = monday / mondayCount
    tuesdayAvg = tuesday / tuesdayCount
    wednesdayAvg = wednesday / wednesdayCount
    thursdayAvg = thursday / thursdayCount
    fridayAvg = friday / fridayCount
    saturdayAvg = saturday / saturdayCount

    list = [sundayAvg, mondayAvg, tuesdayAvg, wednesdayAvg, thursdayAvg, fridayAvg, saturdayAvg]
    averages = {'Sunday': sundayAvg, 'Monday': mondayAvg, 'Tuesday': tuesdayAvg, 'Wednesday': wednesdayAvg,
                'Thursday': thursdayAvg, 'Friday': fridayAvg, 'Saturday': saturdayAvg}
    #check = int(input("How many riders were on the bridge today?"))
    #test = min(list, key=lambda x: abs(x - check))
    count = 0
    weekdayCheck = 0
    for i in range(len(dayTotal)):
        check = dayTotal[i]
        test = min(list, key=lambda x: abs(x - check))
        output = [y for y in averages if averages[y] == test]
        print(str(output[0]))
        print(str(weekday[i]))
        if str(output[0]) == str(weekday[i]):
            count = count + 1
        if str(output[0]) != 'Saturday' or 'Sunday':
            if str(weekday[i]) != 'Saturday' or 'Sunday':
                weekdayCheck = weekdayCheck + 1
    accuracyCheck = float(count / len(dayTotal))
    weekdayCheck = weekdayCheck / len(dayTotal) * (5 / 7)
    print("Using data from the average number of bike riders per day, the model is", (accuracyCheck * 100), "% accurate in predicting the day of the week"
            "based on the number of riders that day")
    print("The model is", (weekdayCheck * 100), "% accurate in predicting whether the day is a weekend or a weekday")

print("Hello! Welcome to my ECE 20875 mini project (path 2: bike traffic)")
x = input("which analysis question would like me to answer?")
if x == '1':
    part1(dataMatrix, averageBikers)
if x == '2':
    part2(dataMatrix, dayTotal, dataset_2)
if x == '3':
    part3(dataMatrix, dayTotal)




