class Solution:
    def __init__(self):
        self.memo = []
    def fizzBuzz(self, n: int) -> List[str]:
        L = len(self.memo)
        if (n <= L):
            pass
        else:
            for i in range(L+1,n+1):
                if i%3 == 0 and i%5 == 0:
                    self.memo.append('FizzBuzz')
                elif i%3 == 0:
                    self.memo.append('Fizz')
                elif i%5 == 0:
                    self.memo.append('Buzz')
                else:
                    self.memo.append(str(i))
        return self.memo[:n]