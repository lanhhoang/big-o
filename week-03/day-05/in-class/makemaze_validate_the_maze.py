# https://www.spoj.com/problems/MAKEMAZE/

from queue import Queue

class Pair:
  x = 0
  y = 0
  def __init__(self, a, b):
    self.x = a
    self.y = b

def isValid(v, maze):
  return v.x >= 0 and v.x < m and v.y >= 0 and v.y < n and maze[v.x][v.y] == '.'

def BFS(start, end, maze):
  dh = [0, -1, 0, 1]
  dc = [1, 0, -1, 0]
  visited = [[False for xx in range(n)] for yy in range(m)]
  q = Queue()

  visited[start.x][start.y] = True
  q.put(start)

  while not q.empty():
    u = q.get()
    for k in range(4):
      v = Pair(u.x + dh[k], u.y + dc[k])
      if isValid(v, maze) and not visited[v.x][v.y]:
        visited[v.x][v.y] = True
        if v.x == end.x and v.y == end.y:
          return True
        q.put(v)
  return False

t = int(input())

for _ in range(t):
  m, n = map(int, input().split())

  maze = []
  for _ in range(m):
    maze.append(input())

  points = []
  for i in range(m):
    for j in range(n):
      if maze[i][j] == '.' and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
        points.append(Pair(i, j))
  
  if len(points) == 2:
    if BFS(points[0], points[1], maze):
      print('valid')
    else:
      print('invalid')
  else:
    print('invalid')