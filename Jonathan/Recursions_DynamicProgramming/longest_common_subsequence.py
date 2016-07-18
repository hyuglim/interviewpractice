
def longest_common_subsequence_naive(string_one, string_two):
    print string_one, string_two
    
    if string_one == string_two:
        return len(string_one)
    if not string_one or not string_two:
        return 0

    longest = 0
    for i in xrange(len(string_one)):
        subresult = longest_common_subsequence(string_one[:i] + string_one[i+1:], string_two)
        if subresult > longest:
            longest = subresult
    
    for i in xrange(len(string_two)):
        subresult = longest_common_subsequence_naive(string_one, string_two[:i] + string_two[i+1:])
        if subresult > longest:
            longest = subresult

    return longest


def longest_common_subsequence_bottom_up(string_one, string_two):
    len_one = len(string_one)
    len_two = len(string_two)
    lcs_subproblems = [[None] * (len_two+1) for i in xrange(len_one+1)] # lcs_subproblems[i][j] has length of lcs of string_one[0:i-1] and string_two[0:j-1]

    for i in xrange(len_one+1):
        for j in xrange(len_two+1):
            if i == 0 or j == 0:
                lcs_subproblems[i][j] = 0
            elif string_one[i-1] == string_two[j-1]:
                lcs_subproblems[i][j] = lcs_subproblems[i-1][j-1] + 1
            else:
                lcs_subproblems[i][j] = max(lcs_subproblems[i-1][j], lcs_subproblems[i][j-1])
    return lcs_subproblems[len_one][len_two]



# assert(longest_common_subsequence_naive('ABC', 'AEC') == 2)
assert(longest_common_subsequence_bottom_up('ABCDGH', 'AEDFHR') == 3)
assert(longest_common_subsequence_bottom_up('AGGTAB', 'GXTXAYB') == 4)

        



