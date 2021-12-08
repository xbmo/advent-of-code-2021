#https://adventofcode.com/2021/day/7

import math

#filename = "day7_test_data.txt"
filename = "day7_data.txt"
fileData = open(filename, "r")

positionList = []

line = fileData.readline()
splitLine = line.split(",")
total = 0
for i in range(len(splitLine)):
    position = int(splitLine[i])
    positionList.append(position)
    total += position

numberOfPositions = len(positionList)
mean = math.floor(total / numberOfPositions)

print("Mean is " + str(mean))

fuelUsed = 0

for i in range(numberOfPositions):
    distance = abs(positionList[i] - mean)
    for move in range(distance + 1):
        fuelUsed += move

print("Total fuel used = " + str(fuelUsed))


