# class Solution:
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         if not nums:
#             return -1
#         l = 0
#         r = len(nums)-1
#         while(l<=r):
#             m = (l+r)//2
#             if nums[m] == target:
#                 return m
#             if nums[l] <= nums[m]:
#                 if nums[m] < target or nums[l] > target:
#                     l = m+1
#                 else:
#                     r = m-1
#             else:
#                 if nums[m] < target and nums[l] > target:
#                     l = m+1
#                 else:
#                     r = m-1
#         return -1



class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        l,r = 0, len(nums)-1
        while(l<r):
            m = (l+r)//2
            if(nums[m] >= nums[0] > target):
                l = m+1
            elif(nums[m] > target > nums[0]):
                r = m
            elif(target > nums[m] >= nums[0]):
                l = m+1
            elif(nums[0] > nums[m] > target):
                r = m
            elif(nums[0] > target > nums[m]):
                l = m+1
            else:
                r = m
        return l if nums[l] == target else -1
                