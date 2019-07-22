#52~93,5

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        num,tail = 1, head
        while(tail.next):
            num += 1
            tail = tail.next
        k = num - k%num
        tail.next = head
        for i in range(k):
            head = head.next
            tail = tail.next
        tail.next = None
        return head