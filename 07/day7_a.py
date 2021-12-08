#https://adventofcode.com/2021/day/7

import math

#filename = "day7_test_data.txt"
filename = "day7_data.txt"
fileData = open(filename, "r")

positionList = []

line = fileData.readline()
splitLine = line.split(",")
for i in range(len(splitLine)):
    positionList.append(int(splitLine[i]))

positionList.sort()

numberOfPositions = len(positionList)
middleIndex = math.ceil(numberOfPositions / 2)
median = positionList[middleIndex]
if numberOfPositions % 2 == 0:
    otherMiddleIndex = middleIndex - 1
    median += positionList[otherMiddleIndex]
    median /= 2

print("Median is " + str(median))

fuelUsed = 0

for i in range(numberOfPositions):
    distance = abs(positionList[i] - median)
    fuelUsed += distance

print("Total fuel used = " + str(fuelUsed))


