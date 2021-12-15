#https://adventofcode.com/2021/day/11

#filename = "day11_test_data.txt"
filename = "day11_data.txt"
fileData = open(filename, "r")

energyGrid = []
gridSize = 10

while True:
    line = fileData.readline()
    if line:
        line = line.removesuffix("\n")
        rowList = []
        energyGrid.append(rowList)
        for i in range(len(line)):
            charString = line[i]
            rowList.append(int(charString))
    else:
        break

def updatePosition(x, y):
    if x < 0 or x >= gridSize:
        return 0
    if y < 0 or y >= gridSize:
        return 0

    #already flashed on this step. No energy left
    if energyGrid[y][x] == -1:
        return 0
    
    energyGrid[y][x] += 1
    if energyGrid[y][x] > 9:
        energyGrid[y][x] = -1 #set to -1 to indicate it flashed this turn

        count = 1
        
        #update all surrounding positions
        count += updatePosition(x - 1, y) #left
        count += updatePosition(x - 1, y - 1) #bottom left
        count += updatePosition(x, y - 1) #bottom
        count += updatePosition(x + 1, y - 1) #bottom right
        count += updatePosition(x + 1, y) #right
        count += updatePosition(x + 1, y + 1) #top right
        count += updatePosition(x, y + 1) #top
        count += updatePosition(x - 1, y + 1) #top left

        return count
    
    return 0

stepsToSimulate = 100
totalFlashes = 0

for i in range(stepsToSimulate):
    flashesToday = 0
    for y in range(gridSize):
        for x in range(gridSize):
            flashesToday += updatePosition(x, y)
    
    #set all flashed positions (value of -1) to 0 for the next day
    for y in range(gridSize):
        for x in range(gridSize):
            if energyGrid[y][x] == -1:
                energyGrid[y][x] = 0

    totalFlashes += flashesToday

    print("step " + str(i + 1) + " flashes = " + str(flashesToday))

print("total flashes after " + str(stepsToSimulate) + " steps = " + str(totalFlashes))