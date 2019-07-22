#86,73

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        if not head.next.next:
            if head.val < head.next.val:
                return head
            else:
                head.next.next = head
                head = head.next
                head.next.next = None
                return head
        p0 = head
        p1 = head
        while(p1 and p1.next):
            p0 = p0.next
            p1 = p1.next.next
        p1 = p0.next
        p0.next = None
        headA = self.sortList(head)
        headB = self.sortList(p1)
        dummy = ListNode(0)
        p0 = dummy
        while(headA and headB):
            if headA.val < headB.val:
                p0.next = headA
                p0 = headA
                headA = headA.next
            else:
                p0.next = headB
                p0 = headB
                headB = headB.next
        if not headA:
            p0.next = headB
        else:
            p0.next = headA
        return dummy.next