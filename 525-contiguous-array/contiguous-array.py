class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans  = 0
        m = defaultdict(int)
        m[0] = -1
        curr_sum = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                curr_sum -= 1
            else:
                curr_sum += 1
            if curr_sum in m:
                ans = max(ans, i-m[curr_sum])
            else:
                m[curr_sum] = i
        
        return ans

                