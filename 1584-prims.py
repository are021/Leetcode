class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Create adjacency list

        N = len(points)
        adj = {i:[] for i in range(N)} #Map each node to list of points (cost, node)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])


        #Implement prims

        res = 0
        visit = set()
        minH = [[0, 0]] #[cost, point]

        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit :
                continue #Already processed node
            res += cost
            visit.add(i)
            for neighborCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neighborCost, nei])
        
        return res


# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n = len(points)
#         min_cost = 0
#         visited = [False] * n
#         pq = [(0, 0)]  # (cost, vertex)
#         cache = {0: 0}

#         while pq:
#             cost, u = heapq.heappop(pq)

#             if visited[u]:
#                 continue

#             visited[u] = True
#             min_cost += cost

#             for v in range(n):
#                 if not visited[v]:
#                     dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
#                     if dist < cache.get(v, float('inf')):
#                         cache[v] = dist
#                         heapq.heappush(pq, (dist, v))

#         return min_cost        
        

        


        