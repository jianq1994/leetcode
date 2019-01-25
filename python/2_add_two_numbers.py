class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2: 
            return None
        head = ListNode(0)
        cur = ListNode(0)
        head.next = cur
        carry = 0
        while(l1 and l2):
            newNode = ListNode((l1.val + l2.val + carry) %10)
            carry = (l1.val + l2.val + carry) //10
            cur.next = newNode
            cur = newNode
            l1 = l1.next
            l2 = l2.next
        if l1:
            l2 = l1  
        while(l2 and carry):
            newNode = ListNode( (l2.val + carry) %10)
            carry = (l2.val + carry) //10
            cur.next = newNode
            cur = newNode
            l2 = l2.next
        if not l2 and carry:
            newNode = ListNode(carry)
            cur.next = newNode
            cur = newNode
        elif not carry and l2:
            cur.next = l2
        return head.next.next