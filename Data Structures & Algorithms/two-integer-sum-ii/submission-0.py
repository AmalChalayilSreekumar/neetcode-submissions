class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)-1

        left = 0
        right = n

        while left!=right:
            temp = numbers[left]+numbers[right]

            if temp > target:
                right -=1
            elif temp < target:
                left +=1
            elif temp == target:
                return [left+1, right+1]
        return False