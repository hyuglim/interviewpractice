# remove node in the middle given only access to that node
# Runtime analysis: remove middle node O(n)

class Node:
    def __init__(self, data):
        self.next_node = None
        self.data = data


    def add_to_tail(self, data):
        current = self
        while current.next_node is not None:
            current = self.next_node
        current.next_node = Node(data) 
        return current.next_node
        

    def print_linked_list(self):
        current = self
        while current is not None:
            print current.data
            current = current.next_node


def make_linked_list(data):
    head = Node(data[0])
    current = head
    for datum in data[1:]:
        current = current.add_to_tail(datum)
    return head


def remove_middle_node(node):
    if node.next_node:
        node.data = node.next_node.data
        node.next_node = node.next_node.next_node
    else:
        raise Exception("Does not work for the last node")


def test_remove_middle_node(num_elements):
    head = make_linked_list(range(1, num_elements+1))
    current = head
    while current.data != num_elements / 2:
        current = current.next_node
    remove_middle_node(current)

    current = head
    while current is not None:
        if current.data == num_elements / 2:
            return False
        current = current.next_node
    return True
    

assert(test_remove_middle_node(5))       
assert(test_remove_middle_node(2))       
assert(test_remove_middle_node(8))       
assert(test_remove_middle_node(10))       
    
