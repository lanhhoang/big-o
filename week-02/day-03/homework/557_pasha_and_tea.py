def inp():
  return map(int, input().split())

n, w = inp()
a = list(inp())

a.sort()

girls = a[:n]
boys = a[n:]

x = 0

if girls[0] * 2 > boys[0]:
  x = boys[0] / 2
else:
  x = girls[0]

total = 3 * x * n

if total > w:
  total = w

print(total)
