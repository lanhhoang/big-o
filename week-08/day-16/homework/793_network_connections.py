# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=734

from sys import stdin

parent = []

def makeSet(n):
  global parent
  parent = [i for i in range(n + 1)]

def findSet(u):
  while u != parent[u]:
    u = parent[u]
  return u

def unionSet(u, v):
  up = findSet(u)
  vp = findSet(v)
  parent[up] = vp

T = int(input())
input()
for t in range(T): # O(T)
  N = int(input())
  makeSet(N) # O(N)
  successful_ans = 0
  unsuccessful_ans = 0
  for line in stdin: # O(Q) - Q: number of queries
    if line == '\n':
      break
    inp = line.split()
    u, v = int(inp[1]), int(inp[2])
    if inp[0] == 'c':
      unionSet(u, v) # O(N)
    if inp[0] == 'q':
      up = findSet(u) # O(N)
      vp = findSet(v) # O(N)
      if up == vp:
        successful_ans += 1
      else:
        unsuccessful_ans += 1
  print('{},{}'.format(successful_ans, unsuccessful_ans))
  if t < T - 1:
    print()

# Complexity: O(T * Q * N)