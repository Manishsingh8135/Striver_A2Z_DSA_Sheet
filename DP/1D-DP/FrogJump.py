# There is a frog on the 1st step of an N stairs long staircase. The frog wants to reach the Nth stair. HEIGHT[i] is the height of the (i+1)th stair.If Frog jumps from ith to jth stair, the energy lost in the jump is given by |HEIGHT[i-1] - HEIGHT[j-1] |.In the Frog is on ith staircase, he can jump either to (i+1)th stair or to (i+2)th stair. Your task is to find the minimum total energy used by the frog to reach from 1st stair to Nth stair.

# Difficulty: Easy
# Platform: CodingNinja
# Link: https://www.codingninjas.com/codestudio/problems/frog-jump_3621012?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTab=0



def frogJump(n, heights) :
    def dfs(i, memo):
        if i == 0:
            return 0
        if i in memo:
            return memo[i]
        ones = dfs(i - 1, memo) + abs(heights[i] - heights[i - 1])
        twos = float('inf')
        if i > 1:
            twos = dfs(i - 2, memo) + abs(heights[i] - heights[i - 2])
        memo[i] = min(ones, twos)
        return memo[i]

    return dfs(n - 1, {})

arr=[10,20,30,10]
n=4
newfunc=frogJump(n,arr)
print(newfunc)