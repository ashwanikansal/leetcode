class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # frequency will be same for every digit.
        hash_list1 = [0]*26
        hash_list2 = [0]*26

        for ch in s:
            hash_list1[ord(ch) - ord('a')] += 1
        
        for ch in t:
            hash_list2[ord(ch) - ord('a')] += 1

        for i in range(25):
            if hash_list1[i] != hash_list2[i]:
                return False

        return True
        

        