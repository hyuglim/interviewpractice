# implement algo to determine if string has unique characters


def has_unique_chars(my_string, num_alphabet = 128):
    if len(my_string) > num_alphabet: 
        return False
    
    char_set = [False for i in xrange(num_alphabet)]
    for char in my_string:
        char_index = ord(char)
        if char_set[char_index]:
            return False
        char_set[ord(char)] = True
    return True




# test cases
assert(has_unique_chars("abcdefg"))
assert(not has_unique_chars("apple"))
assert(has_unique_chars("default"))
assert(not has_unique_chars("eeeeeeeee"))


