class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        if target == nums[left]:
            return left
        if target == nums[right]:
            return right

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # Case 1: window is not rotated -> plain binary search
            if nums[left] <= nums[right]:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

            # Case 2: rotated, mid is in the left (higher) segment
            elif nums[mid] >= nums[left]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            # Case 3: rotated, mid is in the right (lower) segment
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1