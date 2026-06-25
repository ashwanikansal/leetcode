class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        ans, curr = 1, 1
        prev_dig = sorted_nums[0]

        for i in range(1, len(nums)):
            if sorted_nums[i] == prev_dig + 1:
                curr += 1
            elif sorted_nums[i] == prev_dig:
                continue
            else:
                curr = 1

            prev_dig = sorted_nums[i]
            ans = max(ans, curr)
        
        return ans