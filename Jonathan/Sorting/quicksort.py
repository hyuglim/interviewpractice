# This is conventional quicksort practice


def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp


def partition(array, low, high):
    pivot_value = array[high]
    pivot_pointer = low
    for runner_pointer in xrange(low, high):
        if array[runner_pointer] <= pivot_value:
            swap(array, pivot_pointer, runner_pointer)
            pivot_pointer += 1
    swap(array, high, pivot_pointer)
    return pivot_pointer


def quicksort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)


def test_quicksort(array):
    quicksort(array, 0, len(array)-1)
    print array
    for index in xrange(len(array)-1):
        assert(array[index] <= array[index+1] )


array = [3, 4, 1, 12, 6, 5]
test_quicksort(array)
    
