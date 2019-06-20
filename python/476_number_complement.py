class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        digit = 0
        while(num):
            if num%2 == 0:
                ans += 2**digit
            digit += 1
            num = num//2
        return ans