#https://adventofcode.com/2021/day/3
#filename = "day3_test_data.txt"
filename = "day3_data.txt"
fileData = open(filename, "r")

bits = len(fileData.readline()) - 1 #-1 because of the newline character
fileData.seek(0)
print(bits)
numLines = 0
columnBitCountList = []
for i in range(bits):
    columnBitCountList.append(0)

for line in fileData:
    numLines += 1
    number = int(line, 2)

    for bit in range(bits):
        #max bit (as we are count from most significant) - current bit - one (as we don't want to shift the first one)
        bitMask = 1 << (bits - 1 - bit)
        if number & bitMask:
            columnBitCountList[bit] += 1

print("final count:")
print(columnBitCountList)
print("number of lines = " + str(numLines))

halfNumLines = numLines / 2
gammaRateString = ""
epsilonRateString = ""
for i in range(bits):
    bitNumber = 1 << (bits - 1 - bit)
    if columnBitCountList[i] > halfNumLines:
        gammaRateString += "1"
        epsilonRateString += "0"
    else:
        gammaRateString += "0"
        epsilonRateString += "1"

print("final gamma rate output:")
print(gammaRateString)
finalGammaRate = int(gammaRateString, 2)
print("final number = " + str(finalGammaRate))

print("final epsilon rate output:")
print(epsilonRateString)
finalEpsilonRate = int(epsilonRateString, 2)
print("final number = " + str(finalEpsilonRate))

finalValue = finalGammaRate * finalEpsilonRate
print(finalValue)