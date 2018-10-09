# https://codeforces.com/problemset/problem/723/D

class Point:
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

class Lake:
  def __init__(self, points = [], count = 0):
    self.points = points
    self.count = count

  def __lt__(self, other):
    if self.count < other.count:
      return True
    return False

n, m, k = map(int, input().split())
land = []
for _ in range(n):
  land.append(input())

lakes = []
visited = [[False for xx in range(m)] for yy in range(n)]

def isValid(v, matrix):
  return v.x >= 0 and v.x < n and v.y >= 0 and v.y < m and matrix[v.x][v.y] == '.'

def onBorder(v):
  return v.x == 0 or v.x == n - 1 or v.y == 0 or v.y == m - 1

def DFS(start):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  points = [Point(start.x, start.y)]
  stack = []
  stack.append(start)
  visited[start.x][start.y] = True
  isOcean = False

  while len(stack) != 0:
    u = stack.pop()
    if onBorder(u):
      isOcean = True
    for z in range(4):
      v = Point(u.x + dx[z], u.y + dy[z])
      if isValid(v, land) and not visited[v.x][v.y]:
        visited[v.x][v.y] = True
        points.append(v)
        stack.append(v)
  if not isOcean:
    lake = Lake(points, len(points))
    lakes.append(lake)
  
for i in range(n):
  for j in range(m):
    if land[i][j] == '.' and not visited[i][j]:
      DFS(Point(i, j))

lakes.sort()
ncells = 0

for i in range(len(lakes) - k):
  ncells += lakes[i].count
  for j in range(lakes[i].count):
    ux, uy = lakes[i].points[j].x, lakes[i].points[j].y
    land[ux] = land[ux][:uy] + '*' + land[ux][uy+1:]

print(ncells)
for z in range(n):
  print(land[z])