class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = sum([x for x in range(1,n*2,2)])
        sumEven = sum([x for x in range(2,n*2+1, 2)])

        while sumEven != 0:
            sumOdd, sumEven = sumEven, sumOdd % sumEven
        
        return sumOdd
        