#https://adventofcode.com/2021/day/13

#filename = "day13_test_data.txt"
filename = "day13_data.txt"
fileData = open(filename, "r")

positionsList = []
foldsList = []
numRows = 0

readingGrid = True

while True:
    line = fileData.readline()
    if line:
        line = line.removesuffix("\n")
        if line == "":
            readingGrid = False
        elif readingGrid:
            rowList = []
            numRows += 1

            positionSplit = line.split(",")
            x = int(positionSplit[0])
            y = int(positionSplit[1])

            positionsList.append((x, y))
        else:
            foldSplit = line.split("=")
            #get the x or y instruction from the last character of the first part of the split string
            foldXorY = foldSplit[0][len(foldSplit[0]) - 1]
            foldPosition = int(foldSplit[1])
            foldsList.append((foldXorY, foldPosition))
    else:
        break

#print(positionsList)
#print("folds")
#print(foldsList)

def performHorizontalFold(position):
    toFlipList = []
    for i in range(len(positionsList) - 1, -1, -1):
        if positionsList[i][0] > position:
            toFlipList.append(positionsList[i])
            positionsList.pop(i)
        elif positionsList[i][0] == position:
            positionsList.pop(i)
    
    for i in range(len(toFlipList)):
        difference = toFlipList[i][0] - position
        newX = position - difference
        newPosition = (newX, toFlipList[i][1])
        if not newPosition in positionsList:
            positionsList.append(newPosition)

def performVerticalFold(position):
    toFlipList = []
    for i in range(len(positionsList) - 1, -1, -1):
        if positionsList[i][1] > position:
            toFlipList.append(positionsList[i])
            positionsList.pop(i)
        elif positionsList[i][1] == position:
            positionsList.pop(i)
    
    for i in range(len(toFlipList)):
        difference = toFlipList[i][1] - position
        newY = position - difference
        newPosition = (toFlipList[i][0], newY)
        if not newPosition in positionsList:
            positionsList.append(newPosition)

for i in range(len(foldsList)):
    foldInstruction = foldsList[i]
    if foldInstruction[0] == "x":
        performHorizontalFold(foldInstruction[1])
    else:
        performVerticalFold(foldInstruction[1])

#print("pos list after")
#print(positionsList)

print("number of positions = " + str(len(positionsList)))

maxX = 0
maxY = 0

for i in range(len(positionsList)):
    if positionsList[i][0] > maxX:
        maxX = positionsList[i][0]
    if positionsList[i][1] > maxY:
        maxY = positionsList[i][1]

#this could be output to a console, but it's easier to read in a file
outputFile = open("output.txt", "w")

#draw the grid so that the eight letters we're looking for are written out
for y in range(maxY + 1):
    lineString = ""
    for x in range(maxX + 1):
        positionTuple = (x, y)
        if positionTuple in positionsList:
            lineString += "#"
        else:
            lineString += " "
    
    outputFile.write(lineString)
    outputFile.write("\n")

outputFile.close()


