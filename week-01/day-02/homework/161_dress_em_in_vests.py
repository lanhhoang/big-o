# Each i from 1 to n:
#   While j is smaller than m:
#     If j-th vest belongs to range [i-th size - x, i-th size + y]
#       Store i, j
#       Increase j by 1
#       Break
#     Else if j-th vest is larger than i-th size + y (that means j-th vest is too large for person i-th):
#       Break (current j-th vest is for bigger one, go to next person and check)
#     Otherwise (that means j-th vest is smaller than i-th size - x):
#       Increase j by 1 (current j-th vest is too small, go to next vest and check)

n, m, x, y = map(int, input().split())
desired = list(map(int, input().split()))
available = list(map(int, input().split()))

j = 0
res = []

for i in range(n):
  while j < m:
    if available[j] >= (desired[i] - x) and available[j] <= (desired[i] + y):
      res += [[i + 1, j + 1]]
      j += 1
      break
    elif available[j] > (desired[i] + y):
      break
    else:
      j += 1

print(len(res))
for k in res:
  print(k[0], k[1])
  