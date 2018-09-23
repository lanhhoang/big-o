n, k = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = [0] * int(1e5 + 1)
count_k = 0
left = 0

for right in range(n):
  cnt[numbers[right]] += 1

  if cnt[numbers[right]] == 1:
    count_k += 1

  while count_k == k:
    cnt[numbers[left]] -= 1

    if cnt[numbers[left]] == 0:
      print(left + 1, right + 1)
      exit()
    else:
      left += 1

print(-1, -1)
