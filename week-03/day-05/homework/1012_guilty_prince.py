# http://lightoj.com/volume_showproblem.php?problem=1012

from queue import Queue

class Pair:
  x = 0
  y = 0
  def __init__(self, a, b):
    self.x = a
    self.y = b

def isValid(z, maze):
  return z.x >= 0 and z.x < h and z.y >= 0 and z.y < w and maze[z.x][z.y] == '.'

def BFS(point, maze):
  dh = [-1, 1, 0, 0]
  dv = [0, 0, -1, 1]
  visited = [[False for yy in range(w)] for xx in range(h)]
  q = Queue()

  visited[point.x][point.y] = True
  q.put(point)
  count = 1

  while not q.empty():
    u = q.get()
    for k in range(4):
      z = Pair(u.x + dh[k], u.y + dv[k])
      if isValid(z, maze) and not visited[z.x][z.y]:
        visited[z.x][z.y] = True
        count += 1
        q.put(z)

  return count

t = int(input())

for case in range(1, t + 1):
  w, h = map(int, input().split())
  maze = []
  for _ in range(h):
    maze.append(input())

  for i in range(h):
    for j in range(w):
      if maze[i][j] == '@':
        start = Pair(i, j)

  total = BFS(start, maze)
  print('Case ' + str(case) + ': ' + str(total))