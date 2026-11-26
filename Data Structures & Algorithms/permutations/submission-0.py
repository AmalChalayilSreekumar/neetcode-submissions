class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def perms(subset, used):
            if len(subset) == len(nums):
                ans.append(subset.copy())
                return
            

            
            for i in nums:
                if i in used:
                    continue
                used.add(i)
                subset.append(i)
                perms(subset,used)
                used.remove(i)
                subset.pop()

        perms([],set())
        return ans                