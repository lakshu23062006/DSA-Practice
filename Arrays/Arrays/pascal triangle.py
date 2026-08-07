# LeetCode 118. Pascal's Triangle

# Approach:
# 1. Initialize an empty list to store the triangle.
# 2. Create each row with all elements initialized to 1.
# 3. For each row (except the first two), calculate the middle elements
#    by adding the two elements directly above from the previous row.
# 4. Append the completed row to the triangle.
# 5. Return the generated Pascal's Triangle.

# Time Complexity: O(numRows²)
# Space Complexity: O(numRows²)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = tri[i - 1][j - 1] + tri[i - 1][j]

            tri.append(row)

        return tri
