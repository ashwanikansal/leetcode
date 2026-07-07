class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashtable = [0]*26
        maxFreq = 0
        maxLen = 0
        i=0

        for j in range(len(s)):
            hashtable[ord(s[j])-ord('A')] += 1
            maxFreq = max(hashtable)

            while j-i+1-maxFreq > k:
                hashtable[ord(s[i]) - ord('A')] -= 1
                maxFreq = max(hashtable)
                i+=1

            maxLen = max(maxLen, j-i+1)

        return maxLen  