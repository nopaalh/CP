# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        hasil = ListNode()
        mandor = hasil
        while list1 and list2:
            if list1.val < list2.val:
                mandor.next = list1
                list1 = list1.next
            else:
                mandor.next = list2
                list2 = list2.next
            mandor = mandor.next

        mandor.next = list1 if list1 else list2

        return hasil.next