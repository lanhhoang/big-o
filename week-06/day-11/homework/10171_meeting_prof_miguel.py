# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1112

INF = int(1e9)
n = 26

def alphabet_to_int(char):
  return ord(char) - 65

def int_to_alphabet(num):
  return chr(num + 65)

def floyd_warshall(dist):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]

while True:
  N = int(input())
  if N == 0:
    break
  yDist = [[INF for _ in range(n)] for _ in range(n)] # O(n)
  mDist = [[INF for _ in range(n)] for _ in range(n)] # O(n)
  for _ in range(N): # O(N)
    age_type, direction, start, end, cost = input().split()
    start = alphabet_to_int(start)
    end = alphabet_to_int(end)
    cost = int(cost)
    if age_type == 'Y':
      yDist[start][end] = cost
      if direction == 'B':
        yDist[end][start] = cost
    else:
      mDist[start][end] = cost
      if direction == 'B':
        mDist[end][start] = cost
  for i in range(n): # O(n)
    yDist[i][i] = 0
    mDist[i][i] = 0
  u, v = input().split()
  u = alphabet_to_int(u)
  v = alphabet_to_int(v)

  floyd_warshall(yDist) # O(n ** 3)
  floyd_warshall(mDist) # O(n ** 3)

  minDist = INF
  location = []
  for i in range(n): # O(n)
    if yDist[u][i] != INF and mDist[v][i] != INF and yDist[u][i] + mDist[v][i] < minDist:
      minDist = yDist[u][i] + mDist[v][i]

  if minDist == INF:
    print('You will never meet.')
  else:
    for i in range(n): # O(n)
      if yDist[u][i] + mDist[v][i] == minDist:
        location.append(int_to_alphabet(i))
    print(minDist, ' '.join(location))

# Complexity: O(T * n ** 3)