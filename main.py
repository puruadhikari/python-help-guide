class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)
node.next.next.next.next = ListNode(5)

fast = node
slow = node
k = 3

counter = 0
while counter < k - 1:
    fast = fast.next
    counter += 1

while fast:
    slow = slow.next
    fast = fast.next
    prev = slow

temp = slow.next
prev.next = temp
temp.next = None

while prev:
    print(prev.val)
    prev = prev.next


