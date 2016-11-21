global edit_table
edit_table = list()

# function to initialize edit table
def init_edit_table(original_string_length,final_string_length):
    edit_table.append([x for x in xrange(original_string_length + 1)])
    for i in xrange(1, final_string_length + 1):
        edit_table.append([i] + [0] * original_string_length)


# creating the table for number of edits
def create_edit_table(original_string,final_string):
    final_string_length = len(final_string)
    original_string_length = len(original_string)
    init_edit_table(original_string_length,final_string_length)
    for original_string_counter in xrange(original_string_length):
        for final_string_counter in xrange(final_string_length):
            if original_string[original_string_counter]==final_string[final_string_counter]:
                edit_table[final_string_counter+1][original_string_counter+1]=edit_table[final_string_counter][original_string_counter]
            else:
                edit_table[final_string_counter+1][original_string_counter+1]=min(edit_table[final_string_counter][original_string_counter],edit_table[final_string_counter+1][original_string_counter],edit_table[final_string_counter][original_string_counter+1])+1



    return edit_table[final_string_length][original_string_length]


# function to get the steps to convert the original string to final string from end of strings
def create_edit_characters(original_string,final_string):
    final_string_length = len(final_string)
    character_index_at_original = len(original_string)
    character_table=[]
    character_index_at_final = final_string_length
    while character_index_at_final>0 :
        if edit_table[character_index_at_final][character_index_at_original]==edit_table[character_index_at_final-1][character_index_at_original-1] and original_string[character_index_at_original-1]==final_string[character_index_at_final-1]:
            character_index_at_final -=1
            character_index_at_original -=1
        elif edit_table[character_index_at_final][character_index_at_original]-1==edit_table[character_index_at_final-1][character_index_at_original]:
            character_table.append([final_string[character_index_at_final-1],'ADD'])
            character_index_at_final -=1
        elif edit_table[character_index_at_final][character_index_at_original]-1==edit_table[character_index_at_final][character_index_at_original-1]:
            character_table.append([original_string[character_index_at_original-1],'DELETE'])
            character_index_at_original -=1
        elif edit_table[character_index_at_final][character_index_at_original]-1==edit_table[character_index_at_final-1][character_index_at_original-1]:
            character_table.append([original_string[character_index_at_original-1],final_string[character_index_at_final-1], 'MODIFY'])
            character_index_at_final -=1
            character_index_at_original -=1
            # if final_string[character_index_at_final-1]==original_string[character_index_at_original-1]:
    if character_index_at_original>0:
        character_table.append([original_string[character_index_at_original-1],'DELETE'])
        character_index_at_original -=1

    return character_table






if __name__ == '__main__':
    original_string = 'random'
    final_string = 'radim'
    number_of_edit = create_edit_table(original_string, final_string)
    print number_of_edit
    # extra data for more complicated problem
    for x in edit_table:
        print x
    steps = create_edit_characters(original_string, final_string)
    for x in steps[::-1]:
        print x


