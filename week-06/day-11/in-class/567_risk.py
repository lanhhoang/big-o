# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=508

INF = int(1e9)
n = 20

def floyd_warshall(dist):
  for k in range(1, n + 1):
    for i in range(1, n + 1):
      for j in range(1, n + 1):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]

def format_number(num):
  if num >= 10:
    return str(num)
  return format(str(num), " >2s")

for case in range(1, 100000):
  try:
    dist = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
      dist[i][i] = 0
    for i in range(1, n):
      inp = list(map(int, input().split()))
      x, countries = inp[0], inp[1:]
      for j in countries:
        dist[i][j] = 1
        dist[j][i] = 1
    floyd_warshall(dist)

    print('Test Set #' + str(case))
    N = int(input())
    for _ in range(N):
      A, B = map(int, input().split())
      print(format_number(A) + ' to ' + format_number(B) + ': ' + str(dist[A][B]))
    print()
  except EOFError:
    break