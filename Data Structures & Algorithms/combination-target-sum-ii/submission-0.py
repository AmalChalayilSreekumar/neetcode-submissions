class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()

        
        def combDFS(subset, current, index):
            if target<current:
                return
            
            if target == current: 
                ans.append(subset.copy())
                return
            
            if index>n-1:
                return
            
            current += candidates[index]
            subset.append(candidates[index])

            combDFS(subset,current,index+1)
            subset.pop()
            current -= candidates[index]

            while index<n-1 and candidates[index]==candidates[index+1]:
                index+=1
            
            index+=1
            
            combDFS(subset,current,index)
        
        combDFS([],0,0)

        return ans

            
                
            



            