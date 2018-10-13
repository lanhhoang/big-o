# https://www.spoj.com/problems/MICEMAZE/

from queue import PriorityQueue

MAX = 101
INF = int(1e9)
graph = [[] for _ in range(MAX)]

class Node:
  def __init__(self, id, cost):
    self.id = id
    self.cost = cost
  def __lt__(self, other):
    return self.cost <= other.cost

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

N = inp()
E = inp()
T = inp()
M = inp()
for _ in range(M):
  u, v, w = map(int, input().split())
  node = Node(v, w)
  graph[u].append(node)

count = 0
for i in range(1, N + 1):
  dist = [INF for _ in range(MAX)]
  path = [-1 for _ in range(MAX)]
  dijkstra(i)
  if dist[E] <= T:
    count += 1

print(count)