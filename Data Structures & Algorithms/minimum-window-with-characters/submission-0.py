class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        def idx(c):
            a = ord(c)
            if 65<=a<=90:
                return a-39
            else:
                return a-97

        tCount = [0] * 52
        for c in t:
            tCount[idx(c)] += 1

        missing = len(t)              
        best_len, best_start = float('inf'), 0
        left = 0

        for right in range(len(s)):
            r = idx(s[right])
            if tCount[r] > 0:         
                missing -= 1
            tCount[r] -= 1            

            while missing == 0:       
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                l = idx(s[left])
                tCount[l] += 1        
                if tCount[l] > 0:     
                    missing += 1
                left += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]