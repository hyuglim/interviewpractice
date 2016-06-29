#runtime is O(n)

class Node(object):
	def __init__(self, value=None, next_node=None):
		self.value = value
		self.next_node = next_node


def kth_to_last_element(node, k):
	first_pointer_counter = 0
	first_pointer = node
	second_pointer = node
	while first_pointer_counter < k-1:
		if first_pointer.next_node == None:
			return "Not Found"
		first_pointer = first_pointer.next_node
		first_pointer_counter += 1
	
	while first_pointer.next_node != None:
		first_pointer = first_pointer.next_node
		second_pointer = second_pointer.next_node
	return second_pointer.value


def make_node(rarray):
	node = Node(rarray[-1], None)
	rarray = rarray[:-1]
	for i in rarray[::-1]:
		node = Node(i, node)
	return node
	
a = make_node([1,2,3,4,5,6,7])
print kth_to_last_element(a,3)

