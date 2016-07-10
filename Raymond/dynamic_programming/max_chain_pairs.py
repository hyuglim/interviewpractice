#You are given n pairs of numbers. In every pair, the first number is always smaller than the second number. 
#A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion. 
#Find the longest chain which can be formed from a given set of pairs.

def max_chain_pairs(rarray):
	cur_right = 0
	return_array = []
	while len(rarray) > 0:
		min_right = 9999999
		for i in rarray:
			if min_right >= i[1]:
				min_right = i[1]
				best_i = i
		return_array.append(best_i)
		cur_right = best_i[1]
		rarray = [i for i in rarray if i[0] > cur_right]
	return return_array

assert [(5, 24), (27, 40), (50, 90)] == max_chain_pairs([(5,24),(39,60),(15,28),(27,40),(50,90)])
