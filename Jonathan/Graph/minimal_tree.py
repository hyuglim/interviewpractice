# Given a sorted array with unique integer elements, make a binary search tree with minimal weight

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 0, 1, 2, 3, 4, 5, 6, 7, 8
#             4
#    1              6
# 0     2        5     7
#          3              8

def minimal_binary_tree(sorted_array, middle_node, left_end, right_end):
    middle_index = (left_end + right_end) / 2 
    middle_node = Node(sorted_array[middle_index])
    print 'm', middle_index
    
    if right_end - left_end == 1:
        middle_node.right = Node(sorted_array[right_end])
        print 'r', right_end
        return
    left_middle = (left_end + middle_index) / 2
    right_middle = (right_end + middle_index + 1 ) / 2 

    # print left_end, right_end, left_index, middle_index, right_index
    
    if left_middle != middle_index:
        left_node = Node(sorted_array[left_middle])
        minimal_binary_tree(sorted_array, left_node, left_end, middle_index-1)
    
    if right_middle != middle_index:
        right_node = Node(sorted_array[right_middle])
        minimal_binary_tree(sorted_array, right_node, middle_index+1, right_end)


def traverse_tree(root):
    if root.left:
        assert(root.left.data <= root.data)
        traverse_tree(root.left)
    if root.right:
        assert(root.data <= root.right.data)
        traverse_tree(root.right)


def test_minimal_binary_tree(sorted_array):
    middle_index = len(sorted_array) / 2
    middle_node = Node(sorted_array[middle_index])
    minimal_binary_tree(sorted_array, middle_node, 0, len(sorted_array)-1)
    

print 'foo'
# test_minimal_binary_tree(range(9))
test_minimal_binary_tree(range(10))

