def inp():
  return map(int, input().split())

n = int(input())
ratings = list(inp())

# Solution 1: Complexity O(n^2)

# ranks = [0] * n

# for i in range(n):
#   rank = 1
#   for j in range(n):
#     if ratings[j] > ratings[i]:
#       rank += 1
  
#   ranks[i] = rank

# print(' '.join(map(str, ranks)))
