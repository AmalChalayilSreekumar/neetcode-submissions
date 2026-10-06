class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)-1

        right = n
        left = 0
        best = 0
        while left<right:
            temp = min(height[left],height[right])*(right-left)

            if temp>best:
                best = temp

            if height[left]>height[right]:
                right-=1            
            else:
                left+=1
        return best