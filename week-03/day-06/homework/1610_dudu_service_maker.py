# https://www.urionlinejudge.com.br/judge/en/problems/view/1610

MAX = 100001
visited = [0] * MAX
graph = [[] for _ in range(MAX)]
isCycle = False

def DFS(u):
  global isCycle
  visited[u] = 1
  if isCycle:
    return
  for v in graph[u]:
    if visited[v] == 1:
      isCycle = True
      return
    elif visited[v] == 0:
      DFS(v)
  visited[u] = 2

T = int(input())

for _ in range(T):
  V, E = map(int, input().split())

  for i in range(1, V + 1):
    graph[i].clear()
    visited[i] = 0

  for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)

  isCycle = False
  for j in range(1, V + 1):
    if visited[j] == 0:
      DFS(j)
    if isCycle:
      break
  if isCycle:
    print('SIM')
  else:
    print('NAO')