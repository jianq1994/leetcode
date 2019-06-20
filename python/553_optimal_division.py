class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if not nums:
            return ''
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        strnums = [str(num) for num in nums]
        return strnums[0]+'/('+ '/'.join(strnums[1:]) + ')'