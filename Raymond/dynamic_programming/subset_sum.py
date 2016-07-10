def subset_sum(rarray, sum_set):
	if sum_set == 0:
		return True
	else:
		bool_array = []
		for i in rarray:
			copy = rarray[:]
			copy.remove(i)
			bool_array.append(subset_sum(copy, sum_set - i))
		return any(bool_array)

print subset_sum([11,32,38,2,3,4,12,43], 9)


#runtime with memoization is O(len(rarray)^2 * sum_set)
