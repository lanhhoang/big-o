# https://www.spoj.com/problems/ARBITRAG/

def floyd_warshall(n, dist):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][j] < dist[i][k] * dist[k][j]:
          dist[i][j] = dist[i][k] * dist[k][j]
  for i in range(n):
    if dist[i][i] > 1:
      return True
  return False

case = 1
while True:
  V = int(input())
  if V == 0:
    break
  dist = [[0 for _ in range(V)] for _ in range(V)] # O(V ** 2)
  currencies = {}
  for i in range(V): # O(V)
    currency = input().strip()
    currencies[currency] = i
    dist[i][i] = float(1)
  E = int(input())
  for _ in range(E): # O(E)
    inp = input().split()
    c1, r, c2 = currencies[inp[0]], float(inp[1]), currencies[inp[2]]
    dist[c1][c2] = r
  res = floyd_warshall(V, dist) # O(V ** 3)
  if res == True:
    print('Case ' + str(case) + ': Yes')
  else:
    print('Case ' + str(case) + ': No')
  case += 1
  input()

# Complexity: O(T * V ** 3)