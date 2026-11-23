class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def count(index):
            if index>=len(nums):
                return ans.append(subset.copy())

            subset.append(nums[index])
            count(index+1)
            subset.pop()
            count(index+1)

        count(0)
        
        return ans