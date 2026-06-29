class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n-1):
            diff = target - numbers[i]
            l,h = i+1, n-1
            while l<=h:
                m = l+(h-l)//2
                digit = numbers[m]
                if digit == diff:
                    return [i+1, m+1]
                if digit > diff:
                    h = m-1
                else:
                    l = m+1
        
        return []
        