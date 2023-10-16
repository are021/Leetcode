#My Solution
# I've been doing so much dynamic programming, I just approach every problem as a dynamic programming problem now :)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #memoization?

        n = len(nums)
        dp = [False] * n
        dp[-1] = True #Base Case

        for i in range(n - 1, -1, -1):

            #If its zero we cannot move forward
            if nums[i] == 0:
                continue

            rnge = i + nums[i]
            for j in range(i + 1, rnge + 1):
                if j < n and dp[j]:
                    dp[i] = True #This index can reach it!
                    break
        
        return dp[0]


# A greedy solution O(n)
# I was so close to solving it this way!, just one line was different
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        end = n - 1

        for i in range(n - 1, -1, -1):
            if i + nums[i] >= end:
                end = i
            
        
        return True if end == 0 else False




            


                

                



