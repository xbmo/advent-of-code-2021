#https://adventofcode.com/2021/day/10

filename = "day10_test_data.txt"
#filename = "day10_data.txt"

fileData = open(filename, "r")

def parseLineForError(line):
    closingSyntaxStack = []
    for i in range(len(line)):
        symbol = line[i]
        if symbol == "(":
            closingSyntaxStack.append(")")
        elif symbol == "{":
            closingSyntaxStack.append("}")
        elif symbol == "[":
            closingSyntaxStack.append("]")
        elif symbol == "<":
            closingSyntaxStack.append(">")
        else:
            expectedSymbol = closingSyntaxStack.pop()
            if symbol != expectedSymbol:
                if symbol == ")":
                    return 3
                elif symbol == "]":
                    return 57
                elif symbol == "}":
                    return 1197
                elif symbol == ">":
                    return 25137

    return 0

totalSyntaxErrorScore = 0

while True:
        line = fileData.readline()
        if line:
            line = line.removesuffix("\n")
            errorScore = parseLineForError(line)
            if errorScore > 0:
                totalSyntaxErrorScore += errorScore
        else:
            break

print("total syntax error score = " + str(totalSyntaxErrorScore))