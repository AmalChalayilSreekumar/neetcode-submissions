class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        buckets = [[] for i in range(0,n+1)]

        numsDict=dict.fromkeys(set(nums),0)

        for i in nums:
            numsDict[i]+=1
        
        for i in numsDict:
            buckets[numsDict[i]].append(i)

        ans = []

        for i in range(n,0,-1):
            if buckets[i]:
                for num in buckets[i]:
                    ans.append(num)
                    if len(ans)==k:
                        return ans
        return ans


        

        




        