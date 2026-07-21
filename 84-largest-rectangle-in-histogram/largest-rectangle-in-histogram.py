class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = [] # (index, element)
        maxArea = 0

        for i in range(n):
            newInd = i
            while stk and stk[-1][1] > heights[i]:
                ind, h = stk.pop()
                maxArea = max(maxArea, h * (i - ind))
                newInd = ind
            
            stk.append((newInd, heights[i]))
            # print(stk, maxArea)
        
        while stk:
            ind, h = stk.pop()
            maxArea = max(maxArea, h * (n-ind))
        
        return maxArea
        