class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        suffix_max = [0] * (n+1)

        for i in range(n-1, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], prices[i])
        
        maxprofit = 0
        
        for i in range(n):
            if suffix_max[i+1] > prices[i]:
                maxprofit = max(maxprofit, suffix_max[i+1] - prices[i])
        
        return maxprofit
            