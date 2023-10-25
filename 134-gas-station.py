
# My solution, O(n) did a similar problem in one of my classes.
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        res = 0
        curr_total = 0
        array_total = 0
        for i in range(n):
            curr_total += (gas[i] - cost[i])
            array_total += (gas[i] - cost[i])
            if curr_total < 0:
                res = i + 1
                curr_total = 0
            
        return res if array_total >= 0 else -1
            

                
            
