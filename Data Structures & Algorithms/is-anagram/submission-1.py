class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sDict = dict.fromkeys(s,0)
        tDict = dict.fromkeys(t,0)

        for i in s:
            if i in sDict:
                sDict[i]+=1
            
        for i in t:
            if i in tDict:
                tDict[i]+=1
        
        return sDict == tDict