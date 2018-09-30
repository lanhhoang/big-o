# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1876

import queue
import sys
input = sys.stdin.readline

q = queue.Queue()

while True:
  n = int(input())
  if n==0:
    break
  for i in range(1,n+1):
    q.put(i)
  print('Discarded cards:',end='')
  while q.qsize() > 2:
    print(' %d,' % q.get(),end='')
    q.put(q.get())
  if q.qsize() == 1:
    print('\nRemaining card: %d' % q.get())
    continue
  print(" %d" % q.get())
  print('Remaining card: %d' % q.get())