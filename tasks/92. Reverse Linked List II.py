"""

Given the head of a singly linked list and two integers left and right where left <= right, reverse
the nodes of the list from position left to position right, and return the reversed list.

The number of nodes in the list is n.
4 <= n <= 500
-500 <= Node.val <= 500
3 <= left < right <= n

"""
from random import randrange

left = 4
right = 5


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# head = Node(randrange(0, 1000) - 500)
head = Node(1)
current_node = head
for i in range(2, 10):
    new_node = Node(i)
    if i == left:
        left = current_node
    elif i == right:
        right = new_node
    current_node.next = new_node
    current_node = new_node

current_node = left.next
left.next = right
left = current_node
current_node = current_node.next
left.next = right.next
right.next = None
right = current_node.next

while current_node:
    if right:
        current_node.next = left
        left = current_node
        current_node = right
        right = right.next
    else:
        current_node.next = left
        left = current_node
        current_node = None

current_node = head
while current_node:
    print(current_node.val)
    current_node = current_node.next
