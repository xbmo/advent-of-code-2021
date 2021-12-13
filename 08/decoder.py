""" For the purposes of defining a consistent pattern, the seven-segment
display looks like the following

 aaa
b   c
b   c
 ddd
e   f
e   f
 ggg
 
The decoder will map the scrambled version to these keys
  """

def decode(signalPatternsList):
    numToPatternDict = {}
    #find the easy segments (1, 4, 7 and 8)
    one = ""
    for i in range(len(signalPatternsList) - 1, -1, -1):
        signalPattern = signalPatternsList[i]
        length = len(signalPattern)
        if length == 2:
            one = signalPattern
            numToPatternDict[1] = signalPattern
            del(signalPatternsList[i])
        elif length == 3:
            seven = signalPattern
            numToPatternDict[7] = signalPattern
            del(signalPatternsList[i])
        elif length == 4:
            four = signalPattern
            numToPatternDict[4] = signalPattern
            del(signalPatternsList[i])
        elif length == 7:
            numToPatternDict[8] = signalPattern
            del(signalPatternsList[i])

    #the one segment entry contains c and f. We can't know which is which at this point
    cAndF = one

    #print("c and f = " + cAndF)

    #look at the unique segment in number seven to find 'a'
    a = ""
    for i in range(3):
        segment = seven[i]
        if segment not in cAndF:
            a = segment
            break

    #print("a = " + a)

    #four has b and d, but again we can't know what the order is yet
    bAndD = ""
    for i in range(4):
        segment = four[i]
        if segment not in cAndF:
            bAndD += segment
    
    #print("b and d = " + bAndD)

    #look for number nine as it has a unique segment at this point (g)
    g = ""
    for i in range(len(signalPatternsList)):
        length = len(signalPatternsList[i])
        if length == 6:
            numUniqueSegments = 0
            lastUniqueSegment = ""
            for j in range(6):
                segment = signalPatternsList[i][j]
                if segment not in cAndF and segment not in bAndD and segment != a:
                    numUniqueSegments += 1
                    lastUniqueSegment = segment
                    if numUniqueSegments > 1: 
                        #this is not the correct pattern
                        break
            
            if numUniqueSegments == 1:
                #segment g has been found
                g = lastUniqueSegment
                #number nine has been found
                numToPatternDict[9] = signalPatternsList[i]
                del(signalPatternsList[i])
                break
    
    #print("g = " + g)

    #look for number three which contains the unconfirmed segment d. Finding it will also confirm b.
    d = ""
    b = ""
    e = ""
    for i in range(len(signalPatternsList)):
        length = len(signalPatternsList[i])
        if length == 5:
            numUniqueSegments = 0
            lastUniqueSegment = ""
            for j in range(5):
                segment = signalPatternsList[i][j]
                if segment not in cAndF and segment != a and segment != g:
                    numUniqueSegments += 1
                    lastUniqueSegment = segment
                    if numUniqueSegments > 1: 
                        #this is not the correct pattern
                        break
            
            if numUniqueSegments == 1:
                #segment d has been found
                d = lastUniqueSegment
                #number three has been found
                numToPatternDict[3] = signalPatternsList[i]
                del(signalPatternsList[i])

                #check bAndD to find b
                if d == bAndD[0]:
                    b = bAndD[1]
                else:
                    b = bAndD[0]

                break
    
    #print("b = " + b)
    #print("d = " + d)

    #we are left with one completely unknown segment (e) which can now be confirmed
    #iterate over letters a to g using ascii values
    e = ""
    for i in range(97, 104):
        letter = chr(i)
        if letter != a and letter != b and letter != d and letter != g and letter not in cAndF:
            e = letter
            break

    #print("e = " + e)
    
    #the only segments left unconfirmed now are cAndF. 
    #Look for the number six,  because it doesn't contain segment c, thus confirming f
    c = ""
    f = ""
    for i in range(len(signalPatternsList)):
        length = len(signalPatternsList[i])
        if length == 6:
            numUniqueSegments = 0
            lastUniqueSegment = ""
            for j in range(6):
                segment = signalPatternsList[i][j]
                if segment != a and segment != b and segment != d and segment != e and segment != g:
                    numUniqueSegments += 1
                    lastUniqueSegment = segment
                    if numUniqueSegments > 1: 
                        #this is not the correct pattern
                        break

            if numUniqueSegments == 1:
                #segment f has been found
                f = lastUniqueSegment

                #number 6 has been found
                numToPatternDict[6] = signalPatternsList[i]
                del(signalPatternsList[i])
                
                #check cAndF to find c
                if f == cAndF[0]:
                    c = cAndF[1]
                else:
                    c = cAndF[0]

                break
    
    #print("c = " + c)
    #print("f = " + f)

    #the final thing left to do is figure out the patterns for 0, 2 and 5
    for i in range(len(signalPatternsList) - 1, -1, -1):
        signalPattern = signalPatternsList[i]
        #the last remaning six segment pattern is zero
        if len(signalPattern) == 6:
            numToPatternDict[0] = signalPattern
        #segment c is in 2 but not in 5
        elif c in signalPattern:
            numToPatternDict[2] = signalPattern
        else:
            numToPatternDict[5] = signalPattern

    return numToPatternDict
