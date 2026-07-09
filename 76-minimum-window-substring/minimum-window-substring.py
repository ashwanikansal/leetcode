class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)

        thash = {}

        if n1 < n2:
            return ""

        for c in t:
            thash[c] = thash.get(c,0) + 1
        
        left=0
        start_ind = -1
        min_len = n1
        cnt = 0

        for right in range(n1):
            
            ch = s[right]
            if ch in thash and thash[ch] > 0:
                cnt += 1
            thash[ch] = thash.get(ch,0) - 1
            
            while cnt == n2:
                if right-left+1 <= min_len:
                    min_len = right - left + 1
                    start_ind = left
                if thash[s[left]] >= 0:
                    cnt -= 1
                thash[s[left]] = thash[s[left]] + 1
                left += 1
        
        return "" if start_ind==-1 else s[start_ind: start_ind + min_len]

            # 



            
        

        
