# O(n) time and space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use two sum hashmap solution for this?

        map = {}

        for i in range(len(numbers)):
            complement = target - numbers[i]

            if complement in map:
               return [map[complement] + 1,i + 1]

            map[numbers[i]] = i

# O(1) space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while l < r:
            curr = numbers[l] + numbers[r]

            if curr > target:
                r -= 1
            if curr < target:
                l += 1
            if curr == target:
                return [l + 1, r + 1]



