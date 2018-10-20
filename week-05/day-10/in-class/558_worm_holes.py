# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=499
# Note for Python
# for edge in graph is faster than for i in range(len(graph))

INF = int(1e9)
graph = []
dist = []
path = []

class Edge:
  def __init__(self, source, target, weight):
    self.source = source
    self.target = target
    self.weight = weight

def BellmanFord(s):
  global dist
  global graph
  global path

  dist[s] = 0
  for i in range(1, n):
    for edge in graph:
      u = edge.source
      v = edge.target
      w = edge.weight
      if dist[u] != INF and dist[u] + w < dist[v]:
        dist[v] = dist[u] + w
        path[v] = u

  for edge in graph:
    u = edge.source
    v = edge.target
    w = edge.weight
    if dist[u] != INF and dist[u] + w < dist[v]:
      return print('possible')
  print('not possible')

if __name__ == '__main__':
  c = int(input())

  for _ in range(c):
    n, m = map(int, input().split())
    graph = []
    dist = [INF for _ in range(n + 5)]
    path = [-1 for _ in range(n + 5)]
    for _ in range(m):
      u, v, w = map(int, input().split())
      graph.append(Edge(u, v, w))
    s, t = 0, n - 1
    BellmanFord(s)