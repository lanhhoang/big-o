# https://www.hackerrank.com/challenges/bfsshortreach/problem

from queue import Queue

MAX = 1005
visited = [False] * MAX
dist = [-1] * MAX
graph = [[] for i in range(MAX)]

def inp():
  return map(int, input().split())

def BFS(s):
  q = Queue()
  q.put(s)
  visited[s] = True
  dist[s] = 0

  while not q.empty():
    u = q.get()
    for v in graph[u]:
      if not visited[v]:
        visited[v] = True
        dist[v] = dist[u] + 6
        q.put(v)

q = int(input())

for _ in range(q):
  n, m = inp()

  for i in range(MAX):
    visited[i] = False
    dist[i] = -1
    graph[i].clear()

  for _ in range(m):
    u, v = inp()
    graph[u].append(v)
    graph[v].append(u)

  s = int(input())
  BFS(s)

  for i in range(1, n + 1):
    if i == s:
      continue
    print(dist[i], end=' ')
  print()