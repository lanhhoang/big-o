# https://www.spoj.com/problems/PQUEUE/
#
# queue < pair < priority, index > > : to store the priority and index of the current job.
# priority_queue < priority > : to store the priorities in decreasing order.

from collections import deque
from heapq import heappush, heappop

class Job:
  def __init__(self, id, priority):
    self.id = id
    self.priority = priority

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  priorities = list(map(int, input().split()))
  q = deque([])
  pq = []
  for i in range(n):
    q.append(Job(i, priorities[i]))
    heappush(pq, -priorities[i])
  time = 1
  while True:
    first = q[0]
    if first.priority < -pq[0]:
      q.popleft()
      q.append(first)
    else:
      if first.id == m:
        print(time)
        break
      else:
        time += 1
        q.popleft()
        heappop(pq)