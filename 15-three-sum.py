class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Don't use duplicates!
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Two Sum II Solution
            l, r = i + 1, len(nums) - 1
            while l < r:
                third = nums[i] + nums[l] + nums[r]

                if third > 0:
                    r -= 1

                if third < 0:
                    l += 1
                
                if third == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        
        return res

            



        


