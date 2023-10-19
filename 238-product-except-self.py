# res = []
# total = 1

# for val in nums:
#     total *= val

# for val in nums:
#     res.append(total//val)

# return res
# CANNOT USE DIVISION SO WON'T WORK!


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # So we need to know whats infront and behind the value i So We make two passes
        forward = [1] * n
        backward = [1] * n
        res = []
        #Forward Pass
        for i in range(1, n):
            forward[i] = nums[i - 1] * forward[i - 1]
        
        for i in range(n - 2, -1, -1):
            backward[i] = nums[i + 1] * backward[i + 1]
        
        for i in range(n):
            res.append(forward[i] * backward[i])

        return res
    

#This is an O(1) space solution   
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        n = len(nums)
        # So we need to know whats infront and behind the value i So We make two passes
        forward = [1] * n
        backward = 1
        #Forward Pass
        for i in range(1, n):
            forward[i] = nums[i - 1] * forward[i - 1]
        
        for i in range(n - 1, -1, -1):
            forward[i] *= backward
            backward *= nums[i]
        return forward