class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        graph=[[]for _ in range(n)]
        for i,j,x in edges:
            graph[i].append((j,x))
            graph[j].append((i,x))
        def dijkstra(start):
            dist=[float('inf')]*n
            dist[start]=0
            heap=[(0,start)]
            while heap:
                d,node=heapq.heappop(heap)
                if d>dist[node]:
                    continue
                for neighbor,weight in graph[node]:
                    new=d+weight
                    if new<dist[neighbor]:
                        dist[neighbor]=new
                        heapq.heappush(heap,(new,neighbor))
            return dist
        min=n
        city=-1
        for i in range(n):
            reachable_cities=sum(1 for d in dijkstra(i) if d<=distanceThreshold)
            if reachable_cities<=min:
                min=reachable_cities
                city=i
        return city 