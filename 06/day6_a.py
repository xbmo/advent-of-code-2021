#https://adventofcode.com/2021/day/6
filename = "day6_test_data.txt"
#filename = "day6_data.txt"
fileData = open(filename, "r")

timerList = []

line = fileData.readline()
splitLine = line.split(",")
for i in range(len(splitLine)):
    timerList.append(int(splitLine[i]))

daysToSimulate = 256

for day in range(daysToSimulate):
    todaysCount = len(timerList)

    for i in range(todaysCount):
        if timerList[i] == 0:
            timerList.append(8) #spawn a new item at the end of the list
            timerList[i] = 6 #reset the current timer as it's just spawned a new item
        else:
            timerList[i] -= 1

print("Total number of fish after " + str(daysToSimulate) + " = " + str(len(timerList)))





