global LCSTable,lenStringA,lenStringB
LCSTable = []


def initLCSTable():
    for x in xrange(lenStringB+1):
        LCSTable.append([0]*(lenStringA+1))


def createLCSTable(stringA,stringB):
    for rowIndex in xrange(1,lenStringB+1):
        for columnIndex in xrange(1,lenStringA+1):
            if stringA[columnIndex-1]==stringB[rowIndex-1]:
                LCSTable[rowIndex][columnIndex] = LCSTable[rowIndex-1][columnIndex-1]+1
            else:
                LCSTable[rowIndex][columnIndex] = max(LCSTable[rowIndex][columnIndex-1],LCSTable[rowIndex-1][columnIndex])
    # for x in LCSTable:
    #     print x

def createLCS(stringA,stringB):
    rowIndex = lenStringB
    columnIndex = lenStringA
    LCS = ''
    while rowIndex >0:
        if stringA[columnIndex-1]==stringB[rowIndex-1]:
            LCS = stringA[columnIndex-1]+LCS
            rowIndex -=1
            columnIndex -=1
        elif LCSTable[rowIndex][columnIndex]==LCSTable[rowIndex-1][columnIndex]:
            rowIndex -=1
        else:
            columnIndex -=1
    return LCS

if __name__ == '__main__':
    stringA = 'freako'
    stringB = 'faker'
    lenStringA = len(stringA)
    lenStringB = len(stringB)
    initLCSTable()
    createLCSTable(stringA,stringB)
    print LCSTable[lenStringB][lenStringA]
    print createLCS(stringA,stringB)




