class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        # if i pre-compute the suffix prod into an array
        suffix_product = [0]*n

        suffix_product[n-1] = nums[n-1] 
        
        for i in range(n-2, -1, -1):
            suffix_product[i] = suffix_product[i+1] * nums[i]

        # 24, 24, 12, 4
        # prefx = 6
        # 24, 12, 8, 


        prefix_product = 1
        for i in range(n-1):
            suffix_product[i] = prefix_product * suffix_product[i+1]
            prefix_product *= nums[i] 
        
        suffix_product[n-1] = prefix_product

        return suffix_product


        