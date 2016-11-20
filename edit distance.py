from collections import defaultdict


def init_edit_table(original_string_length,final_string_length ):
    edit_table = []
    print edit_table
    edit_table.append([x for x in xrange(original_string_length + 1)])
    for i in xrange(1, final_string_length + 1):
        edit_table.append([i] + [0] * original_string_length)
    return edit_table


# def get

def create_edit_table(original_string,final_string):
    final_string_length = len(final_string)
    original_string_length = len(original_string)
    edit_table = init_edit_table(original_string_length,final_string_length)
    for original_string_counter in xrange(original_string_length):
        for final_string_counter in xrange(final_string_length):
            if original_string[original_string_counter]==final_string[final_string_counter]:
                edit_table[final_string_counter+1][original_string_counter+1]=edit_table[final_string_counter][original_string_counter]
            else:
                edit_table[final_string_counter+1][original_string_counter+1]=min(edit_table[final_string_counter][original_string_counter],edit_table[final_string_counter+1][original_string_counter],edit_table[final_string_counter][original_string_counter+1])+1



    return edit_table
    # table = [final_string_length+1][original_string_length+1]
    # pass


edit_table = create_edit_table('abcdef','azced')
def create_edit_characters(edit_table):
    print
for x in edit_table:
    print x