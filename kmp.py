def build_prefix_suffix_len_array(s):
    if len(s)==0:
        return [0]
    length_of_string = len(s)
    array = [0]*length_of_string
    first_index = 0
    second_index = 1
    while second_index<length_of_string:
        if s[first_index]==s[second_index]:
            array[second_index] = first_index+1
            first_index += 1
            second_index += 1
        else:
            if first_index==0:
                second_index += 1
            else:
                first_index = array[first_index-1]

    return array


def pattern_match_all_occurrence(pattern,text):
    if len(pattern)>len(text):
        return []
    else:
        matches=[]
        prefix_suffix_array = build_prefix_suffix_len_array(pattern)
        index_in_pattern = 0
        index_in_text = 0
        while index_in_text<len(text):
            if pattern[index_in_pattern]==text[index_in_text]:
                index_in_pattern +=1
                index_in_text +=1
            else:
                if index_in_pattern==0:
                    index_in_text += 1
                else:
                    index_in_pattern = prefix_suffix_array[index_in_pattern-1]
            if index_in_pattern==len(pattern):
                matches.append(index_in_text-index_in_pattern)
                index_in_text=index_in_text-index_in_pattern+1
                index_in_pattern=0

        return matches


def pattern_match_first_occurrence(pattern,text):
    if len(pattern)>len(text):
        return -1
    else:
        prefix_suffix_array = build_prefix_suffix_len_array(pattern)
        index_in_pattern = 0
        index_in_text = 0
        while index_in_text<len(text):
            if pattern[index_in_pattern]==text[index_in_text]:
                index_in_pattern +=1
                index_in_text +=1
            else:
                if index_in_pattern==0:
                    index_in_text += 1
                else:
                    index_in_pattern = prefix_suffix_array[index_in_pattern-1]
            if index_in_pattern==len(pattern):
                return index_in_text-index_in_pattern
        return -1


print pattern_match_all_occurrence('AABA','AABAACAADAABAAABAA')
print pattern_match_first_occurrence('AABA','AABAACAADAABAAABAA')

print pattern_match_all_occurrence('AABE','AABAACAADAABAAABAA')
print pattern_match_first_occurrence('AABE','AABAACAADAABAAABAA')





