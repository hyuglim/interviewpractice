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
