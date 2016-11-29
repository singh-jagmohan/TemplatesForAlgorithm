def constructTable(stringA,stringB,interleavingString,lenStringA,lenStringB):
    interleavingTable = []
    # creating table of (lenStringB+1)*(lenStringA+1) with fields initialized to 1
    for x in xrange(lenStringB + 1):
        interleavingTable.append([1] * (lenStringA + 1))
    # change first row
    for i in xrange(1, lenStringA + 1):
        if stringA[i - 1] == interleavingString[i - 1] and interleavingTable[0][i - 1] == 1:
            interleavingTable[0][i] = 1
        else:
            interleavingTable[0][i] = 0
    # change first column
    for i in xrange(1,lenStringB+1):
        if stringB[i-1] == interleavingString[i-1] and interleavingTable[i-1][0]==1:
            interleavingTable[i][0]=1
        else:
            interleavingTable[i][0] = 0
    return interleavingTable

def isInterleaving(stringA,stringB,interleavingString):
    lenStringA = len(stringA)
    lenStringB = len(stringB)
    interleavingTable =constructTable(stringA,stringB,interleavingString,lenStringA,lenStringB)
    for rowIndex in xrange(1,lenStringB+1):
        for columnIndex in xrange(1,lenStringA+1):
            if interleavingString[rowIndex+columnIndex-1]==stringA[columnIndex-1] and interleavingTable[rowIndex][columnIndex-1]==1:
                interleavingTable[rowIndex][columnIndex]=1
            elif interleavingString[rowIndex+columnIndex-1]==stringB[rowIndex-1] and interleavingTable[rowIndex-1][columnIndex]==1:
                interleavingTable[rowIndex][columnIndex]=1
            else:
                interleavingTable[rowIndex][columnIndex] = 0
    return interleavingTable[lenStringB][lenStringA]




if __name__=='__main__':
    stringA = 'aab'
    stringB = 'axy'
    interleavingString1 = 'abaaxy'
    interleavingString2 = 'aaxaby'
    if len(stringA)+len(stringB)==len(interleavingString1):
        if isInterleaving(stringA,stringB,interleavingString1):
            print "YES"
        else:
            print "NO"
    else:
        print "NO"
    if len(stringA) + len(stringB) == len(interleavingString2):
        if isInterleaving(stringA, stringB, interleavingString2):
            print "YES"
        else:
            print "NO"
    else:
        print "NO"
