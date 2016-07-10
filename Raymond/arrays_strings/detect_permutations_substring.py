def detect_permutations_substring(substring1, substring2):
	substring_dict = {}
	for i in substring1:
		if i in substring_dict:
			substring_dict[i] += 1
		else:
			substring_dict[i] = 1
	print substring_dict
	for j in substring2:
		if j in substring_dict:
			substring_dict[j] -= 1
			if substring_dict[j] == 0:
				del substring_dict[j]
		else:
			return False
	return not substring_dict

print not detect_permutations_substring("aa","bb")
print not detect_permutations_substring("aa","")
print not detect_permutations_substring("","sdf")
print detect_permutations_substring("racecar","rraccea")
print detect_permutations_substring("jocn  asc","  sanoccj")

