# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# LEETCODE: EASY  70 Climbing Stairs
# Link: https://leetcode.com/problems/climbing-stairs/

def climbStairs( n):
    memo = {}
    def dfs(n, memo):
        if n <= 1:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = dfs(n - 1, memo) + dfs(n - 2, memo)
        return memo[n]
    return dfs(n, {})

newfunc=climbStairs(5)
print(newfunc)

