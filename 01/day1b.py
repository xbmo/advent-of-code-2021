#https://adventofcode.com/2021/day/1#part2
#filename = "day1_test_data.txt"
filename = "day1_data.txt"
fileData = open(filename, "r")

dataList = []
previousValue = -1
isFirstLine = True
count = 0

#first process the file and convert all lines to numbers, and store them in a list
for line in fileData:
    numericValue = int(line)
    dataList.append(numericValue)

listLength = len(dataList)
print("List length = " + str(listLength))
#go through the numeric list and perform the three measurement sliding window check
for i in range(listLength - 2):
    totalValue = 0
    for j in range(3):
        totalValue += dataList[i + j]
    if isFirstLine:
        isFirstLine = False
    else:
        if totalValue > previousValue:
            count += 1
    previousValue = totalValue

print("There are " + str(count) + " measurements larger than the previous measurement.")
