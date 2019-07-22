#98,5

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p0,p1,p2 = dummy,head,head.next
        for i in range(n-1):
            if i<m-1:
                p0,p1,p2 = p0.next,p1.next,p2.next
            else:
                p1.next = p2.next
                p2.next = p0.next
                p0.next = p2
                p2 = p1.next
        return dummy.next