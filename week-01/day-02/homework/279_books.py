n, t = map(int, input().split())
minutes = list(map(int, input().split()))

l = 0
sum = 0
res = 0

for r in range(n):
  sum += minutes[r]

  while sum > t:
    sum -= minutes[l]
    l += 1

  res = max(res, r - l + 1)

print(res)
