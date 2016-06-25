def edit_distance(str1, str2):
	if len(str1) == 0:
		return len(str2)
	elif len(str2) == 0:
		return len(str1)
	elif len(str1) == len(str2):
		return numDiffs(str1,str2)
	elif len(str1) > len(str2):
		rarray = []
		for i in xrange(len(str1)):
			rarray.append(edit_distance(str1[:i] + str1[i+1:], str2))
		return min(rarray) + 1
	else:
		rarray = []
		for i in xrange(len(str2)):
			rarray.append(edit_distance(str1, str2[:i] + str2[i+1:]))
		return min(rarray) + 1


def numDiffs(str1, str2):
	counter = 0
	for i in xrange(len(str1)):
		if str1[i] != str2[i]:
			counter += 1
	return counter


print edit_distance('a','b')
print edit_distance('a','ba')
print edit_distance('abacdpl','cdf')

test_cases = {
                ("saturday", "sunday") : 3,
                ("cut", "cat") : 1,
                ("geek", "gesek") : 1
             }
for (str1, str2), answer in test_cases.iteritems():
    assert(edit_distance(
                         str1, str2) 
            == answer)

