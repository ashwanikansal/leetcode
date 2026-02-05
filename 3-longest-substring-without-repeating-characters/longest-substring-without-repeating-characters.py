class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        hash_map = {}

        i=0
        for j in range(0, len(s)):
            if s[j] in hash_map.keys() and hash_map[s[j]] >= i:
                i = hash_map[s[j]] + 1
            max_len = max(max_len, j-i+1)    
            hash_map[s[j]] = j

        return max_len
        