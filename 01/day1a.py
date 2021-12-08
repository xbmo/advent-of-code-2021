#https://adventofcode.com/2021/day/1
#filename = "day1_test_data.txt"
#filename = "day1_data.txt"
filename = "day1_data_dan.txt"
fileData = open(filename, "r")
outFile = open("day1out.txt", "w")

isFirstLine = True
previousValue = -1
#count is incremented each time the numeric value for the line is larger than the previous one 
count = 0
for line in fileData:
    numericValue = int(line)
    if isFirstLine:
        isFirstLine = False
    else:
        if numericValue > previousValue:
            count += 1
            outFile.write("(increased)\n")
        else:
            outFile.write("(decreased)\n")
    previousValue = numericValue

print("There are " + str(count) + " measurements larger than the previous measurement.")

fileData.close()
outFile.close()