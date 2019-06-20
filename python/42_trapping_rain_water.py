class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left = [0] * len(height)
        right = [0] * len(height)
        left[0] = height[0]
        right[-1] = height[-1]
        for i in range(1,len(height)):
            left[i] = max(left[i-1],height[i])
            right[-i-1] = max(right[-i], height[-i-1])
        rain = 0 
        for i in range(len(height)):
            rain += min(left[i], right[i]) - height[i]
        return rain