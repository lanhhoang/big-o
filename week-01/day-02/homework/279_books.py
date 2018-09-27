n, t = map(int, input().split())
minutes = list(map(int, input().split()))

l = 0
sum = 0
count = 0
res = 0

for r in range(n):
  sum += minutes[r]
  count += 1

  while sum > t:
    sum -= minutes[l]
    l += 1
    count -= 1

  res = max(res, count)

print(res)
