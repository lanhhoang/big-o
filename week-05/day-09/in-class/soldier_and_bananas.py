k, n, w = map(int, input().split())

total = k * w * (w + 1) // 2
if total >= n:
  print(total - n)
else:
  print(0)