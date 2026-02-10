class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            s = set()
            odd = 0
            even = 0
            for j in range(i, n):
                is_even = True if nums[j] % 2 == 0 else False
                if nums[j] not in s:
                    if is_even:
                        even += 1
                    else:
                        odd += 1

                if odd == even:
                    res = max(res, j-i+1)
                s.add(nums[j])
        
        return res
                