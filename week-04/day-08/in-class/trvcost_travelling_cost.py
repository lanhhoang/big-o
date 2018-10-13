# https://www.spoj.com/problems/TRVCOST/

from queue import PriorityQueue

MAX = 501
INF = int(1e9)
graph = [[] for _ in range(MAX)]
dist = [INF for _ in range(MAX)]
path = [-1 for _ in range(MAX)]

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

N = int(input())

for _ in range(N):
  A, B, W = map(int, input().split())
  node_A = Node(A, W)
  node_B = Node(B, W)
  graph[A].append(node_B)
  graph[B].append(node_A)

U = int(input())
Q = int(input())
dijkstra(U)

for _ in range(Q):
  V = int(input())
  if dist[V] == INF:
    print('NO PATH')
  else:
    print(dist[V])