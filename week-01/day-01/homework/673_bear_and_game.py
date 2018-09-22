# Get the number of minutes to an integer
# Get interesting minutes to an array
#
# In case of number of interesting minutes is smaller than or equal to 1
#   Calculate difference between interesting minute and start minute which is 1
#   If difference is larger than or equal to 15
#     Print 15
#   Else
#     Print total of given interesting minute plus 15
# Else
#   Loop from start to end of interesting minutes array
#     In case of first element
#       Calculate difference between first minute and start minute which is 1
#       If difference is larger than or equal to 15
#         Print 15
#         Exit from program
#     Else
#       Calculate difference between minute at index i and minute at index i - 1
#       If difference is larger than 15
#         Print total of minute at index i - 1 plus 15
#         Exit from program
#
#   If there is no such number is printed while looping
#     Calculate difference between last minute and end minute which is 90
#     If difference is smaller than 15
#       Print 90
#     Else
#       Print total of last minute plus 15

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