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

totalRiskLevel = 0

for y in range(numRows):
    for x in range(numColumns):
        current = heightmap[y][x]
        lower = True
        down = y - 1
        if down >= 0:
            if heightmap[down][x] <= current:
                lower = False
        if lower:
            up = y + 1
            if up < numRows:
                if heightmap[up][x] <= current:
                    lower = False
        if lower:
            left = x - 1
            if left >= 0:
                if heightmap[y][left] <= current:
                    lower = False
        if lower:
            right = x + 1
            if right < numColumns:
                if heightmap[y][right] <= current:
                    lower = False
        if lower:
            #print("low point = " + str(current) + " | " + str(x) + "," + str(y))
            totalRiskLevel += 1 + current

print("total risk level = " + str(totalRiskLevel))

