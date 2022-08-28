# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Difficulty: Medium
# Platform: Leetcode
# Link: https://leetcode.com/problems/house-robber-ii/

#Code
def rob( nums) :
    n = len(nums)
    if not nums:
        return 0

    def dfs(i, n, dict):
        if i >= n:
            return 0
        if i in dict:
            return dict[i]
        take = dfs(i + 2, n, dict) + nums[i]
        nottake = dfs(i + 1, n, dict) + 0

        dict[i] = max(take, nottake)
        return dict[i]

    start = dfs(0, n - 1, {})
    first = dfs(1, n, {})
    return max(start, first, nums[0])

#Driver Code:

#Input:
arr=[1,2,3,1]

#Output : 4
newfunc=rob(arr)
print(newfunc)
