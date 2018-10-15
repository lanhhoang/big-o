# https://www.spoj.com/problems/SHPATH

from heapq import heappush, heappop

INF = int(1e9)

class Node:
  def __init__(self, id, cost):
    self.id = id
    self.cost = cost

  def __lt__(self, other):
    return self.cost < other.cost

def dijkstra(n, src, dest):
  pq = []
  dist = [INF for _ in range(n + 1)]
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
  print(dist[dest])

def inp():
  return int(input())

if __name__ == '__main__':
  s = inp()
  for test in range(s):
    n = inp()
    graph = [[] for _ in range(n + 1)]
    cities = {}
    for i in range(1, n + 1):
      name = input().strip()
      cities[name] = i
      p = inp()
      for _ in range(p):
        nr, cost = map(int, input().split())
        graph[i].append(Node(nr, cost))

    r = int(input())
    for _ in range(r):
      source, destination = map(str, input().split())
      dijkstra(n, cities[source], cities[destination])
    # read empty line
    for i in range(1, n + 1):
      graph[i].clear()
    if test < s - 1:
      empty = input().strip()