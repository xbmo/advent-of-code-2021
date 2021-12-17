#https://adventofcode.com/2021/day/12

#filename = "day12_test_data_set_1.txt"
#filename = "day12_test_data_set_2.txt"
#filename = "day12_test_data_set_3.txt"
filename = "day12_data.txt"
fileData = open(filename, "r")

connectionsDict = {}

startNode = "start"
endNode = "end"

def isSmallCave(key):
    for i in range(len(key)):
        if str.isupper(key[i]):
            return False

    return True

while True:
    line = fileData.readline()
    if line:
        line = line.removesuffix("\n")
        rowList = []
        splitString = line.split("-")
        indexZeroIsEnd = splitString[0] == endNode
        indexOneIsStart = splitString[1] == startNode
        #add the connection twice, once for each direction (unless it's the start or end node)
        if not indexZeroIsEnd and not indexOneIsStart:
            if not splitString[0] in connectionsDict:
                connectionsDict[splitString[0]] = []
            connectionsDict[splitString[0]].append(splitString[1])

        indexOneIsEnd = splitString[1] == endNode
        indexZeroIsStart = splitString[0] == startNode

        if indexZeroIsStart or indexOneIsEnd:
            continue
        
        if not splitString[1] in connectionsDict:
            connectionsDict[splitString[1]] = []
        connectionsDict[splitString[1]].append(splitString[0])
            
    else:
        break

#print(connectionsDict)

allPathsList = []

def getPaths(key, pathList, smallCaveThatCanBeVisitedTwice = ""):
    pathList.append(key)
    if key == endNode:
        allPathsList.append(pathList)
    else:
        listForKey = connectionsDict[key]
        for nextKey in listForKey:
            smallCaveToVisitTwiceForThisPath = smallCaveThatCanBeVisitedTwice
            if nextKey in pathList:           
                if isSmallCave(nextKey):
                    if smallCaveToVisitTwiceForThisPath == "" and pathList.count(nextKey) < 2:
                        smallCaveToVisitTwiceForThisPath = nextKey
                    else:
                        continue
            
            newList = pathList.copy()
                
            getPaths(nextKey, newList, smallCaveToVisitTwiceForThisPath)

getPaths(startNode, [])

#for i in range(len(allPathsList)):
#    print(allPathsList[i])

#print(allPathsList)

print("number of paths = " + str(len(allPathsList)))
