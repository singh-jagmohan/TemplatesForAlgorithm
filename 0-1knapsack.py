def knapsack(weights,values,maximum_weight):
    heightOfTable = len(values)
    weightTable = [[0 for x in xrange(maximum_weight+1)] for y in xrange(heightOfTable)]
    for column in xrange(weights[0],maximum_weight+1):
        weightTable[0][column]=values[0]
    for row in xrange(1,heightOfTable):
        for column in xrange(maximum_weight+1):
            if column>=weights[row]:
                weightTable[row][column]=max(values[row]+weightTable[row-1][column-weights[row]],weightTable[row-1][column])
            else:
                weightTable[row][column]=weightTable[row-1][column]

    return weightTable

def traceElementsOfWeights(weights,weightTable,maximum_weight):
    heightOfTable = len(weights)
    for row in xrange(heightOfTable,0,-1):
        if



knapsack([1,3,4,5],[1,4,5,7],7)