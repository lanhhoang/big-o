# https://www.spoj.com/problems/CAM5/

MAX = 100001
V = None
E = None
visited = [False] * MAX
path = [-1] * MAX
graph = [[] for _ in range(MAX)]

def DFS(start):
  stack = []
  visited[start] = True
  stack.append(start)

  while len(stack) > 0:
    u = stack.pop()
    for v in graph[u]:
      if visited[v] == False:
        visited[v] = True
        stack.append(v)
        path[v] = u

t = int(input())

for _ in range(t):
  V = int(input())
  E = int(input())

  for i in range(V):
    graph[i].clear()
    visited[i] = False
    path[i] = -1

  for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

  for i in range(V):
    DFS(i)
  
  count = 0
  for i in range(V):
    if path[i] == -1:
      count += 1
  print(count)