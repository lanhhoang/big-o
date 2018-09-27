def inp():
  return map(int, input().split())

n, x = inp()
c = list(inp())

c.sort()

total = 0

for i in range(n):
  total += c[i] * x
  if x > 1:
    x -= 1

print(total)