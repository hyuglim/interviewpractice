# Given n pairs of numbers, first is smaller than the second
# (a,b) : a < b. 
# chain can be formed (a, b) (c, d), if b < c
# find the longest chain from a set of pairs
#
# Runtime analysis: remove_overlapping => O(n)
#                   max_length_chain =>O(n)
#                   Overall => O(n^2)

def is_overlapping(test_range, reference_range):
    return test_range[0] < reference_range[1]


def max_length_chain(pair_set):
    pair_sequence = sorted(pair_set, key=lambda pair: pair[1])
    chain_length = 0
    while pair_sequence:
        earliest_finish_pair = pair_sequence.pop(0)
        chain_length += 1

        pair_sequence = remove_overlapping(pair_sequence, earliest_finish_pair)
    return chain_length


def remove_overlapping(pair_sequence, reference_range):
    return [pair for pair in pair_sequence if not is_overlapping(pair, reference_range)]
        

set_pairs = [(5, 24), (15, 28), (27, 40), (39, 60), (50, 90) ]
assert(max_length_chain(set_pairs) == 3)
