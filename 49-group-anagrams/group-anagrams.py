class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}

        for s in strs:
            key = tuple(sorted(s))
            anagrams.setdefault(key, []).append(s)

        return list(anagrams.values())
        