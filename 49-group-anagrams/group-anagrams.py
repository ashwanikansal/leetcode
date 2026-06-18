class Solution:
    def createKey(self, s):
        hasharray = [0]*26
        for ch in s:
            hasharray[ord(ch)-ord('a')] += 1
        return tuple(hasharray)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # 2 words are anagram or not?
        # length should be same
        # freq of each character should be same in both word.

        dictionary = {} # keys: "0104010... 26length" : value: [strings]
        
        for string in strs:
            key = self.createKey(string)
            dictionary.setdefault(key, []).append(string)
        
        print(dictionary)
        
        res = []
        
        for k in dictionary:
            res.append(dictionary[k])

        return res


        