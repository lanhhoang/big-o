# https://www.hackerearth.com/practice/data-structures/trees/binary-search-tree/practice-problems/algorithm/distinct-count/

T = int(input())

for _ in range(T):
  N, X = map(int, input().split())
  arr = set(map(int, input().split()))
  count = len(arr)
  if count == X:
    print('Good')
  elif count < X:
    print('Bad')
  else:
    print('Average')