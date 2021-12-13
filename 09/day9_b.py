#https://adventofcode.com/2021/day/9

#filename = "day9_test_data.txt"
filename = "day9_data.txt"
fileData = open(filename, "r")

heightmap = []

numRows = 0

while True:
        line = fileData.readline()
        if line:
            line = line.removesuffix("\n")
            rowList = []
            numRows += 1
            heightmap.append(rowList)
            for i in range(len(line)):
                charString = line[i]
                rowList.append(int(charString))
        else:
            break

#print(heightmap)

numColumns = len(heightmap[0])

#print(numRows)
#print(numColumns)

def getTotalRiskLevel(x, y):
    current = heightmap[y][x]
    down = y - 1
    if down >= 0:
        if heightmap[down][x] <= current:
            return -1
    up = y + 1
    if up < numRows:
        if heightmap[up][x] <= current:
            return -1
    left = x - 1
    if left >= 0:
        if heightmap[y][left] <= current:
            return -1
    right = x + 1
    if right < numColumns:
        if heightmap[y][right] <= current:
            return -1

    #print("low point = " + str(current) + " | " + str(x) + "," + str(y))
    return 1 + current

def getCountInDirection(x, y, visited):
    if x >= 0 and x < numColumns:
        if y >= 0 and y < numRows:
            position = (x, y)
            if position not in visited:
                if heightmap[y][x] != 9:
                    #print(str(heightmap[y][x]) + " (" + str(x) + "," + str(y) + ")")
                    
                    count = 1
                    visited.append((x, y))
                    count += getCountInDirection(x + 1, y, visited)
                    count += getCountInDirection(x - 1, y, visited)
                    count += getCountInDirection(x, y + 1, visited)
                    count += getCountInDirection(x, y - 1, visited)

                    return count

    return 0

basinsList = []

for y in range(numRows):
    for x in range(numColumns):
        risk = getTotalRiskLevel(x, y)
        if risk > -1:
            #after 9 days, it's finally time for some recursion
            visitedList = []
            basinSize = getCountInDirection(x, y, visitedList)
            basinsList.append(basinSize)

#print(basinsList)

basinsList.sort()

#take the last three items and multiply them
listSize = len(basinsList)
multiplied = basinsList[listSize -1] * basinsList[listSize - 2] * basinsList[listSize - 3]
print("final size = " + str(multiplied))
    

