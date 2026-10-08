class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0

        # Pass 1: left to right
        left = 0
        stored = []
        for right in range(1, len(height)):
            if height[left] <= height[right]:
                for v in stored:
                    trapped += height[left] - v
                stored = []
                left = right
            else:
                stored.append(height[right])
        peak = left

        h = height[peak:][::-1]
        left = 0
        stored = []
        for right in range(1, len(h)):
            if h[left] <= h[right]:
                for v in stored:
                    trapped += h[left] - v
                stored = []
                left = right
            else:
                stored.append(h[right])

        return trapped

