class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def count(subset, index):
            if index>=len(nums):
                return ans.append(subset.copy())

            subset.append(nums[index])
            count(subset,index+1)
            subset.pop()
            count(subset,index+1)

        count([],0)
        
        return ans