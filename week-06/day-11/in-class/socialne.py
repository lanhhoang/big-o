# https://www.spoj.com/problems/SOCIALNE/

INF = int(1e9)  

def floyd_warshall(dist):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]

T = int(input())

for _ in range(T):
  line = list(input())
  n = len(line)
  matrix = [line]
  for i in range(1, n):
    matrix.append(list(input()))
  dist = [[None for _ in range(n)] for _ in range(n)]
  for i in range(n):
    line = matrix[i]
    for j in range(n):
      if i == j:
        dist[i][j] = 0
      else:
        if line[j] == 'Y':
          dist[i][j] = 1
        else:
          dist[i][j] = INF
  floyd_warshall(dist)
  maxFriend = 0
  minId = 0
  for i in range(n):
    count = 0
    for j in range(n):
      if dist[i][j] == 2:
        count += 1
    if count > maxFriend:
      maxFriend = count
      minId = i
  print(minId, maxFriend)