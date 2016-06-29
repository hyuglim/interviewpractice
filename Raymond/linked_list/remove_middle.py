#remove an element in the array with only access to one of the elements
#runtime is O(1)

class Node(object):
	def __init__(self, value=None, next_node=None):
		self.value = value
		self.next_node = next_node
	def __str__(self):
		print self.value

	def make_array(self,rarray):
		rarray.append(self.value)
		if self.next_node != None:
			return self.next_node.make_array(rarray)
		else:
			return rarray

def make_node(rarray):
	node = Node(rarray[-1], None)
	rarray = rarray[:-1]
	for i in rarray[::-1]:
		node = Node(i, node)
	return node
	
def remove_middle(remove_node):
	remove_node.value = remove_node.next_node.value
	remove_node.next_node = remove_node.next_node.next_node

a = make_node([1,2,3,4,5])

remove_middle(a.next_node.next_node.next_node)
print a.make_array([])

