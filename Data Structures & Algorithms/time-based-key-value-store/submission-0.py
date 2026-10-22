class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.timeMap:
            self.timeMap[key] = []

        self.timeMap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        values = self.timeMap[key]
        left, right = 0, len(values) - 1

        while left <= right:
            mid = left + (right - left) // 2
            midTime = values[mid][1]

            if timestamp > midTime:
                left = mid + 1
            elif timestamp < midTime:
                right = mid - 1
            else:
                return values[mid][0]

        if right >= 0:
            return values[right][0]
        return ""