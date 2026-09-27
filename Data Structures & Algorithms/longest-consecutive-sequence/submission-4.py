class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allNums = dict.fromkeys(set(nums), 0)
        nums = set(nums)
        best = 0
        length = 0
        
        for num in nums:
            if num-1 in allNums:
                continue
            while num+length in allNums:
                length+=1
            if length>=best:
                best = length
            length = 0
        

        return best