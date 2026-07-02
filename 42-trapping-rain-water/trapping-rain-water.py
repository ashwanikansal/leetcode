class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        suffix_max = [0] * n
        suffix_max[n-1] = height[n-1]
        
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], height[i])


        prev_max = height[0]
        total_water = 0

        for i in range(1, n-1):
            water_level = min(prev_max, suffix_max[i+1]) - height[i]

            if water_level > 0:
                total_water += water_level
            prev_max = max(prev_max, height[i])
        
        return total_water

            
        