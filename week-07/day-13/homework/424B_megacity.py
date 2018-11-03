# http://codeforces.com/problemset/problem/424/B

from math import sqrt

MEGA_POPULATION = int(1e6)

class Location:
  def __init__(self, x, y, population):
    self.x = x
    self.y = y
    self.population = population
    self.dist = sqrt(x ** 2 + y ** 2)

n, population = map(int, input().split())
locations = []
for _ in range(n):
  x, y, k = map(int, input().split())
  locations.append(Location(x, y, k))

locations.sort(key=lambda l: l.dist)
radius = -1
for location in locations:
  x, y, k, r = location.x, location.y, location.population, location.dist
  if population + k >= MEGA_POPULATION:
    radius = r
    break
  else:
    population += k
    
print('{:.7f}'.format(radius))