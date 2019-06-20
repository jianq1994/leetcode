from collections import deque
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed:
            return True
        push = []
        popped = deque(popped)
        pushed = deque(pushed)
        while(popped):
            ved = popped.popleft()
            if ved in push[:-1]:
                return False
            elif ved in push[-1:]:
                push.pop()
                pass
            elif pushed:
                while(pushed):
                    cur = pushed.popleft()
                    if cur != ved:
                        push.append(cur)
                    else:
                        break
        return True

            