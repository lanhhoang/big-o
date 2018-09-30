# https://www.spoj.com/problems/STPAR/

def cars_check(n, cars):
  street = 1
  side_street = [] # stack

  for car in cars:
    if car == street:
      street += 1
    else:
      while len(side_street) != 0 and side_street[-1] == street:
        street += 1
        side_street.pop()
      if len(side_street) != 0 and side_street[-1] < car:
        break
      side_street.append(car)

  while len(side_street) != 0:
    if side_street[-1] == street:
      street += 1
    side_street.pop()
  
  if street == n + 1:
    print('yes')
  else:
    print('no')

while True:
  n = int(input())
  if n == 0:
    exit()

  cars = list(map(int, input().split()))
  cars_check(n, cars)