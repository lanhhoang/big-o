# https://www.spoj.com/problems/MST

from heapq import heappush, heappop

INF = int(1e9)
class Node:
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist <= other.dist

def prim(src):
  pq = []
  heappush(pq, Node(src, 0))
  dist[src] = 0
  while len(pq) != 0:
    top = heappop(pq)
    u = top.id
    d = top.dist
    visited[u] = True
    for neighbor in graph[u]:
      v = neighbor.id
      w = neighbor.dist
      if not visited[v] and w < dist[v]:
        dist[v] = w
        heappush(pq, Node(v, w))
        path[v] = u

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dist = [INF for _ in range(N + 1)]
path = [-1 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for _ in range(M):
  u, v, w = map(int, input().split())
  graph[u].append(Node(v, w))
  graph[v].append(Node(u, w))
prim(1)
res = 0
for i in range(1, N + 1):
  if path[i] == -1:
    continue
  res += dist[i]
print(res)