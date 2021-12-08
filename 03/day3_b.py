#https://adventofcode.com/2021/day/3
#filename = "day3_test_data.txt"
filename = "day3_data.txt"
fileData = open(filename, "r")

numBits = len(fileData.readline()) - 1 #-1 because of the newline character
fileData.seek(0)

oxygenGenList = []
co2ScrubberList = []

#first process the file data by converting to a number and storing in lists
for line in fileData:
    number = int(line, 2)

    #add every number to the lists. They will be reduced in the next step
    oxygenGenList.append(number)
    co2ScrubberList.append(number)

def reduce(list, matchMostCommonBit):
    for bit in range(numBits):
        #max bit (as we are count from most significant) - current bit - one (as we don't want to shift the first one)
        bitMask = 1 << (numBits - 1 - bit)
        #go through the current bit position and count how many times it is set
        bitSetAsOneCount = 0

        listLength = len(list)

        for i in range(listLength):
            if list[i] & bitMask:
                bitSetAsOneCount += 1

        mostCommonBitIsOne = bitSetAsOneCount >= listLength / 2

        #now the most common bit value has been determined, go through each entry in the list and delete if 
        #if it doesn't match the 'matchMostCommonBit' argument. The list is iterated backwards so that items can be removed
        for i in range(listLength - 1, -1, -1):
            bitValueIsOne = list[i] & bitMask
            if mostCommonBitIsOne:
                if bitValueIsOne and not matchMostCommonBit or not bitValueIsOne and matchMostCommonBit:
                    del(list[i])
            else:
                if not bitValueIsOne and not matchMostCommonBit or bitValueIsOne and matchMostCommonBit:
                    del(list[i])

        if len(list) == 1:
            break

reduce(oxygenGenList, True)
oxygenGenValue = oxygenGenList[0]
print("Final Oxygen Generator value = " + str(oxygenGenValue))
print(oxygenGenList)

reduce(co2ScrubberList, False)
co2ScrubberValue = co2ScrubberList[0]
print("Final CO2 Scrubber value = " + str(co2ScrubberValue))
print(co2ScrubberList)

finalValue = oxygenGenValue * co2ScrubberValue

print("Final value = " + str(finalValue))

        

