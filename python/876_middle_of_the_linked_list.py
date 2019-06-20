# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return head
        fast = head
        slow = head
        while(fast):
            if fast.next:
                fast = fast.next.next
            else:
                fast = None
                return slow
            slow = slow.next
        return slow