class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # n, n-1, n-2, ..., 1 = O(n^2)
        # set() -> O(n)

        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        
        return False

        