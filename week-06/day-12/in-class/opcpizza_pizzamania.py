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
  for i in range(n): # O(NlogN)
    x = price - money[i]
    if binarySearch(money, i + 1, n - 1, x) == True:
      count += 1
  print(count)

# Complexity: O(T * NlogN)