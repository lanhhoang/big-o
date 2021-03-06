# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=975

from heapq import heappush, heappop
from math import sqrt
INF = int(1e9)

class Node:
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist <= other.dist

def prim(graph, src):
  dist = [INF for _ in range(N + 1)]
  visited = [False] * (N + 1)
  weight = 0
  dist[src] = 0
  pq = []
  heappush(pq, Node(src, 0))

  while len(pq) != 0:
    top = heappop(pq)
    u = top.id
    visited[u] = True
    for v in range(1, N + 1):
      if not visited[v] and dist[v] > graph[u][v]:
        dist[v] = graph[u][v]
        heappush(pq, Node(v, dist[v]))

  for i in range(1, N + 1):
    weight += dist[i]
  return weight

def distance(x1, y1, x2, y2):
  sqr_dis = (x2 - x1) ** 2 + (y2 - y1) ** 2
  return sqrt(sqr_dis)

T = int(input())
for t in range(T):
  input()
  N = int(input())
  x = [0] * (N + 1)
  y = [0] * (N + 1)
  for i in range(1, N + 1):
    x[i], y[i] = map(float, input().split())
  graph = [[] for _ in range(N + 1)]
  for i in range(1, N + 1):
    graph[i].append(0.0)
    for j in range(1, N + 1):
      graph[i].append(distance(x[i], y[i], x[j], y[j]))
  print("%.2f" % prim(graph, 1))
  if t < T - 1:
    print()