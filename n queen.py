### function to check if two posirions are compatible with each other
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

def backtrackForFirst(N):
    if N==1:
        return [0,0]
    positions=[]
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
            if len(positions)>=1:
                lastPosition = positions.pop()
                next_column = lastPosition[1]+1
            else:
                break
    return positions





def is_compatible_with_list(pos_to_compare,list_to_compare_with):
    for position in list_to_compare_with:
        if is_compatible(pos_to_compare,position):
            pass
        else:
            return False
    return True


def backtrackAll(N):
    if N<1:
        return 0
    if N==1:
        return [[0,0]]
    positions = [[[0,0]]]
    next_row=1
    next_column=0
    index_of_combination = 0
    status = False
    second_status = False
    while 1:
        while next_row<N:
            while next_column<N:
                if is_compatible_with_list([next_row,next_column],positions[index_of_combination]):
                    positions[index_of_combination].append([next_row,next_column])
                    status =True
                    break
                else:
                    next_column +=1
            if status==True:
                next_row +=1
                next_column = 0
                status = False
            else:
                if next_row==0 and next_column==N:
                    second_status = True
                    break
                next_row -=1
                next_column =positions[index_of_combination].pop()[1]+1
        if second_status==True:
            break
        else:
            index_of_combination +=1
            next_column=positions[index_of_combination - 1][-1][1]+1
            next_row = N - 1
            positions.append(positions[index_of_combination-1][:-1])
            second_status =False

    if positions[index_of_combination]==[]:
        positions.pop()
    return positions

print backtrackForFirst(4)
#print backtrackAll(4)

