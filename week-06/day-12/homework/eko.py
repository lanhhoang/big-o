# https://www.spoj.com/problems/EKO/

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().split()))

def getCutted(height):
  sum = 0
  for h in heights:
    if h > height:
      sum += h - height
  return sum

left = 0
right = max(heights)
res = 0

while (left <= right):
  mid = left + (right - left) // 2
  if getCutted(mid) >= M:
    res = mid
    left = mid + 1
  else:
    right = mid - 1

print(res)