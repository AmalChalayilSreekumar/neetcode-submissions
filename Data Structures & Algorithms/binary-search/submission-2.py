class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)-1

        left = 0
        right = n

        while left<=right:
            mid=left+(right-left)//2

            if target<nums[mid]:
                right=mid-1
            elif target>nums[mid]:
                left=mid+1
            else:
                return mid
        return -1