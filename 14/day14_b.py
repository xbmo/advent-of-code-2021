#https://adventofcode.com/2021/day/14

import math
from os import system

#filename = "day14_test_data.txt"
filename = "day14_data.txt"
fileData = open(filename, "r")

polymerTemplate = fileData.readline().removesuffix("\n")
pairInsertionRules = {}
polymer = polymerTemplate

#read the blank line before the pair insertion rules
fileData.readline()

while True:
        line = fileData.readline()
        if line:
            line = line.removesuffix("\n")
            split = line.split(" -> ")
            pairInsertionRules[split[0]] = split[1]
        else:
            break

polymerCountDict = {}
#count the pairs in the initial template
for i in range(len(polymer) - 1):
    pair = polymer[i : i + 2]
    if pair not in polymerCountDict:
        polymerCountDict[pair] = 1
    else:
        polymerCountDict[pair] += 1

#print(polymerCountDict)

stepsToSimulate = 40
for step in range(stepsToSimulate):
    newPolymerCountDict = {}
    totalStepCount = 0
    for key in polymerCountDict:
        count = polymerCountDict[key]
        insertCharacter = pairInsertionRules[key]
        pair1 = key[0] + insertCharacter
        pair2 = insertCharacter + key[1]
        if pair1 not in newPolymerCountDict:
            newPolymerCountDict[pair1] = count
        else:
            newPolymerCountDict[pair1] += count

        if pair2 not in newPolymerCountDict:
            newPolymerCountDict[pair2] = count
        else:
            newPolymerCountDict[pair2] += count

        totalStepCount += count * 2

    polymerCountDict = newPolymerCountDict
    totalStepCount += 1

    print(f"After step {step + 1}, polymer length is {totalStepCount}")

#print(polymerCountDict)

#count each element
elementCountDict = {}
for key in polymerCountDict:
    count = polymerCountDict[key]
    if key[0] not in elementCountDict:
        elementCountDict[key[0]] = count
    else:
        elementCountDict[key[0]] += count

    if key[1] not in elementCountDict:
        elementCountDict[key[1]] = count
    else:
        elementCountDict[key[1]] += count

#at this point, each element has been counted twice (once for the first character in the key and once for the second)
#half each value and make sure the resulting number is rounded with ceil
for key in elementCountDict:
    value = elementCountDict[key]
    value = math.ceil(value / 2)
    elementCountDict[key] = value


#print("element count")
#print(elementCountDict)

highest = 0
lowest = 1000000000000000

for val in elementCountDict.values():
    if val > highest:
        highest = val
    if val < lowest:
        lowest = val

finalValue = highest - lowest

print(f"Final value is = {finalValue}")
