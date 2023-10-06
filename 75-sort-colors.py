class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        heap = [i for i in nums]
        heapq.heapify(heap)

        res = []

        for i in range(len(heap)):
            nums[i] = heapq.heappop(heap)


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l , r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]


        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1

            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
            