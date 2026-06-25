class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        longest = 0
        for x in hs:
            if (x-1) not in hs:
                length = 1
                while (x + length) in hs:
                    length += 1
                longest = max(length, longest)
        return longest