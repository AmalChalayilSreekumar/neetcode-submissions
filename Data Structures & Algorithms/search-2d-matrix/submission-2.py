class Solution:
    def searchMatrix(self, matrix, target) -> bool:

        # If its smaller than the smallest element or larger than the largest element return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        targetRow = None

        if len(matrix) == 1:
            targetRow = matrix[0]

        # Check 2 ends of the matrix (Don't have rows in front and behind)
        elif target < matrix[1][0]:    # First row
            targetRow = matrix[0]
        elif target >= matrix[-1][0]:  # Last row
            targetRow = matrix[-1]

        else:
            # Has to be a middle row because we tested first and last row
            leftRow, rightRow = 1, len(matrix) - 2

            while leftRow <= rightRow:
                mid = leftRow + (rightRow - leftRow) // 2
                midRight = mid + 1

                # Binary Search
                if matrix[mid][0] <= target < matrix[midRight][0]:
                    targetRow = matrix[mid]
                    break
                elif matrix[mid][0] > target:
                    rightRow = mid - 1
                else:
                    leftRow = mid + 1

        if targetRow is None:
            return False

        # Now just do regular binary search on the target row
        leftCol, rightCol = 0, len(targetRow) - 1

        while leftCol <= rightCol:
            mid = leftCol + (rightCol - leftCol) // 2

            if targetRow[mid] > target:
                rightCol = mid - 1
            elif targetRow[mid] < target:
                leftCol = mid + 1
            else:
                return True
        return False