class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * (n+1)
        for num in nums:
            count[num] += 1
        ans = []
        for i,c in enumerate(count):
            if c == 2:
                ans.append(i)
        return ans