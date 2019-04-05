/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int sum=0;
        ListNode p = new ListNode(0);
        ListNode r = p;
        
        while(l1!=null || l2!=null){
            if(l1!=null){
                sum+=l1.val;
                l1 = l1.next;
            }
            if(l2!=null){
                sum+=l2.val;
                l2 = l2.next;
            }
            p.next = new ListNode(sum %10);
            sum = sum /10;
            p = p.next;
        }
        if(sum==1){
             p.next = new ListNode(sum);
        }
        return r.next;
        
    }
}