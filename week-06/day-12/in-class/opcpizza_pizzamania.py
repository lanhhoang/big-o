# https://www.spoj.com/problems/OPCPIZZA/
# Note: Each friend is guaranteed to have distinct amount of money

def binarySearch(a, left, right, x): # O(logN)
  while left <= right:
    mid = (left + right) // 2
    if x == a[mid]:
      return True
    elif x < a[mid]:
      right = mid - 1
    else:
      left = mid + 1
  return False

t = int(input())
for _ in range(t):
  n, price = map(int, input().split())
  money = list(map(int, input().split())) # O(N)
  money.sort() # O(NlogN)
  count = 0
  for m in money: # O(NlogN)
    x = price - m
    res = binarySearch(money, 0, n - 1, x)
    if res == True:
      count += 1
  print(count // 2)

# Complexity: O(T * NlogN)