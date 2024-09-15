# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        p1, p2 = head, head

        len_cycle = find_length_of_cycle(head)

        if len_cycle == 0:
            return None

        while len_cycle > 0:
            p2 = p2.next
            len_cycle -= 1

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1


def find_length_of_cycle(head):
    fast, slow = head, head
    cycle_length = 0

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            while True:
                slow = slow.next
                cycle_length += 1
                if slow == fast:
                    break
            return cycle_length

    return 0