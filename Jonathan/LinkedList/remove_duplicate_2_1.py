import pdb

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


def to_array(head):
    current = head 
    elements = []
    while current is not None:
        elements.append(current.data)
        current = current.next_node
    return elements



# remove duplicates from unsorted linked list

def remove_duplicate(head):
    visited = {}
    current = head
    previous = None
    while current is not None:
        if current.data in visited:
            previous.next_node = current.next_node
        else:
            visited[current.data] = True
            previous = current
        current = current.next_node


def make_linked_list(data):
    head = Node(data[0])
    current = head
    for datum in data[1:]:
        current = current.add_to_tail(datum)
    return head

        
def test_remove_duplicate(data):
    head = make_linked_list(data)
    remove_duplicate(head)
    unique_array = to_array(head)
    print unique_array
    assert(len(unique_array) == len(set(unique_array)))

    
#test_remove_duplicate(range(5))
test_remove_duplicate([0, 0])
test_remove_duplicate([0, 0, 0])
test_remove_duplicate([1, 2, 2, 3])
test_remove_duplicate([1, 2, 3, 4, 4])
