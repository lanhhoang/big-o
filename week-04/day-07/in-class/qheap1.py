# https://www.hackerrank.com/challenges/qheap1/problem

from queue import PriorityQueue

h = PriorityQueue()
h_remove = PriorityQueue()

Q = int(input())
for i in range(Q):
  query = input().split()
  if query[0] == str(1):
    h.put(int(query[1]))
  elif query[0] == str(2):
    h_remove.put(int(query[1]))
  else:
    while not h_remove.empty() and h.queue[0] == h_remove.queue[0]:
      h.get()
      h_remove.get()
    print(h.queue[0])