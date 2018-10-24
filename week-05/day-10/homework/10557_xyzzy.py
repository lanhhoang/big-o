# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1498

from queue import Queue

graph = []
maxEnergy = []

class Edge:
  def __init__(self, source, target, weight):
    self.source = source
    self.target = target
    self.weight = weight

def BFS(src, dest, graph):
  q = Queue()
  visited = [False] * (n + 1)
  q.put(src)
  visited[src] = True

  while not q.empty():
    u = q.get()
    for v in graph[u]:
      if not visited[v]:
        visited[v] = True
        q.put(v)
  return visited[dest]

def BellmanFord(src, dest, neighbors):
  global graph
  global maxEnergy

  maxEnergy[src] = 100
  cycle_v = 0
  flag = 0
  for _ in range(1, n):
    for edge in graph:
      u = edge.source
      v = edge.target
      w = edge.weight
      if maxEnergy[u] > 0 and maxEnergy[u] + w > maxEnergy[v]:
        maxEnergy[v] = maxEnergy[u] + w
  for edge in graph:
    u = edge.source
    v = edge.target
    w = edge.weight
    if maxEnergy[u] > 0 and maxEnergy[u] + w > maxEnergy[v]:
      flag = 1
      cycle_v = v

  if maxEnergy[dest] > 0:
    print('winnable')
  elif flag == 1 and BFS(cycle_v, dest, neighbors):
    print('winnable')
  else:
    print('hopeless')

while True:
  n = int(input())
  if n == -1:
    break
  energy_levels = [0 for _ in range(n + 1)]
  neighbors = [[] for _ in range(n + 1)]
  for i in range(1, n + 1):
    inp = list(map(int, input().split()))
    energy, num_of_doorways, rooms = inp[0], inp[1], inp[2:]
    energy_levels[i] = energy
    for j in range(num_of_doorways):
      neighbors[i].append(rooms[j])
  graph = []
  maxEnergy = [0 for _ in range(n + 1)]
  for k in range(1, n + 1):
    rooms = neighbors[k]
    for room in rooms:
      energy = energy_levels[room]
      graph.append(Edge(k, room, energy))
  start = 1
  end = n
  BellmanFord(start, end, neighbors)