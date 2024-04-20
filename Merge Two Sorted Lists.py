# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        head = dummy

        while list1 and list2 :
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next

            else:
                head.next = list2
                list2= list2.next

            head =head.next

        if not list1:
            head.next = list2

        elif not list2 :
             head.next = list1  

        return dummy.next        

       
   
