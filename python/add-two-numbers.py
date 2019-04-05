# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return
        dummy = ListNode(0); p = dummy
        
        flag = 0
        while l1 and l2:
            val = l1.val + l2.val + flag
            p.next = ListNode(val % 10)
            flag = val / 10
            
            l1 = l1.next
            l2 = l2.next
            p = p.next
        
        item = l1 or l2

        while item:
            val =  item.val + flag
            p.next = ListNode(val % 10)
            flag = val / 10
            item = item.next
            p = p.next
 
        if flag:
            p.next = ListNode(flag)
        return dummy.next
            
