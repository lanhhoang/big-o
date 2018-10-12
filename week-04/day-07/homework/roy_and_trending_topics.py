# https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/roy-and-trending-topics-1/

# Using sort: O(NlogN)

import heapq

class Topic:
  def __init__(self, id = 0, z_score = 0, change = 0):
    self.id = id
    self.z_score = z_score
    self.change = change

  def __lt__(self, other):
    if (self.change > other.change) or (self.change == other.change and self.id > other.id):
      return True
    return False

N = int(input())

pq = []

for _ in range(N):
  ID, Z, P, L, C, S = map(int, input().split())
  new_Z = P * 50 + L * 5 + C * 10 + S * 20
  change = new_Z - Z
  topic = Topic(ID, new_Z, change)
  heapq.heappush(pq, topic)

for _ in range(5):
  topic = heapq.heappop(pq)
  print(topic.id, topic.z_score)