class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            flag = 0
            for j in nums2[nums2.index(i):]:
                if j > i:
                    flag = 1
                    ans.append(j)
                    break
            if not flag:
                ans.append(-1)
        return ans