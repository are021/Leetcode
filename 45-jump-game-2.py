# My solution - Nearly O(n^2 time complexity) even worse probably
# Another DP solution
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[-1] = 0

        for i in range(n - 2, -1 , -1):
            dist = nums[i] + i
            if dist >= n - 1:
                dp[i] = 1
            else:
                for j in range(1, (min(nums[i] + 1,n))):
                    dp[i] = min(dp[i], 1 + dp[i + j])

        return dp[0]
    
# Greedy Solution O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        #BFS like Greedy - Search by Levels - Level = Jumps

        jumps = 0
        l, r = 0, 0 

        while r < len(nums) - 1:
            far = 0
            for i in range(l, r + 1):
                far = max(far, i + nums[i])
            
            l = r + 1
            r = far
            jumps += 1
        
        return jumps

