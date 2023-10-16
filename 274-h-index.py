#BAD SOLUTION O(n*k where k is the max value of an entrie)
# SO this can be way worse than O(n^2)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maxValue = max(citations)
        memo = [0 for i in range(maxValue + 1)]


        for i in range(len(citations)):
            maxValue = citations[i]

            for j in range(0, maxValue + 1):
                memo[j] += 1

        for idx in range(len(memo) - 1, -1, -1):
            if idx <= memo[idx]:
                return idx
        
        return 0

# Better nlogn
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for i in range(n):
            if n - i <= citations[i]:
                return n - i
        
        return 0
        

#O(n) solution I found in solutions
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        tmp = [0 for _ in range(len(citations) + 1)]
        n = len(citations)
        for i in range(n):
            if citations[i] > n:
                tmp[n] += 1
            else:
                tmp[citations[i]] += 1
        
        total = 0

        for j in range(n, -1, -1):
            total += tmp[j]
            if total >= j:
                return j



