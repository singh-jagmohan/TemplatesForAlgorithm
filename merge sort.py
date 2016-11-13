def mergeLists(firstList,secondList):
    mergedList = []
    while len(firstList) != 0 and len(secondList) != 0:
        if firstList[0] < secondList[0]:
            mergedList += [firstList[0]]
            firstList=firstList[1:]
        else:
            mergedList += [secondList[0]]
            secondList = secondList[1:]
    if len(firstList) == 0:
        mergedList +=secondList
    else:
        mergedList +=firstList
    return mergedList

def sortByMerge(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = len(x)/2
        firstList = sortByMerge(x[:middle])
        secondList = sortByMerge(x[middle:])
        return mergeLists(firstList,secondList)


### fucntion to get chunks of input data
def getList():
    return map(int,raw_input().split(" "))


##main function
if __name__ == "__main__":
    ##initialize list as empty
    currentSortedList = []
    while 1:
        ## get chunk of input sort it and merge it with current list
        currentSortedList = mergeLists(currentSortedList,sortByMerge(getList()))
        print currentSortedList

