"""
48. Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

Example 1:

Original:      Rotada (90°):
[1, 2, 3]  -->  [7, 4, 1]
[4, 5, 6]  -->  [8, 5, 2]
[7, 8, 9]  -->  [9, 6, 3]

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Original:                  Rotada (90°):
[ 5,  1,  9, 11]    -->    [15, 13,  2,  5]
[ 2,  4,  8, 10]    -->    [14,  3,  4,  1]
[13,  3,  6,  7]    -->    [12,  6,  8,  9]
[15, 14, 12, 16]    -->    [16,  7, 10, 11]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()
        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
output = [[7,4,1],[8,5,2],[9,6,3]]

solution = Solution().rotate(matrix)
print(solution)

# Should be a second matrix to save.
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        number_of_raws = len(matrix)
        number_of_colums = len(matrix[0])
        for i in range(number_of_colums):
            for j in range(number_of_raws):
                matrix[i][j] = matrix[number_of_raws - 1 - j][i]

        return matrix