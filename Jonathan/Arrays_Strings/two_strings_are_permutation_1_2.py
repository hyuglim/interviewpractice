# given two strings determine if one is permutation of the other

from collections import Counter
def are_permutations(string_one, string_two):
    if len(string_one) != len(string_two):
        return False
    
    char_count_set = Counter(string_one)
    for char in string_two:
        if char not in char_count_set or \
                char_count_set[char] < 0:
            return False
        else:
            char_count_set[char] -= 1
    return all(count == 0 for char, count in char_count_set.iteritems())


assert(are_permutations('apple', 'pplea'))
assert(not are_permutations('banana', 'apple'))
assert(are_permutations('fuck', 'fuck'))
assert(not are_permutations('asdgadsb', 'asdgasdgdasgf'))
