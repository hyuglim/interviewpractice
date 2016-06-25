# edit is insert, remove, or replace a char
# detect if two strings are at most one edit distance away from each other

from collections import Counter

def one_edit_away(s1, s2):
    if len(s1) == len(s2):
        return one_replace_away(s1, s2):
    elif len(s1) + 1 == len(s2):
        return one_insert_away(s1, s2)
    elif len(s2) + 1 == len(s1):
        return one_insert_away(s2, s1)
    else:   
        return False

def one_replace_away(s1, s2):
    index1 = 0
    index2 = 0
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:


    pass

def one_insert_away(s1, s2):
    pass



assert(one_edit_away('pale', 'ple'))
assert(one_edit_away('pales', 'pale'))
assert(one_edit_away('pale', 'bale'))
assert(not one_edit_away('pale', 'bake'))


