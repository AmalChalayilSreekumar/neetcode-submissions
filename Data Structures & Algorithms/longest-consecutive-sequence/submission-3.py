class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allNums = dict.fromkeys(set(nums), 0)
        nums = set(nums)
        best = 0
        length = 0
        
        for num in nums:
            try:
                allNums[num-1]
            except KeyError:
                while num+length in allNums:
                    length+=1
                if length>=best:
                    best = length
                length = 0
        

        return best