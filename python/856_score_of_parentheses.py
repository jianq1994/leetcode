from collections import deque

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = deque()
        for s in S:
            if s == '(':
                stack.append(s)
            else:
                p = stack.pop()
                if p == '(':
                    stack.append(1)
                else:
                    num = 0
                    while(p != '('):
                        num += p
                        p = stack.pop()
                    stack.append(2*num)
        return sum(stack)