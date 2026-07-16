class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        col = [-1]*n
        for i in range(n):
           if col[i] != -1:
               continue
           que = deque([i])
           col[i] = 0
           while que:
               node = que.popleft()
               for neighbor in graph[node]:
                   if col[neighbor] == -1:
                       col[neighbor] = 1 - col[node]
                       que.append(neighbor)
                   elif col[neighbor] == col[node]:
                       return False
        return True