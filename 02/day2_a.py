#https://adventofcode.com/2021/day/2
#filename = "day2_test_data.txt"
filename = "day2_data.txt"
fileData = open(filename, "r")

horizontalPosition = 0
depth = 0

for line in fileData:
    split = line.split()
    symbol = split[0][0]
    value = int(split[1])
    if symbol == "u":
        depth -= value
    elif symbol == "d":
        depth += value
    elif symbol == "f":
        horizontalPosition += value

print("Horizontal position is " + str(horizontalPosition))
print("Depth is " + str(depth))

finalValue = horizontalPosition * depth

print("Final value is " + str(finalValue))
    
