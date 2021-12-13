#https://adventofcode.com/2021/day/8

from decoder import decode

#filename = "day8_test_data.txt"
filename = "day8_data.txt"
fileData = open(filename, "r")

def decodeNumber(pattern, decodedDict):
    length = len(pattern)
    if length == 2:
        return 1
    elif length == 3:
        return 7
    elif length == 4:
        return 4
    elif length == 7:
        return 8

    for key in decodedDict:
        source = decodedDict[key]
        if len(source) == length:
            match = True
            for i in range(length):
                if pattern[i] not in source:
                    match = False
                    break
            
            if match:
                return key
    
    return -1

finalOutputValue = 0

while True:
    line = fileData.readline()
    if line:
        line = line.removesuffix("\n")
        signalOutputSplit = line.split(" | ")
        signalPatternsList = signalOutputSplit[0].split()
        outputValuesList = signalOutputSplit[1].split()
        decodedDict = decode(signalPatternsList)

        outputAsString = ""
        for i in range(len(outputValuesList)):
            number = decodeNumber(outputValuesList[i], decodedDict)
            outputAsString += str(number)

        stringToInt = int(outputAsString)

        finalOutputValue += stringToInt
    else:
        break

print("Final output value = " + str(finalOutputValue))