# given number of pairs of parentheses
# return all valid pairs 

# Runtime analysis. n is 2 * num a.k.a. number of chars in string
# is_valid_pairs: O(n) 
# get_all_permutations: O(n! * n). there are n! perms, and substring takes O(n) each iter
# get_valid_parentheses: O(n! * n^2) = for each permutation, check run is_valid_pair

def get_valid_parentheses(num):
    paren_combinations = []
    get_all_permutations("", "()" * num, paren_combinations)
    return [
               paren_pair for paren_pair in paren_combinations
               if is_valid_pairs(paren_pair)
           ]



def get_all_permutations(prefix, suffix, permutations):
    if not suffix:
        permutations.append(prefix)

    for i in xrange(len(suffix)):
        get_all_permutations(
                    prefix + suffix[i],
                    suffix[:i] + suffix[i+1:],
                    permutations
                )


def is_valid_pairs(parens):
    open_paren_stack = []
    for paren in parens:
        if paren == '(':
            open_paren_stack.append(paren)
        elif paren == ')':
            if not open_paren_stack:
                return False
            else:
                open_paren_stack.pop()
        else:
            raise Exception("invalid input: need paren")
    return True


assert(is_valid_pairs([paren for paren in "()()()()()"]))
assert(not is_valid_pairs([paren for paren in ")()()()()"]))
assert(is_valid_pairs([paren for paren in "((()(())))"]))
assert(not is_valid_pairs([paren for paren in "()(()()))())"]))
    

assert(all([pair in ['((()))','(()())','(())()','()(())','()()()'] for pair in get_valid_parentheses(3)]))
