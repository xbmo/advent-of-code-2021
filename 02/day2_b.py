#https://adventofcode.com/2021/day/2#part2
#filename = "day2_test_data.txt"
filename = "day2_data.txt"
fileData = open(filename, "r")

horizontalPosition = 0
depth = 0
aim = 0

for line in fileData:
    split = line.split()
    symbol = split[0][0]
    value = int(split[1])
    if symbol == "u":
        aim -= value
    elif symbol == "d":
        aim += value
    elif symbol == "f":
        horizontalPosition += value
        depth += aim * value

print("Horizontal position is " + str(horizontalPosition))
print("Depth is " + str(depth))

finalValue = horizontalPosition * depth

print("Final value is " + str(finalValue))
    
