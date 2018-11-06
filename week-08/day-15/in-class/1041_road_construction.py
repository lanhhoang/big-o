# http://lightoj.com/volume_showproblem.php?problem=1041

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

T = int(input())
for t in range(T):
  input()
  m = int(input())
  roads = []
  for _ in range(m):
    roads.append(input())
  cities = dict()
  id = 0
  for road in roads:
    city1, city2, cost = road.split()
    if city1 not in cities:
      cities[city1] = id
      id += 1
    if city2 not in cities:
      cities[city2] = id
      id += 1
  n = len(cities)
  graph = [[] for _ in range(n)]
  dist = [INF for _ in range(n)]
  visited = [False] * (n)
  for road in roads:
    city1, city2, cost = road.split()
    u, v, w = cities[city1], cities[city2], int(cost)
    graph[u].append(Node(v, w))
    graph[v].append(Node(u, w))
  prim(0)
  res = 0
  for d in dist:
    res += d
  if res < INF:
    print('Case {}: {}'.format(t + 1, res))
  else:
    print('Case {}: Impossible'.format(t + 1))