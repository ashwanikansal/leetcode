class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums = sorted(nums)
        result = []
        for first in range(0, n-2):
            if first > 0 and nums[first-1] == nums[first]:
                continue
            target = 0 - nums[first]
            left, right = first + 1, n-1

            while(left < right):
                total = nums[left] + nums[right]
                if total == target:
                    result.append([nums[first], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        
        return result