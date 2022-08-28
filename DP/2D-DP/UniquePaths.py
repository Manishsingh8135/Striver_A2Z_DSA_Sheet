# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Difficulty: Medium
# Platform : Leetcode
# Link : https://leetcode.com/problems/unique-paths/

#Code:


def uniquePaths(m, n) :
    visited = {}

    def dfs(i, j, visited):
        key = str(i) + "," + str(j)
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        if key in visited:
            return visited[key]
        if i == m - 1 and j == n - 1:
            return 1

        down = dfs(i, j + 1, visited)

        right = dfs(i + 1, j, visited)

        visited[key] = down + right
        return visited[key]

    return dfs(0, 0, visited)

#Driver Code

# Input:
m=3
n=2

#Output: 3

newfunc=uniquePaths(m,n)
print(newfunc)

