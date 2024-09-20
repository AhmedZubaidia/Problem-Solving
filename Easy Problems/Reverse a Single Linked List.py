# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        nex = None

        while head != None:
            nex = head.next
            head.next = prev
            prev = head
            head = nex

        head = prev

        return head
