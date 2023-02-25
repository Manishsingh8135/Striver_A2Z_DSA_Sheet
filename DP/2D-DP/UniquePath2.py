#You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
#
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
# The testcases are generated so that the answer will be less than or equal to 2 * 109.


def uniquePaths2(m, n,grid) :
    visited = {}
    m, n = len(grid), len(grid[0])

    def dfs(i, j, visited):
        key = str(i) + "," + str(j)
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 1:
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


#Output: 3
grid=[[0,0,0],[0,1,0],[0,0,0]]
m,n=len(grid),len(grid[0])
newfunc=uniquePaths2(m,n,grid)
print(newfunc)