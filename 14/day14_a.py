#https://adventofcode.com/2021/day/14

filename = "day14_test_data.txt"
#filename = "day14_data.txt"
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

stepsToSimulate = 5
for step in range(stepsToSimulate):
    polymerList = []
    for i in range(len(polymer) - 1):
        pair = polymer[i : i + 2]
        #print(pair)
        toInsert = pairInsertionRules[pair]
        #print(f" insert {toInsert}")
        polymerList.append(pair[0])
        polymerList.append(toInsert)
    
    #put the last element on the end of the list
    polymerList.append(polymer[len(polymer) - 1])

    polymer = "".join(polymerList)
    
    print(f"After step {step + 1}: {polymer}")
    print(f"After step {step + 1}, polymer length is {len(polymer)}")

#count each element
elementCountDict = {}
for i in polymer:
    if not i in elementCountDict:
        elementCountDict[i] = 1
    else:
        elementCountDict[i] += 1

print(elementCountDict)

highest = 0
lowest = 1000000000

for val in elementCountDict.values():
    if val > highest:
        highest = val
    if val < lowest:
        lowest = val

finalValue = highest - lowest

print(f"Final value is = {finalValue}")

