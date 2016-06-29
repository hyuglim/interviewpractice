#in place partition where given value k
#all elements of linked list less than k have index less than
#all elements greater or equal to k
#runtime O(n)

import Node as node_file

def partition(start_node, k):
	pivot_node = start_node
	iter_node = start_node
	while iter_node != None:
		if iter_node.value < k:
			temp = iter_node.value
			iter_node.value = pivot_node.value
			pivot_node.value = temp
			iter_node = iter_node.next_node
			pivot_node = pivot_node.next_node
		else:
			iter_node = iter_node.next_node


a = node_file.Node.make_node([5,7,6,3,4,6,9,1,0,20,2])
partition(a, 5)
print a.make_array([])
