# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    '''https://leetcode.com/problems/swap-nodes-in-pairs/'''
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = ListNode(0)
        p.next = head
        point = p
        while point.next and point.next.next:
            temp = point.next.next
            point.next.next = temp.next
            temp.next = point.next
            point.next = temp
            point = temp.next
        return p.next
