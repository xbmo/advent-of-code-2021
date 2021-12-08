def parse(filename):
    fileData = open(filename, "r")

    d = {} 

    #the first line is the draw order for the numbers
    drawOrderString = fileData.readline()
    drawOrderStringArray = drawOrderString.split(",")
    drawOrderList = []
    for i in range(len(drawOrderStringArray)):
        drawOrderList.append(int(drawOrderStringArray[i]))

    d["draw"] = drawOrderList

    #now there is an empty line between each grid of bingo cards. Bingo cards are a 5 by 5 grid
    #where columns are separated by an empty space and rows are separated by a newline
    numBoards = 0

    while True:
        line = fileData.readline()
        if line:
            #the newline has just been read, now read the five rows
            row = 0
            gridList = []
            while row < 5:
                rowList = []
                gridList.append(rowList)
                rowString = fileData.readline()
                rowStringArray = rowString.split()
                for i in range(len(rowStringArray)):
                    rowList.append(int(rowStringArray[i]))

                row += 1

            d[numBoards] = gridList
            numBoards += 1
        else:
            break

    d["numBoards"] = numBoards

    return d