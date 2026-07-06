class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        n = len(s)
        hs = set()
        res = 0

        for j in range(n):
            
            if s[j] in hs:
                while s[i] != s[j]:
                    hs.remove(s[i])
                    i += 1
                hs.remove(s[i])
                i+=1
            
            hs.add(s[j])
            res = max(res, len(hs))
        
        return res
            





