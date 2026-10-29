class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = dict.fromkeys(s,0)

        n=len(s)

        left,right = 0,0


        charMap[s[left]]+=1
        max_freq  = 1


        while right<n-1:
            right+=1
            length = right-left+1 

            charMap[s[right]] += 1
            
            if charMap[s[right]]>max_freq:
                max_freq = charMap[s[right]]

            otChars = length-max_freq

            if otChars > k:
                charMap[s[left]]-=1
                left+=1


        return right-left + 1

            
            


            