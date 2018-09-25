n, m = map(int, input().split())
good = list(map(int, input().split()))
prepared = list(map(int, input().split()))

i = 0
j = 0

while i < n and j < m:
  if prepared[j] >= good[i]:
    i += 1
    j += 1
  else:
    j += 1

print(n - i)
