##insertion sort can be used if we don't have much space but in this case time complexity will increase to O(n^2)


##getting element one by one
def getElement():
    return int(raw_input())



##inserting into list at the right position
def insertElementIntoList(element,oldList):
    for index,item in enumerate(oldList):
        if element<item:
            return oldList[:index]+[element]+oldList[index:]
    return oldList+[element]

if __name__ == "__main__":
    currentSortedList=[]
    while 1:
        currentSortedList = insertElementIntoList(getElement(),currentSortedList)
        print currentSortedList




