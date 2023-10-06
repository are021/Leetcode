class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num:
                return[num[complement], i]
            num[nums[i]] = i
        
        return []