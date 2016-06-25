# aabcccccaaa -> a2b1c5a3

def compress_string(my_string):
    if not my_string:
        return ""

    result_string = ""
    past_char = my_string[0]
    past_count = 1
    for i in xrange(1, len(my_string)):
        curr_char = my_string[i]
        if past_char == curr_char:
            past_count += 1
        else:
            result_string = result_string + past_char + str(past_count)
            past_char = curr_char
            past_count = 1
    result_string = result_string + past_char + str(past_count)
    return result_string


assert('a2b1c5a3' == compress_string('aabcccccaaa'))
        


