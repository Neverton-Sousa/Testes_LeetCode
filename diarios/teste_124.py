class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            u,v = edges[i]
            c = succProb[i]
            adj[u].append((v, c))
            adj[v].append((u, c))

        dist = [0.0] * n
        visited = [False] * n
        maxHeap = [(-1.0, start)]
        dist[start] = [1.0]
        
        while maxHeap:
            w, u = heapq.heappop(maxHeap)
            if visited[u]:
                continue
            visited[u] = True
            
            for v, c in adj[u]:
                if not visited[v] and (c * (-w)) > dist[v]:
                    dist[v] = c * (-w)
                    heapq.heappush(maxHeap, ((c*w), v))
        return dist[end]