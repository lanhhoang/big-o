# Store all l values to list_l
# Store all r values to list_r
#
# Formally we will assume that segment [a, b] covers segment [c, d], if they meet this condition
# a ≤ c ≤ d ≤ b.
#
# Based on above condition, we gonna find min of all l and max of all r
# to find a segment [l, r] that may cover all segments
# l = min of list_l
# r = max of list_r
#
# Next we loop from 1 to n and compare the segment we have just found
# with all given segments by compare each list_l element with l and each list_r element with r
# If there is a segment, print the index of segment

n = int(input())
list_l = []
list_r = []

for i in range(n):
  l, r = list(map(int, input().split()))
  list_l.append(l)
  list_r.append(r)

left = min(list_l)
right = max(list_r)
res = -1

for i in range(n):
  if list_l[i] == left and list_r[i] == right:
    res = i + 1

print(res)
