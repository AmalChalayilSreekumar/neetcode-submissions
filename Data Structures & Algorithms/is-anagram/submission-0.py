class Solution:
    def isAnagram(self,s: str, t: str) -> bool:
        n= len(s)
        if n!=len(t): return False

        sDict = dict.fromkeys(s,0)
        tDict = dict.fromkeys(t,0)

        for i in range(0, n):
            sDict[s[i]]+=1
            tDict[t[i]]+=1


        for i in sDict:
            if i not in tDict or tDict[i]!=sDict[i]:
                return False


        return True