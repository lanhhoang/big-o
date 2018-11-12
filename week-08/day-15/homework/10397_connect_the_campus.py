# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1338

from heapq import heappush, heappop
from math import sqrt
INF = int(1e9)

class Scanner:
  def __generator__():
    while True:
      try:
        buff = input().strip().split()
        for x in buff:
          yield x
      except EOFError:
        exit()

  sc = __generator__()
  def next():
    return Scanner.sc.__next__()

class Node:
  def __init__(self, id, dist):
    self.id = id
    self.dist = dist
  def __lt__(self, other):
    return self.dist <= other.dist

def prim(graph, src):
  N = len(graph)
  dist = [INF for _ in range(N)]
  visited = [False] * N
  weight = 0
  dist[src] = 0
  pq = []
  heappush(pq, Node(src, 0))

  while len(pq) != 0:
    top = heappop(pq)
    u = top.id
    visited[u] = True
    for v in range(N):
      if not visited[v] and dist[v] > graph[u][v]:
        dist[v] = graph[u][v]
        heappush(pq, Node(v, dist[v]))

  for i in range(N):
    weight += dist[i]
  return weight

def distance(x1, y1, x2, y2):
  sqr_dis = (x2 - x1) ** 2 + (y2 - y1) ** 2
  return sqrt(sqr_dis)

while True:
  N = int(Scanner.next())
  x = [0] * N
  y = [0] * N
  for i in range(N):
    x[i], y[i] = int(Scanner.next()), int(Scanner.next())
  graph = []
  for i in range(N):
    graph.append([])
    for j in range(N):
      graph[i].append(distance(x[i], y[i], x[j], y[j]))
  M = int(Scanner.next())
  for _ in range(M):
    u, v = int(Scanner.next()), int(Scanner.next())
    u -= 1
    v -= 1
    graph[u][v] = 0
    graph[v][u] = 0
  print("%.2f" % prim(graph, 0))