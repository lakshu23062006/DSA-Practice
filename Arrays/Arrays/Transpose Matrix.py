# LeetCode 867. Transpose Matrix

# Approach:
# 1. Find the number of rows and columns in the matrix.
# 2. Create a new matrix with dimensions (columns × rows).
# 3. Traverse each element of the original matrix.
# 4. Swap the row and column indices while storing the element.
# 5. Return the transposed matrix.

# Time Complexity: O(rows × cols)
# Space Complexity: O(rows × cols)

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        ans = [[0] * rows for i in range(cols)]

        for i in range(rows):
            for j in range(cols):
                ans[j][i] = matrix[i][j]

        return ans
