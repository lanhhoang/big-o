# https://codeforces.com/problemset/problem/471/B

while True:
  try:
    n = int(input())
    tasks = list(enumerate(map(int, input().split()), 1)) # [(id, difficulty)]
    tasks.sort(key = lambda x: x[1]) # sort by id
    i = 0
    while i < n - 1:
      if tasks[i][1] == tasks[i + 1][1]:
        break
      i += 1
    j = i + 1
    while j < n - 1:
      if tasks[j][1] == tasks[j + 1][1]:
        break
      j += 1
    if j > n - 2:
      print('NO')
    else:
      print('YES')
      tasks = [str(id) for id, difficulty in tasks]
      print(' '.join(tasks))
      tasks[i], tasks[i + 1] = tasks[i + 1], tasks[i]
      print(' '.join(tasks))
      tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]
      print(' '.join(tasks))
  except:
    break