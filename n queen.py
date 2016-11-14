def is_compatible(pos_to_compare,pos_to_be_compared_with):
    if pos_to_be_compared_with[0]==pos_to_compare[0]:
        return False
    if pos_to_be_compared_with[1]==pos_to_compare[1]:
        return False
    if pos_to_compare[0]+pos_to_compare[1]==pos_to_be_compared_with[0]+pos_to_be_compared_with[1]:
        return False
    if pos_to_compare[0]-pos_to_compare[1]==pos_to_be_compared_with[0]-pos_to_be_compared_with[1]:
        return False
    return True

def backtrack(N):
    if N==1:
        return [0,0]
    positions=[]
    first_row_column = 0
    positions.append([0,0])
    next_row = 1
    next_column = 0
    status = True
    second_status = False
    while next_row<N:
        while next_column<N:
            for position in positions:
                if is_compatible([next_row,next_column],position):
                    pass
                else:
                    status = False
                    break
            if status==False:
                status =True
                next_column +=1
            else:
                positions.append([next_row, next_column])
                second_status = True
                break
        if second_status==True:
            next_row +=1
            next_column=0
            second_status = False
        else:
            next_row -=1
            lastPosition = positions.pop()
            next_column = lastPosition[1]+1
    print positions

backtrack(5)
