# https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/bishu-and-his-girlfriend/

import math

MAX = 1001
dist = [-1] * MAX
graph = [[] for _ in range(MAX)]

def DFS(s):
  for v in graph[s]:
    if dist[v] == -1:
      dist[v] = dist[s] + 1
      DFS(v)

N = int(input())
for _ in range(N - 1):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

Q = int(input())
girls = [False] * (N + 1)
for _ in range(Q):
  x = int(input())
  girls[x] = True

start = 1
dist[start] = 0
DFS(start)

min_dist = math.inf
index = -1
for i in range(2, N):
  if dist[i] < min_dist and girls[i] == True:
    min_dist = dist[i]
    index = i

print(index)