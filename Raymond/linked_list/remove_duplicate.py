class Node(object):
	
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def __str__(self):
		print self.data

	def make_array(self,rarray):
		rarray.append(self.data)
		if self.next_node != None:
			return self.next_node.make_array(rarray)
		else:
			return rarray


def remove_duplicate(cur_node):
	initial_node = cur_node
	linked_hash = {}
	linked_hash[cur_node.data] = True
	while cur_node.next_node != None:
		if cur_node.next_node.data in linked_hash:
			cur_node.next_node = cur_node.next_node.next_node
		else:
			linked_hash[cur_node.next_node.data] = True
			cur_node = cur_node.next_node
	return initial_node


def make_node(rarray):
	node = Node(rarray[-1], None)
	rarray = rarray[:-1]
	for i in rarray[::-1]:
		node = Node(i, node)
	return node
	

a = make_node([1,1,5,6,7,2,3,3,2,2,3,4])
remove_duplicate(a)
print a.make_array([])

b = make_node([1,2,3,6,6])
remove_duplicate(b)
print b.make_array([])

b = make_node([1] * 5)
remove_duplicate(b)
print b.make_array([])
