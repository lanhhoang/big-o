# https://www.spoj.com/problems/SHPATH

from queue import PriorityQueue

MAX = 10001
INF = int(1e9)
graph = [[] for _ in range(MAX)]

class Node:
  def __init__(self, id, cost):
    self.id = id
    self.cost = cost

  def __lt__(self, other):
    return self.cost < other.cost

def dijkstra(s):
  pq = PriorityQueue()
  pq.put(Node(s, 0))
  dist[s] = 0

  while not pq.empty():
    top = pq.get()
    u = top.id
    w = top.cost
    for neighbor in graph[u]:
      if w + neighbor.cost < dist[neighbor.id]:
        dist[neighbor.id] = w + neighbor.cost
        pq.put(Node(neighbor.id, dist[neighbor.id]))
        path[neighbor.id] = u

def inp():
  return int(input())

if __name__ == '__main__':
  s = inp()
  for test in range(s):
    n = inp()
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
      dist = [INF for _ in range(MAX)]
      path = [-1 for _ in range(MAX)]
      source, destination = map(str, input().split())
      start = cities.get(source)
      end = cities.get(destination)
      dijkstra(start)
      print(dist[end])
    # read empty line
    if test < s - 1:
      empty = input().strip()