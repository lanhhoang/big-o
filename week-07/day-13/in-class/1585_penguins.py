# http://acm.timus.ru/problem.aspx?num=1585
# https://vjudge.net/problem/URAL-1585

n = int(input())
d = dict()
for _ in range(n):
  name = input()
  if name in d:
    d[name] += 1
  else:
    d[name] = 1

kind = ''
count = -1
for item in d.items():
  if item[1] > count:
    kind = item[0]
    count = item[1]
print(kind)