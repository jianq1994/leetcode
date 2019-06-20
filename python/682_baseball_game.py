class Solution:
    def calPoints(self, ops: List[str]) -> int:
        valid = []
        for op in ops:
            if op == 'C':
                valid.pop()
            elif op == 'D':
                valid.append(2*valid[-1])
            elif op == '+':
                valid.append(valid[-1]+valid[-2])
            else:
                valid.append(int(op))
        return sum(valid)