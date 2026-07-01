class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left , right = 0 , n-1
        max_water = 0

        while (left<right):
            curr_water = (right-left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            max_water = max(max_water, curr_water)
        return max_water
        