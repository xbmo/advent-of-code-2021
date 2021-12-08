class Line:
    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

    def __str__(self):
        return str(self.x1) + "," + str(self.y1) + " -> " + str(self.x2) + "," + str(self.y2)

    def isHorizontal(self):
        return self.y1 == self.y2

    def isVertical(self):
        return self.x1 == self.x2

    def is45DegreeDiagonal(self):
        fromDistance = abs(self.x1 - self.x2)
        toDistance = abs(self.y1 - self.y2)
        return fromDistance == toDistance

    def getXDirection(self):
        if self.x1 < self.x2:
            return 1

        return -1

    def getYDirection(self):
        if self.y1 < self.y2:
            return 1

        return -1
    
    def getDiagonalDistance(self):
        a = abs(self.x2 - self.x1)
        b = abs(self.y2 - self.y1)

        return max(a, b)