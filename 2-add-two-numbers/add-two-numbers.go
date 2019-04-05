/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers_1(l1 *ListNode, l2 *ListNode) *ListNode {
    head := &ListNode{0, nil}
    current := head
    carry := 0
    for l1 != nil || l2 != nil || carry > 0 {
        sum := carry
        if l1 != nil {
            sum += l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            sum += l2.Val
            l2 = l2.Next
        }
        carry = sum / 10
        current.Next = new(ListNode)
        current.Next.Val = sum % 10
        current = current.Next
    }
    return head.Next
}


func addTwoNumbers_2(l1 *ListNode, l2 *ListNode) *ListNode {
    carry := 0
    head := new(ListNode)
    cur := head
    for l1 != nil || l2 != nil || carry != 0 {
        n1, n2 := 0, 0
        if l1 != nil {
            n1, l1 = l1.Val, l1.Next
        }
        if l2 != nil {
            n2, l2 = l2.Val, l2.Next
        }
        num := n1 + n2 + carry
        carry = num / 10
        cur.Next = &ListNode{Val:num%10, Next:nil}
        cur = cur.Next
    }
    return head.Next
}