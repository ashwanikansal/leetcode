class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lower = str(low)
        higher = str(high)

        n1 = len(lower)
        n2 = len(higher)
        
        res = []

        for l in range(n1, n2+1):
            for i in range(1, 9-l+2):
                s=''
                for j in range(i, i+l):
                    s=s+str(j)
                num = int(s)
                if num >= low and num <= high:
                    res.append(num)
        
        return res