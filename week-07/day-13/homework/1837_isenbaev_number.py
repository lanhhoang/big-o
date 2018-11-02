# http://acm.timus.ru/problem.aspx?space=1&num=1837

from sys import stdin
from queue import Queue

input = stdin.readline
MAX = 305
dist = [-1] * MAX
graph = [[] for _ in range(MAX)]

def BFS(start):
  queue = Queue()
  queue.put(start)
  dist[start] = 0

  while not queue.empty():
    u = queue.get()
    for v in graph[u]:
      if dist[v] == -1:
        dist[v] = dist[u] + 1
        queue.put(v)

n = int(input())
contestants = dict()
count = 0
for _ in range(n):
  team = input().split()
  for member in team:
    if member not in contestants:
      contestants[member] = count
      count += 1
  u, v, w = contestants[team[0]], contestants[team[1]], contestants[team[2]]
  graph[u].append(v)
  graph[u].append(w)
  graph[v].append(u)
  graph[v].append(w)
  graph[w].append(u)
  graph[w].append(v)
sorted_contestants = {k: contestants[k] for k in sorted(contestants)}
if 'Isenbaev' in contestants:
  src = contestants.get('Isenbaev')
  BFS(src)
  for key in sorted_contestants.keys():
    num = sorted_contestants.get(key)
    if dist[num] == -1:
      print(key, 'undefined')
    else:
      print(key, dist[num])
else:
  for key in sorted_contestants.keys():
    print(key, 'undefined')