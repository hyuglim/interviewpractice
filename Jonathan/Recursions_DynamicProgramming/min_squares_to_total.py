# find minimum number of squares that add up to n
# i.e. 100 = 25 * 4 = 10^2 * 1 : answer is 1
# a number is always a sum of squares because 1^2 = 1

# Runtime analysis
# minimum_num_squares_to_add: O(n^2)

def minimum_num_squares_to_add_solve(n):
    square_table = {x:1 for x in xrange(4)}
    square_table[0] = 0
    return minimum_num_squares_to_add(n, square_table)

def minimum_num_squares_to_add(n, square_table):
    
    if n in square_table:
        return square_table[n]
        
    seq = [1 +  
            minimum_num_squares_to_add(n - x*x, square_table) 
            for x in xrange(1, n+1) 
            if x*x <= n]
    square_table[n] = min(seq)

    return square_table[n]




assert(minimum_num_squares_to_add_solve(4) == 1)
assert(minimum_num_squares_to_add_solve(5) == 2)
assert(minimum_num_squares_to_add_solve(50) == 2)
assert(minimum_num_squares_to_add_solve(75) == 3)
assert(minimum_num_squares_to_add_solve(17) == 2)
    




