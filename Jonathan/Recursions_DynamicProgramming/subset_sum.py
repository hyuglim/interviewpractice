# given a set, determine if there is a subset with sum equal to a given int

# Runtime analysis
# subset_sum: n^n per each call => O(n) for copy for n iterations in for loop
#             2^n recursion calls
#             O(2^n * n^2)

def subset_sum(subset, total):
    if total == 0:
        return True
    
    results = []
    for num in subset:
        new_set = subset.copy()
        new_set.remove(num)
        results.append(subset_sum(new_set, total - num))

    return any(results)


assert(subset_sum(set([1,2,5,6,4,64,9]), 69))
assert(subset_sum(set([1,2,5,6,4,64,9]), 0))
assert(subset_sum(set([1,2,5,6,4,64,9]), 3))
assert(subset_sum(set([1,2,5,6,4,64,9]), 15))
assert(not subset_sum(set([1,2,5,6,4,64,9]), 1000))
