class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        stack = []
        current = head

        while current:
            if current.child:
                if current.next:
                    stack.append(current.next)  # Save the next node
                current.next = current.child  # Connect child to next
                current.next.prev = current
                current.child = None  # Remove child reference

            if not current.next and stack:
                current.next = stack.pop()  # Get next from stack
                current.next.prev = current

            current = current.next  # Move forward

        return head
