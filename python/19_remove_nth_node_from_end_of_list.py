#99,5
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or not n:
            return None
        second = head
        for i in range(n):
            if second == None:
                return head
            second = second.next
        dummy = ListNode(0)
        dummy.next = head
        prefirst = dummy
        first = head
        while(second):
            prefirst = prefirst.next
            first = first.next
            second = second.next
        prefirst.next = first.next
        return dummy.next


#55,5

# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         if not head:
#             return head
#         dummy = ListNode(0)
#         dummy.next = head
#         p0,p1,p2 = dummy, head, head
#         for i in range(n):
#             p2 = p2.next
#         while(p2):
#             p0 = p0.next
#             p1 = p1.next
#             p2 = p2.next
#         p0.next = p1.next
#         return dummy.next
        