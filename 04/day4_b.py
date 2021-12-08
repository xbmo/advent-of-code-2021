#https://adventofcode.com/2021/day/4

from parser import parse

#filename = "day4_test_data.txt"
filename = "day4_data.txt"

numRows = 5
numColumns = 5

parsedData = parse(filename)
#print(parsedData)

draw = parsedData["draw"]
numberOfBallsDrawn = len(draw)
drawIndex = 0
numBoards = parsedData["numBoards"]

finishedBoardLists = []

solutionFound = False

while drawIndex < numberOfBallsDrawn and not solutionFound:
    currentNumber = draw[drawIndex]

    #update each board with the current number, and check if the board has won
    for i in range(numBoards):
        #check to see if this board has already won
        if i in finishedBoardLists:
            continue

        board = parsedData[i]
        
        boardComplete = False

        for row in range(numRows):
            for column in range(numColumns):
                if board[row][column] == currentNumber:
                    #change number to -1 when it is found
                    board[row][column] = -1
                    #check the rest of the row to see if it is complete
                    allFound = True
                    for checkColumn in range(numColumns):
                        if board[row][checkColumn] != -1:
                            allFound = False
                            break
                    if not allFound:
                        allFound = True
                        #if the row is not complete, check the column
                        for checkRow in range(numRows):
                            if board[checkRow][column] != -1:
                                allFound = False
                                break
                    
                    if allFound:
                        boardComplete = True
                        break

        if boardComplete:
            #add this board to the finished list
            finishedBoardLists.append(i)

            if len(finishedBoardLists) == numBoards:
                #find all the unused squares on the grid
                unmarkedSum = 0
                for row in range(numRows):
                    for column in range(numColumns):
                        if board[row][column] != -1:
                            unmarkedSum += board[row][column]

                print("Final winning board = " + str(i))
                print("Current number = " + str(currentNumber))
                print("Unmarked sum = " + str(unmarkedSum))
                finalAnswer = currentNumber * unmarkedSum
                print("Final answer = " + str(finalAnswer))
                break

    drawIndex += 1

