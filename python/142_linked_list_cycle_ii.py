#13~98,77

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        p0 = head.next 
        p1 = head.next.next
        while(p0 and p1 and p1.next and p0 != p1):
            p0 = p0.next
            p1 = p1.next.next
        if not p0 or not p1 or not p1.next:
            return None
        p0 = head
        while(p0 != p1):
            p0 = p0.next
            p1 = p1.next
        return p0