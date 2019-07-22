#87~93,55~76

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """        
        p1, p2 = headA, headB
        while(p1 and p2):
            p1 = p1.next
            p2 = p2.next
        if not p1:
            p1 = headB
        else:
            p2 = headA
        while(p1 and p2):
            p1 = p1.next
            p2 = p2.next
        if not p1:
            p1 = headB
        else:
            p2 = headA
        while(p1 and p2 and p1!=p2):
            p1 = p1.next
            p2 = p2.next
        if p1 == p2:
            return p1
        return None