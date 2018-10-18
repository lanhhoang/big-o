# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1594
# Reference: https://www.geeksforgeeks.org/shortest-distance-two-cells-matrix-grid/
# TLE for Python

from collections import deque

class Point:
  def __init__(self, a, b, t = 0):
    self.x = a
    self.y = b
    self.time = t

def isValid(v, matrix):
  return v.x >= 0 and v.x < R and v.y >= 0 and v.y < C and matrix[v.x][v.y] == '.'

def BFS(start, end, matrix):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  visited = [[False for yy in range(C)] for xx in range(R)]
  queue = deque([])

  visited[start.x][start.y] = True
  queue.append(start)

  while len(queue) != 0:
    u = queue.popleft()
    if u.x == end.x and u.y == end.y:
      print(u.time)
      return
    for k in range(4):
      v = Point(u.x + dx[k], u.y + dy[k], u.time + 1)
      if isValid(v, matrix) and not visited[v.x][v.y]:
        visited[v.x][v.y] = True
        queue.append(v)

while True:
  R, C = map(int, input().split())
  if R == 0 and C == 0:
    break
  bombs_R = int(input())
  land = [['.' for yy in range(C)] for xx in range(R)]

  for _ in range(bombs_R):
    inp = input().split()
    r, n, c = int(inp[0]), int(inp[1]), list(map(int, inp[2:]))
    for i in range(n):
      land[r][c[i]] = '#'

  x, y = map(int, input().split())
  src = Point(x, y)
  x, y = map(int, input().split())
  dest = Point(x, y)

  BFS(src, dest, land)