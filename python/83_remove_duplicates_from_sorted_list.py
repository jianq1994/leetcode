#62~85,5

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        dummy = ListNode(0)
        dummy.next = head
        p0 = dummy
        while(1):
            if not p0.next:
                return dummy.next
            while(p0.next.next and p0.next.val == p0.next.next.val):
                p0.next.next = p0.next.next.next
            p0 = p0.next
