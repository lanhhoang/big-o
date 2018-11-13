# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1541

from heapq import heappush, heappop
INF = int(1e9)

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
  trace = [{} for _ in range(N)]
  weight = 0
  dist[src] = 0
  pq = []
  heappush(pq, Node(src, 0))
  
  while len(pq) != 0:
    top = heappop(pq)
    u = top.id
    visited[u] = True
    _len = len(graph[u])
    for i in range(_len):
      v = graph[u][i].id
      w = graph[u][i].dist
      if not visited[v] and w < dist[v]:
        dist[v] = w
        heappush(pq, Node(v, w))
        trace[v] = {'path': u, 'index': i}
  
  for i in range(N):
    weight += dist[i]
  return weight, trace

T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  graph = [[] for _ in range(N)]
  for _ in range(M): # O(M)
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(Node(v, w))
    graph[v].append(Node(u, w))
  trace = []
  mst1, trace = prim(graph, 0) # O(MlogN)
  mst2 = INF
  for j in range(1, N): # O(N * MlogN)
    item = trace[j]
    u = item['path']
    i = item['index']
    temp = graph[u][i].dist
    graph[u][i].dist = INF
    val, temp_trace = prim(graph, 0) # O(MlogN)
    graph[u][i].dist = temp
    mst2 = min(mst2, val)
  print('{} {}'.format(mst1, mst2))

# Complexity: O(N * MlogN)