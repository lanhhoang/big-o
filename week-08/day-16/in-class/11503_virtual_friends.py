# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2498

MAX = 100010
parent = []
cnt = []

def makeSet():
  global parent, cnt, ranks
  parent = [i for i in range(MAX)]
  cnt = [1 for i in range(MAX)]

def findSet(u):
  if u == parent[u]:
    return u
  parent[u] = findSet(parent[u])
  return parent[u]

def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  if up != vp:
    parent[vp] = up
    cnt[up] += cnt[vp]
  print(cnt[up])

T = int(input())
for _ in range(T):
  F = int(input())
  friendships = []
  friends = dict()
  id = 0
  for _ in range(F):
    u, v = input().split()
    friendships.append([u, v])
    if u not in friends:
      friends[u] = id
      id += 1
    if v not in friends:
      friends[v] = id
      id += 1
  makeSet()
  for friendship in friendships:
    u, v = friends[friendship[0]], friends[friendship[1]]
    unionSet(u, v)