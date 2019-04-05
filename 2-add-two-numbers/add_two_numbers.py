# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0
        r = p = ListNode(0)
        while l1 or l2:
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            p.next = ListNode(sum%10)
            sum = int(sum/10)
            p = p.next
            
            if sum:
                p.next = ListNode(sum)
        # 此写法也可
        # if sum:
        #     p.next = ListNode(sum)
            
        return r.next