class Solution:
    def trap(self, height: List[int]) -> int:
        trapped = 0

        left = 0
        stored = []
        for right in range(1, len(height)):
            if height[left] <= height[right]:
                while stored:
                    trapped += height[left] - stored.pop()
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
                while stored:
                    trapped += h[left] - stored.pop()
                stored = []
                left = right
            else:
                stored.append(h[right])

        return trapped

