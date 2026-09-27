class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allNums = dict.fromkeys(set(nums), 0)
        nums = set(nums)
        start = []

        
        for num in nums:
            try:
                allNums[num-1]
            except KeyError:
                start.append(num)

        print(start)
        best = 0
        length = 0
        for num in start:
            while num+length in allNums:
                length+=1
                print(num, length)
            if length>=best:
                best = length
            length = 0
        

        return best