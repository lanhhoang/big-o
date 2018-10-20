# http://www.lightoj.com/volume_showproblem.php?problem=1074
# https://vjudge.net/problem/LightOJ-1074

INF = int(1e9)
graph = []
dist = []
path = []

class Edge:
  def __init__(self, source, target, weight):
    self.source = source
    self.target = target
    self.weight = weight

def BellmanFord(src):
  global graph
  global dist
  global path

  dist[src] = 0
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
      return False
  return True

if __name__ == '__main__':
  T = int(input())
  for case in range(1, T + 1):
    input()
    n = int(input())
    junctions = list(map(int, input().split()))
    junctions = [0] + junctions
    m = int(input())
    graph = []
    dist = [INF for _ in range(n + 5)]
    path = [-1 for _ in range(n + 5)]
    for _ in range(m):
      u, v = map(int, input().split())
      w = (junctions[v] - junctions[u]) ** 3
      graph.append(Edge(u, v, w))
    q = int(input())
    src = 1
    print('Case ' + str(case) + ':')
    for _ in range(q):
      dest = int(input())
      res = BellmanFord(src)
      if dist[dest] == INF or dist[dest] < 3:
        print('?')
      else:
        print(dist[dest])