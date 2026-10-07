class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combList = []
        for i in range(len(position)):
            combList.append((position[i], speed[i]))

        combList.sort()
        fleets = 0
        leadTime = 0

        while combList:
            pos, sped = combList.pop()
            time = (target - pos) / sped

            if time > leadTime:
                fleets += 1
                leadTime = time

        return fleets