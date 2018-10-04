# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3359
# Debug: https://www.udebug.com/UVa/12207
# TLE in UVa
# AC in Algote

from queue import Queue

case = 1

while True:
  p, c = map(int, input().split())
  if p == 0 and c == 0:
    break

  q = Queue()
  q_size = min(p, c)
  for i in range(1, q_size + 1):
    q.put(i)

  print('Case ' + str(case) + ':')
  for i in range(c):
    command = input().split()
    if command[0] == 'N':
      tmp = q.get()
      q.put(tmp)
      print(tmp)
    else:
      q2 = Queue()
      x = int(command[1])
      q2.put(x)
      while q.empty() == False:
        tmp = q.get()
        if tmp != x:
          q2.put(tmp)
      q = q2
  case += 1
