# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1524

parent = []
ranks = []

def makeSet(N):
  global parent, ranks
  parent = [i for i in range(N + 1)]
  ranks = [0 for i in range(N + 1)]

def findSet(u):
  if parent[u] != u:
    parent[u] = findSet(parent[u])
  return parent[u]

def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up == vp:
    return
  if ranks[up] > ranks[vp]:
    parent[vp] = up
  elif ranks[up] < ranks[vp]:
    parent[up] = vp
  else:
    parent[up] = vp
    ranks[up] += 1

N = None
M = None
case = 1
while True:
  N, M = map(int, input().split())
  if N == 0 and M == 0:
    break
  makeSet(N)
  for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    unionSet(u, v)
  count = 0
  for i in range(N):
    if i == findSet(i):
      count += 1
  print('Case {}: {}'.format(case, count))
  case += 1