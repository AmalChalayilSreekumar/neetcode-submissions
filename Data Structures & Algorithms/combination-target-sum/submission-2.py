class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        
        def combDFS(subset, current, index):
            if target<current:
                return
            
            if target == current: 
                ans.append(subset.copy())
                return
            
            if index>n-1:
                return

            
            current += nums[index]
            subset.append(nums[index])

            combDFS(subset,current,index)
            subset.pop()
            current -= nums[index]
            combDFS(subset,current,index+1)
        
        combDFS([],0,0)

        return ans

            
                
            



            