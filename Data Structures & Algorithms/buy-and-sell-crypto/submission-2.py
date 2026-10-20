class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<=1:
            return 0
    
        left, right = 0, 1

        best = 0
        while right<n:
            if prices[left]>prices[right]:
                left = right
            else:
                best = max(best, prices[right]-prices[left])
            right+=1

        return best