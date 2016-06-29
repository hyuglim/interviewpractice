# check a linked list is a palindrome
# Runtime analysis: O(n)


from node import Node
from node import make_linked_list

def is_palindrome(head):
    string = get_string_in_list(head)
    return string == string[::-1]


def get_string_in_list(head):
    str_builder = []
    current = head
    while current is not None:
        str_builder.append(current.data)
        current = current.next_node
    return ''.join(str_builder)


def test_is_palindrome(data):
    return is_palindrome(make_linked_list(data))


assert(not test_is_palindrome(list("apple")))
assert(test_is_palindrome(list("abcba")))
assert(not test_is_palindrome(list("banana")))
assert(test_is_palindrome(list("hellolleh")))

