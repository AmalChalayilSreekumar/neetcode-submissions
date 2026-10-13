class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)

        # Smaller than the smallest or larger than the largest -> False (done once, up front)
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        targetRow = None

        # Check the 2 ends first (no rows in front of / behind them)
        if rows == 1:
            targetRow = matrix[0]
        elif target < matrix[1][0]:           # first row
            targetRow = matrix[0]
        elif target >= matrix[rows - 1][0]:   # last row
            targetRow = matrix[rows - 1]
        else:
            # Target is in a middle row, somewhere in rows 1..rows-2
            leftRow, rightRow = 1, rows - 2
            while leftRow <= rightRow:
                mid = leftRow + (rightRow - leftRow) // 2
                midRight = mid + 1

                # target starts at/after this row's first element, before the next row's
                if matrix[mid][0] <= target < matrix[midRight][0]:
                    targetRow = matrix[mid]
                    break
                elif target < matrix[mid][0]:
                    rightRow = mid - 1
                else:
                    leftRow = mid + 1

        if targetRow is None:
            return False

        leftCol, rightCol = 0, len(targetRow) - 1

        while leftCol <= rightCol:
            mid = leftCol + (rightCol - leftCol) // 2

            if targetRow[mid] < target:
                leftCol = mid + 1
            elif targetRow[mid] > target:
                rightCol = mid - 1
            else:
                return True
        return False