#https://adventofcode.com/2021/day/10

#filename = "day10_test_data.txt"
filename = "day10_data.txt"

fileData = open(filename, "r")

def parseLineForAutocompleteScore(line):
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
            if symbol != expectedSymbol: #discard corrupt lines
                return 0

    length = len(closingSyntaxStack)
    if length > 0:
        autocompleteScore = 0
        while length > 0:
            autocompleteScore *= 5
            symbol = closingSyntaxStack.pop()
            if symbol == ")":
                autocompleteScore += 1
            elif symbol == "]":
                autocompleteScore += 2
            elif symbol == "}":
                autocompleteScore += 3
            elif symbol == ">":
                autocompleteScore += 4

            length -= 1
        
        return autocompleteScore


    return 0

autocompleteScoreList = []

while True:
        line = fileData.readline()
        if line:
            line = line.removesuffix("\n")
            autocompleteScore = parseLineForAutocompleteScore(line)
            if autocompleteScore > 0:
                #print(autocompleteScore)
                autocompleteScoreList.append(autocompleteScore)
        else:
            break
    
autocompleteScoreList.sort()
#the correct answer is the middle value
middleIndex = int(len(autocompleteScoreList) / 2)
print("middle score = " + str(autocompleteScoreList[middleIndex]))