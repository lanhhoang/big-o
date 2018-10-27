# https://www.spoj.com/problems/HACKRNDM/

def binarySearch(arr, left, right, x):
  while left <= right:
    mid = (left + right) // 2
    if x == arr[mid]:
      return True
    elif x < arr[mid]:
      right = mid - 1
    else:
      left = mid + 1
  return False

n, k = map(int, input().split())
numbers = list(map(int, input().split())) # O(N)
numbers.sort() # O(NlogN)
count = 0
for i in range(n): # O(NlogN)
  x = k + numbers[i]
  if binarySearch(numbers, i + 1, n - 1, x) == True:
    count += 1
print(count)

# Complexity: O(NlogN)