# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        rev_head = self.reverse_single_linked_list(slow)

        basic_head = head

        while rev_head and head is not None:
            nex = head.next
            head.next = rev_head
            head = nex

            nex = rev_head.next
            rev_head.next = head
            rev_head = nex

        if head is not None:
            head.next = None

        return basic_head

    def reverse_single_linked_list(self, head):

        prev = None
        nex = None

        while head is not None:
            nex = head.next
            head.next = prev
            prev = head
            head = nex

        return prev


