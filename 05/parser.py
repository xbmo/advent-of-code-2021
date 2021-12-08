from line import Line

def parse(filename):
    fileData = open(filename, "r")

    line2dList = []

    while True:
        line = fileData.readline()
        if line:
            line = line.removesuffix("\n")
            splitString = line.split(" -> ")
            fromSplitString = splitString[0].split(",")
            toSplitString = splitString[1].split(",")

            line2d = Line()
            line2d.x1 = int(fromSplitString[0])
            line2d.y1 = int(fromSplitString[1])
            line2d.x2 = int(toSplitString[0])
            line2d.y2 = int(toSplitString[1])

            line2dList.append(line2d)

        else:
            break

    return line2dList