# min time to finish n tasks without skipping two consecutive tasks


def min_time(tasks, index):
    if index < 0:
        return 0

    incl = tasks[0]
    excl = 0

    for i in xrange(1, len(tasks)):
        incl_new = tasks[i] + min(incl, excl)
        excl_new = incl
        incl = incl_new
        excl = excl_new
    print incl, excl
    return min(incl, excl)


assert(min_time([10, 5, 7, 10], 3) == 12)
assert(min_time([10], 0) == 0)
assert(min_time([10, 30], 1) == 10)
