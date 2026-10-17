"""
54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
[1] --> [2] --> [3]
                 |
                 v
[4] --> [5]     [6]
 ^               |
 |               v
[7] <-- [8] <-- [9]

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
[1] --> [2] --> [3] --> [4]
                         |
                         v
[5] --> [6] --> [7]     [8]
 ^                       |
 |                       v
[9] <-- [10] <-- [11] <-- [12]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []

        top = 0
        bottom = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # 1. Recorrer fila superior: izquierda -> derecha
            for col in range(left, right + 1):
                result.append(matrix[top][col])

            top += 1

            # 2. Recorrer columna derecha: arriba -> abajo
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])

            right -= 1

            # 3. Recorrer fila inferior: derecha -> izquierda
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])

                bottom -= 1

            # 4. Recorrer columna izquierda: abajo -> arriba
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])

                left += 1

        return result
    
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
result = Solution().spiralOrder(matrix)
print(result)