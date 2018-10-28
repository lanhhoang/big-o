# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=316&page=show_problem&problem=1552

def lowerBound(arr, left, right, x): # O(logN)
  pos = right
  while left < right:
    mid = (left + right) // 2
    if arr[mid] >= x:
      pos = mid
      right = mid
    else:
      left = mid + 1
  return pos

def upperBound(arr, left, right, x): # O(logN)
  pos = right
  while left < right:
    mid = (left + right) // 2
    if arr[mid] > x:
      pos = mid
      right = mid
    else:
      left = mid + 1
  return pos


N = int(input())
heights = list(map(int, input().split())) # O(N)
Q = int(input())
queries = list(map(int, input().split())) # O(Q)

shorter = 0
taller = 0

for q in queries: # O(Q)
  lower = lowerBound(heights, 0, N - 1, q)
  upper = upperBound(heights, 0, N - 1, q)
  if q > heights[N - 1]:
    shorter = heights[N - 1]
    taller = 'X'
  elif q == heights[N - 1]:
    shorter = heights[lower - 1]
    taller = 'X'
  elif q < heights[0]:
    shorter = 'X'
    taller = heights[0]
  elif q == heights[0]:
    shorter = 'X'
    taller = heights[upper]
  else:
    shorter = heights[lower - 1]
    taller = heights[upper]
  print(shorter, taller)
  
# Complexity: O(QlogN) ~ O(NlogN)