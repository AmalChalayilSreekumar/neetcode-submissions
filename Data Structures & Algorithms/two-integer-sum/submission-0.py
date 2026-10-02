class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {item: index for index, item in enumerate(nums)}

        
        for i in range(0, len(nums)):
            temp = target-nums[i]
            if temp in numsDict:
                  if i != numsDict[temp]: 
                    return [i,numsDict[temp]]