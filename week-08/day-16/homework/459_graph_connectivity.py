# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=400

from sys import stdin

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

def char_to_int(char):
  return ord(char) - 65

T = int(input())
input()
for t in range(T): # O(T)
  N = char_to_int(input())
  makeSet(N) # O(N)
  for line in stdin: # O(M) - M: number of paths
    if line == '\n':
      break
    u, v = map(char_to_int, list(line.strip()))
    unionSet(u, v) # O(logN)
  count = 0
  for i in range(N + 1): # O(N)
    if i == findSet(i): # O(logN)
      count += 1
  print(count)
  if t < T - 1:
    print()

# Complexity: O(T * (M + N)logN)