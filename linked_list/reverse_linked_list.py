"""
given a linked list, print it in reverse order
1 -> 2 -> 3 -> 4
1 <- 2 <- 3 <- 4
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

sll = ListNode(1)
sll.next = ListNode(2)
sll.next.next = ListNode(2)
sll.next.next.next = ListNode(1)

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

rev_list = reverse_linked_list(sll)

while rev_list:
    print(rev_list.val)
    rev_list = rev_list.next

