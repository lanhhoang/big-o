n = int(input())
segments = []

for i in range(n):
  segment = list(map(int, input().split()))
  segments.append(segment)

def cover(list1, list2):
  return list1[0] <= list2[0] and list2[0] <= list2[1] and list2[1] <= list1[1]

def big_segment(n, segments):
  index = -1
  for i in range(n):
    count = 0
    for j in range(n):
      if segments[i] == segments[j]: continue
      if cover(segments[i], segments[j]):
        count += 1
    if count == n - 1:
      index = i + 1
      break
  print(index)

big_segment(n, segments)
