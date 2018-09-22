n = int(input())
minutes = list(map(int, input().split()))

last_interest = 0

for i in range(n):
  if last_interest + 15 < minutes[i]:
    print(last_interest + 15)
    exit()
  else:
    last_interest = minutes[i]

print(min(last_interest + 15, 90))
