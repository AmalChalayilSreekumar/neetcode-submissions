class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # A window of len(s1) can't fit inside a shorter s2,
        # so no permutation of s1 can possibly exist in s2.
        if len(s1) > len(s2):
            return False

        # Letter-frequency tables for 'a'..'z' (index 0 = 'a', 25 = 'z').
        s1_count = [0] * 26   # counts of letters in s1 (the target)
        s2_count = [0] * 26   # counts of letters in the current window of s2

        # Fill s1_count, and fill s2_count with the FIRST window of s2
        # (the first len(s1) characters). Both are done in one loop
        # because the window and s1 have the same length.
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1   # ord(c) - ord('a') maps letter -> 0..25
            s2_count[ord(s2[i]) - ord('a')] += 1

        # `matches` = how many of the 26 letters have equal counts in s1 and the window.
        # If matches == 26, the window is a permutation of s1.
        # Tracking this lets us avoid re-comparing all 26 counts on every slide.
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        left = 0  # left edge of the window (inclusive)

        # `right` is the index of the NEXT character to enter the window.
        # The window currently covers s2[left : right], so we start at len(s1).
        for right in range(len(s1), len(s2)):
            # Check the current window before sliding. If all 26 letters
            # match, we found a permutation of s1 in s2.
            if matches == 26:
                return True

            # ---- Add the new character on the right ----
            idx = ord(s2[right]) - ord('a')
            s2_count[idx] += 1
            if s2_count[idx] == s1_count[idx]:
                # This letter just went from mismatched to matched.
                matches += 1
            elif s2_count[idx] - 1 == s1_count[idx]:
                # This letter WAS matched before the increment, now it's off by one.
                matches -= 1

            # ---- Remove the old character on the left ----
            idx = ord(s2[left]) - ord('a')
            s2_count[idx] -= 1
            if s2_count[idx] == s1_count[idx]:
                # Mismatched -> matched.
                matches += 1
            elif s2_count[idx] + 1 == s1_count[idx]:
                # Was matched before the decrement, now off by one.
                matches -= 1

            left += 1  # shrink from the left so the window length stays len(s1)

        # The loop checks the window *before* sliding, so the very last
        # window hasn't been checked yet. Check it here.
        return matches == 26