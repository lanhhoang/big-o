n = int(raw_input())
l = list(map(int, raw_input().split()))

print(l)

if len(l) <= 1:
  if l[0] == 0:
    print('NO')
  else:
    print('YES')
else:
  count = 0
  for i in range(len(l)):
    if l[i] == 1:
      count = count + 1  
  if count == len(l) - 1:
    print('YES')
  else:
    print('NO')
