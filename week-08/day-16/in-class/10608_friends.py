# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1549

MAX = 30005
parent = []
cnt = []
ranks = []

def makeSet():
  global parent, cnt, ranks
  parent = [i for i in range(MAX)]
  cnt = [1 for i in range(MAX)]
  ranks = [0 for i in range(MAX)]

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
    cnt[up] += cnt[vp]
  elif ranks[up] < ranks[vp]:
    parent[up] = vp
    cnt[vp] += cnt[up]
  else:
    parent[up] = vp
    cnt[vp] += cnt[up]
    ranks[vp] += 1

T = int(input())
for _ in range(T):
  N, M = map(int, input().split())
  makeSet()
  for _ in range(M):
    u, v = map(int, input().split())
    unionSet(u, v)
  print(max(cnt))