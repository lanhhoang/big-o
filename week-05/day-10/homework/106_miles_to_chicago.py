# https://www.urionlinejudge.com.br/judge/en/problems/view/1655
# Reference: https://cs.stackexchange.com/questions/19207/find-least-probable-path-in-graph

import math

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
  global graph
  global dist
  global path

  dist[s] = 0
  for _ in range(1, n):
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
      return False
  return True

if __name__ == '__main__':
  while True:
    inp = list(map(int, input().split()))
    if inp[0] == 0:
      break
    n, m = inp
    graph = []
    dist = [INF for _ in range(n + 5)]
    path = [-1 for _ in range(n + 5)]
    for _ in range(m):
      u, v, w = map(int, input().split())
      w = -math.log2(w / 100)
      graph.append(Edge(u, v, w))
      graph.append(Edge(v, u, w))
    src = 1
    dest = n
    res = BellmanFord(src)
    if res == True:
      dist = math.pow(2, -dist[dest]) * 100
      print(format(dist, '.6f') + ' percent')