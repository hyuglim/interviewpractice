# longest increasing subsequence for [10,22,9,33,21,50,41,60,80]
# is lenght of [10,22,33,50,60,80] == 6

def longest_increasing_subsequence(array, index):
    subproblem_indices = get_valid_indices(array, index)
    if not subproblem_indices:
        return 1
    else:
        return 1 + max([longest_increasing_subsequence(array, subproblem_index)
            for subproblem_index in subproblem_indices])


def get_valid_indices(array, i):
    tmp = [j for j in xrange(i)
            if array[j] < array[i]]
    return tmp


def solve_longest_increasing_subsequence(array):
    tmp = [longest_increasing_subsequence(array, index) for index in xrange(len(array))]
    return max(tmp)


assert(solve_longest_increasing_subsequence([10,22,9,33,21,50,41,60,80]) == len([10,22,33,50,60,80]))
