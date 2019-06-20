class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums:
            return []
        H = len(nums)
        L = len(nums[0])
        if H*L != r*c:
            return nums
        ans = []
        for i in range(r):
            rowi = []
            for j in range(c):
                rowi.append(nums[(i*c+j)//L][(i*c+j)%L])
            ans.append(rowi)
        return ans
                