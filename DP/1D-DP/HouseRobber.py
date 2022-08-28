# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Difficulty : Medium
# Platform : LeetCode
# Link : https://leetcode.com/problems/house-robber/

#Code
def rob( nums):
    n = len(nums)

    def dfs(i, memo):
        if i >= n:
            return 0
        if i in memo:
            return memo[i]

        take = dfs(i + 2, memo) + nums[i]
        nottake = dfs(i + 1, memo)

        memo[i] = max(take, nottake)

        return memo[i]

    return dfs(0, {})

#Driver Code:

#Input:
arr=[1,2,3,1]

#Output : 4
newfunc=rob(arr)
print(newfunc)
