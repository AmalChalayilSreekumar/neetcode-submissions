from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):          # always binary search the smaller array
            A, B = B, A

        m, n = len(A), len(B)
        half = (m + n + 1) // 2      # size of the left half
        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2       # elements taken from A
            j = half - i             # elements taken from B

            aL = A[i - 1] if i > 0 else float("-inf")
            aR = A[i]     if i < m else float("inf")
            bL = B[j - 1] if j > 0 else float("-inf")
            bR = B[j]     if j < n else float("inf")

            if aL <= bR and bL <= aR:            # valid partition
                if (m + n) % 2:                  # odd total
                    return float(max(aL, bL))
                return (max(aL, bL) + min(aR, bR)) / 2
            elif aL > bR:                        # A's cut is too far right
                hi = i - 1
            else:                                # A's cut is too far left
                lo = i + 1