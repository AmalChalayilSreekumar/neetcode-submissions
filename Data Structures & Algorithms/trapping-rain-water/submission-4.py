class Solution:
    def trap(self, height: List[int]) -> int:
        def sweep(h):
            left = 0
            stored = []
            trapped = 0
            for right in range(1, len(h)):
                if h[left] <= h[right]:
                    for v in stored:
                        trapped += h[left] - v
                    stored = []
                    left = right
                else:
                    stored.append(h[right])
            return trapped, left

        trapped, peak = sweep(height)

        trapped += sweep(height[peak:][::-1])[0]
        return trapped

