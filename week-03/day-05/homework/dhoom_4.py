# https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/dhoom-4/

from queue import Queue

MAX = 100001
dist = [-1] * MAX

key, lock = map(int, input().split())
n = int(input())
values = list(map(int, input().split()))

q = Queue()
dist[key] = 0
q.put(key)

while not q.empty():
  u = q.get()
  for k in values:
    v = (u * k) % 100000
    if dist[v] == -1:
      dist[v] = dist[u] + 1
      q.put(v)
  if dist[lock] != -1:
    break
print(dist[lock])