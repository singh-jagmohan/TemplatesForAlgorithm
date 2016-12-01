# generate the value table for all items
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


# return the exact items with which we get the maximum value
def traceElementsOfWeights(weights,weightTable,maximum_weight):
    heightOfTable = len(weights)
    steps = []
    for row in xrange(heightOfTable-1,-1,-1):
        if row == 0:
            if weightTable[row][maximum_weight]==0:
                pass
            else:
                steps = [weights[row]] + steps
        else:
            if weightTable[row][maximum_weight]==weightTable[row-1][maximum_weight]:
                pass
            else:
                steps = [weights[row]]+steps
                maximum_weight -= weights[row]
    return steps




weights = [3,1,4,5]
values = [4,1,5,7]
maximum_weight = 7


if __name__=='__main__':

    ###table has the value for all intermediate weights and maximum values which can be acheived
    table = knapsack(weights,values,maximum_weight)
    # for x in table:
    #     print x
    print table[len(weights)-1][maximum_weight]
    # for index, i in enumerate(table):
    #     print i

    print traceElementsOfWeights(weights,table,maximum_weight)
