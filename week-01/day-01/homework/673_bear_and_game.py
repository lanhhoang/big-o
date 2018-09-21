n = int(input())
minutes = list(map(int, input().split()))

start_minute = 1
end_minute = 90

if n <= 1:
  length = minutes[0] - start_minute
  if length >= 15:
    print(15)
  else:
    print(minutes[0] + 15)
else:
  for i in range(n):
    if i == 0:
      length = minutes[i] - start_minute
      if length >= 15:
        print(15)
        exit()
    else:
      length = minutes[i] - minutes[i - 1]
      if length > 15:
        print(minutes[i - 1] + 15)
        exit()
  
  if (end_minute - minutes[-1]) < 15:
    print(90)
  else:
    print(minutes[-1] + 15)