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
        