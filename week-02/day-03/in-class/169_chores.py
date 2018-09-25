n, a, b = map(int, input().split())
chores = list(map(int, input().split()))

chores.sort()
first = chores[:b]
second = chores[b:n]

x = second[0] - first[len(first) - 1]

print(x)
