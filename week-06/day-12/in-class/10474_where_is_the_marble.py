# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1415

def bsFirst(arr, left, right, x): # O(logN)
  while left <= right:
    mid = (left + right) // 2
    if (mid == left or x > arr[mid - 1]) and arr[mid] == x:
      return mid
    elif x > arr[mid]:
      return bsFirst(arr, mid + 1, right, x)
    else:
      return bsFirst(arr, left, mid - 1, x)
  return -1

case = 1
while True:
  N, Q = map(int, input().split())
  if N == 0 and Q == 0:
    break
  marbles = []
  queries = []
  for _ in range(N): # O(N)
    marbles.append(int(input()))
  marbles.sort() # O(NlogN)
  print('CASE# ' + str(case) + ':')
  for _ in range(Q): # O(QlogN) ~ O(NlogN)
    q = int(input())
    index = bsFirst(marbles, 0, len(marbles) - 1, q)
    if index != -1:
      print(str(q) + ' found at ' + str(index + 1))
    else:
      print(str(q) + ' not found')
  case += 1

# Complexity: O(T * NlogN)