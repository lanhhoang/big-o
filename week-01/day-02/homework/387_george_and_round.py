n, m = map(int, input().split())
good = list(map(int, input().split()))
prepared = list(map(int, input().split()))

i = 0
j = 0
count = 0 # Number of good prepared problems

while i < n and j < m:
  if prepared[j] >= good[i]:
    i += 1
    j += 1
    count += 1
  else:
    j += 1

print(n - count)
