def inp():
  return map(int, input().split())

n = int(input())
ratings = list(inp())

ranks = [0] * n

# Solution 2: Complexity O(nlogn)
class Student:
  def __init__(self, id = 0, rating = 0):
    self.id = id
    self.rating = rating

  def __lt__(self, other):
    if (self.rating > other.rating) or (self.rating == other.rating and self.id < other.id):
      return True
    else:
      return False

students = []

for i in range(n):
  students.append(Student(i, ratings[i]))

students.sort()

ranks[students[0].id] = 1

for i in range(1, n):
  if students[i].rating == students[i - 1].rating:
    ranks[students[i].id] = ranks[students[i - 1].id]
  else:
    ranks[students[i].id] = i + 1

print(' '.join(map(str, ranks)))

# Solution 1: Complexity O(n^2)

# for i in range(n):
#   rank = 1
#   for j in range(n):
#     if ratings[j] > ratings[i]:
#       rank += 1
  
#   ranks[i] = rank

# print(' '.join(map(str, ranks)))
