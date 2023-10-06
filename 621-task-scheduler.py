# class Solution:
#     def leastInterval(self, tasks: List[str], n: int) -> int:
#         if len(tasks) == 0:
#             return 0
#         if n == 0:
#             return len(tasks)

#         idleTable = {}
#         q = deque()
#         interval = 0
#         for val in tasks:
#             q.append(val)
#             if val not in idleTable:
#                 idleTable[val] = 0
        
#         while q:
#             curr = q.popleft() 
            
#             if idleTable[curr] == 0:
#                 interval += 1
#             else:
#                 q.append(curr)
#             idleTable[curr] = (1 + idleTable[curr]) % n
#         return interval


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # O(n * m) Idle time
        count = Counter(tasks) #Counts occurences of Characters
        maxHeap = [-cnt for cnt in count.values()] #Create the minheap
        heapq.heapify(maxHeap) #Heapify the heaparray

        time = 0
        q = deque() #Pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHead) #Add 1 since we processed task
                if cnt:
                    q.append([cnt, time + n])
            
            #Take care of queue
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        
        return time
            



            
            


        