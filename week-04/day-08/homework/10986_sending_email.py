# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1927

from heapq import heappush, heappop

MAX = 20001
INF = int(1e9)
graph = [[] for _ in range(MAX)]
dist = [INF for _ in range(MAX)]
path = [-1 for _ in range(MAX)]

class Node:
  def __init__(self, id, cost):
    self.id = id
    self.cost = cost
  def __lt__(self, other):
    return self.cost <= other.cost

def dijkstra(src):
  pq = []
  heappush(pq, Node(src, 0))
  dist[src] = 0

  while len(pq) != 0:
    top = heappop(pq)
    u = top.id
    w = top.cost
    for neighbor in graph[u]:
      if w + neighbor.cost < dist[neighbor.id]:
        dist[neighbor.id] = w + neighbor.cost
        heappush(pq, Node(neighbor.id, dist[neighbor.id]))
        path[neighbor.id] = u

N = int(input())

for case in range(1, N + 1):
  n, m, s, t = map(int, input().split())

  for i in range(n):
    graph[i].clear()
    dist[i] = INF
    path[i] = -1

  for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append(Node(v, w))
    graph[v].append(Node(u, w))
  
  dijkstra(s)
  if dist[t] != INF:
    print('Case #' + str(case) + ': ' + str(dist[t]))
  else:
    print('Case #' + str(case) + ': unreachable')