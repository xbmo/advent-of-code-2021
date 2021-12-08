#https://adventofcode.com/2021/day/5

from parser import parse
from line import Line

#filename = "day5_test_data.txt"
filename = "day5_data.txt"

parsedData = parse(filename)

positionCountDict = {}

for line in parsedData:
    if line.isHorizontal():
        direction = line.getXDirection()
        for x in range(line.x1, line.x2 + direction, direction):
            positionTuple = (x, line.y1)
            positionCountDict[positionTuple] = positionCountDict.get(positionTuple, 0) + 1
    elif line.isVertical():
        direction = line.getYDirection()
        for y in range(line.y1, line.y2 + direction, direction):
            positionTuple = (line.x1, y)
            positionCountDict[positionTuple] = positionCountDict.get(positionTuple, 0) + 1

#print(positionCountDict)

overlappingPositionsCount = 0

for key in positionCountDict:
    if positionCountDict[key] > 1:
        overlappingPositionsCount += 1

print("Overlapping positions count = " + str(overlappingPositionsCount))

