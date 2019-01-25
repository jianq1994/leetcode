class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        first = head
        second = head.next
        while(1):
            first.next = second.next
            second.next = first
            pre.next = second
            pre = first
            first = first.next
            if not first:
                return dummy.next
            if not first.next:
                return dummy.next
            second = first.next
            