# NOTE: Below is time limit exceeded solution because Codeforces is overloaded
# and submitted solution is in queue a long time therefore I cannot finalize
# an accepted solution
#
# Get the number of segments to an integer
# Get all segments to an array
#
# Create a helper method called 'cover'
# This helper method receives 2 segments list1 and list2, then identify whether
# list1 covers list2 or not
#
# Initialize index variable which value is -1
# Loop from start to end of array of segments with index i
#   Initialize count variable which value is 0
#   Loop from start to end of array of segments with index j
#     If segments[i] equals to segments[j] skip to next iteration
#     If segments[i] covers segments[j]
#       Increase count by 1
#
#   After loop with j index finishes, if count equals to number of segments minus 1
#     Store current index plus 1 to initialized index variable at the beginning
#     Break from the loop with i
#
# Print index variable value

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
