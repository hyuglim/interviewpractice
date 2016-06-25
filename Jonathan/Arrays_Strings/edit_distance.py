# get the number of edits needed to 
# turn string1 into string2
# edit: insert, delete, replace a char


def edit_distance(str1, str2, len1, len2):
    
    # if str1 is empty, need to insert len2 times to str1
    if not len1:
        return len2

    if not len2:
        return len1

    # if last chars are the same, then decrease subproblem size by 1
    if str1[len1-1] == str2[len2-1]:
        return edit_distance(str1, str2, len1-1, len2-1)

    # consider 3 operations on last char of the first string
    return 1 + min(
                    edit_distance(str1, str2, len1, len2-1), # insert
                    edit_distance(str1, str2, len1-1, len2), # remove
                    edit_distance(str1, str2, len1-1, len2-1), # replace
               )



test_cases = {
                ("saturday", "sunday") : 3,
                ("cut", "cat") : 1,
                ("geek", "gesek") : 1
             }
for (str1, str2), answer in test_cases.iteritems():
    assert(edit_distance(
                         str1, str2, 
                         len(str1), len(str2)
                        ) 
            == answer)








    



