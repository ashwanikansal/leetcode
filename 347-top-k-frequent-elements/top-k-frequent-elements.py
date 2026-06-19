class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1 -> 3, 2 -> 2, 3 -> 1
        dictionary = {}
        for n in nums:
            dictionary[n] = dictionary.get(n, 0) + 1
        
        # print(dictionary.items())
        ans = []
        for ky, v in sorted(dictionary.items(), key=lambda items : items[1], reverse = True):
            if k>0:
                ans.append(ky)
                k -= 1

        return ans
        