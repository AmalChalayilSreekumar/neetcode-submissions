class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        k = max(piles)

        # If the hours and number of piles are equal then the piles, then the eating speed must be the largest element
        if n == h:
            return k

        left, right= 1,k
        rate = None

        while left<right:
            rate = left + (right-left)//2
            total_hours = 0
            for pile in piles:
                total_hours+= -(pile//-rate)

            if total_hours<=h:
                right = rate
            elif total_hours>h:
                left = rate+1 

        
        return left