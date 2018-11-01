# https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1167

from sys import stdin
input = stdin.readline

T = int(input())
input()
for t in range(T):
  species = dict()
  count = 0
  for line in stdin:
    if line == '\n':
      break
    line = line.strip()
    count += 1
    if line in species:
      species[line] += 1
    else:
      species[line] = 1
  sorted_species = {k: species[k] for k in sorted(species)}
  for item in sorted_species.items():
    name = item[0]
    population = "{:.4f}".format(item[1] / count * 100)
    print(name, population)
  if t < T - 1:
    print()