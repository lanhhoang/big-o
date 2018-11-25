# http://lightoj.com/volume_showproblem.php?problem=1008

from math import ceil, sqrt

T = int(input())
for t in range(T):
  s = int(input())
  sq = ceil(sqrt(s))
  r = sq * sq - s
  if r < sq:
    y = r + 1
    x = sq
  else:
    x = 2 * sq - r - 1
    y = sq
  if sq & 1:
    x, y = y, x
  print('Case {}: {} {}'.format(t + 1, x, y))