#https://adventofcode.com/2021/day/8
#filename = "day8_test_data.txt"
filename = "day8_data.txt"
fileData = open(filename, "r")

def decodeToDictionary(list):
    d = {}
    #find the easy values (ones with a unique number of characters) and remove them
    for i in range(len(list) - 1, -1, -1):
        #todo - don't read the same value twice
        segments = list[i]
        length = len(segments)
        if length == 2:
            d[segments] = 1
        elif length == 3:
            d[segments] = 7
        elif length == 4:
            d[segments] = 4
        elif length == 7:
            d[segments] = 8

    return d

easyDigitsCount = 0

while True:
    line = fileData.readline()
    if line:
        line = line.removesuffix("\n")
        signalOutputSplit = line.split(" | ")
        outputValuesList = signalOutputSplit[1].split()
        decoded = decodeToDictionary(outputValuesList)
        #print(decoded)
        #print(outputValuesList)
        for i in range(len(outputValuesList)):
            segments = outputValuesList[i]
            if segments in decoded:
                easyDigitsCount += 1
    else:
        break

print(easyDigitsCount)

