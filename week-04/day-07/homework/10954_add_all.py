# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1895
# If total cost is minimum then each cost must be minimum
# To achieve this, after each sum put sum to Priority Queue
# to make sure we will take minimum element to calculate

from queue import PriorityQueue

while True:
  N = int(input())
  if N == 0:
    break
  a = list(map(int, input().split()))
  h = PriorityQueue()
  for i in range(N):
    h.put(a[i])
  cost = 0
  while len(h.queue) > 1:
    first = h.get()
    second = h.get()
    sum = first + second
    h.put(sum)
    cost += sum
  print(cost)