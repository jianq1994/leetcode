#41,5

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head:
#             return head
        
#         def reversewithtail(head):
#             if not head.next:
#                 return head,head
#             newhead, tail = reversewithtail(head.next)
#             tail.next = head
#             head.next = None
#             return newhead, head
        
#         head, tail = reversewithtail(head)
#         return head
            
#92,27

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p0 = None
        p1 = head
        p2 = head.next
        while(p2):
            p1.next = p0
            p0 = p1
            p1 = p2
            p2 = p2.next
        p1.next = p0
        return p1