class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while(l<r):
            m = (l+r)//2
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            elif nums[m] == nums[m-1]:
                if (r-l+1)%4 == 1:
                    r = m-2
                else:
                    l = m+1
            else:
                if (r-l+1)%4 == 1:
                    l = m+2
                else:
                    r = m-1
        return nums[r]
            