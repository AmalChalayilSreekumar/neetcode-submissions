class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0

        left, right = 0, len(heights)-1

        while left<right:
            best = max(min(heights[left],heights[right])*(right-left), best)

            if heights[left]>heights[right]:
                right-=1
            elif heights[right]<heights[left]:
                left+=1
            else:
                left+=1
                
        return best