# https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/monk-and-multiplication/

from queue import PriorityQueue

N = int(input())
A = list(map(int, input().split()))

h = PriorityQueue()
for i in range(N):
  if i < 2:
    print(-1)
    h.put(-A[i])
  else:
    h.put(-A[i])
    first = -h.get()
    second = -h.get()
    third = -h.get()
    print(first * second * third)
    h.put(-first)
    h.put(-second)
    h.put(-third)