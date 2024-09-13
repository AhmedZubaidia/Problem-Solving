class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Solution:
    def hasCycle(self, head):

        slow = head
        fast = head

        while fast is not None and fast.next is not None:

            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False
