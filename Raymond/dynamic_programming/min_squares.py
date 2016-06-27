import math

mem_hash = {}
def min_squares(n):	
	if n in mem_hash:
		return mem_hash[n]
	if n == int(math.sqrt(n)) ** 2:
		return 1
	if n == 2 or n == 3:
		return 2
	else:
		val = min([min_squares(i) + min_squares(n-i) for i in xrange(1,n/2+1)])
		mem_hash[n] = val
		print mem_hash
		return val

print min_squares(510)

#runtime is n^2
