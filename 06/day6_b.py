#https://adventofcode.com/2021/day/6
#filename = "day6_test_data.txt"
filename = "day6_data.txt"
fileData = open(filename, "r")

timerDict = {}
#set up days 0-8 in the dictionary
for i in range(9):
    timerDict[i] = 0

line = fileData.readline()
splitLine = line.split(",")
for i in range(len(splitLine)):
    daysLeft = int(splitLine[i])
    timerDict[daysLeft] += 1

daysToSimulate = 256

numberOfFishToRespawnAndSpawnTomorrow = 0

for day in range(daysToSimulate):

    numberOfFishToRespawnAndSpawnToday = numberOfFishToRespawnAndSpawnTomorrow

    #decrement all day counts
    for i in range(0,8):
        timerDict[i] = timerDict[i + 1]
    timerDict[8] = 0

    numberOfFishToRespawnAndSpawnTomorrow = timerDict[0]

    #add new items (numberToCreate) to day 8
    timerDict[8] += numberOfFishToRespawnAndSpawnToday

    #add fish who spawned a new fish last turn (numberOfFishToReset) to day 6
    timerDict[6] += numberOfFishToRespawnAndSpawnToday

totalNumberOfFish = 0

for i in range(9):
    totalNumberOfFish += timerDict[i]

print("Total number of fish after " + str(daysToSimulate) + " = " + str(totalNumberOfFish))





