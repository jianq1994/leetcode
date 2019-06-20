class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = set()
        ans = []
        for i in nums:
            if i in d:
                d.remove(i)
            else:
                d.add(i)
        return list(d)