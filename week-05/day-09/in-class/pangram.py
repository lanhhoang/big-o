# http://codeforces.com/problemset/problem/520/A

n = int(input())
s = input()

s = s.lower()
alphabet = {}
count = 0

for i in range(n):
  if alphabet.get(s[i]) == None:
    alphabet[s[i]] = 1
    count += 1
  else:
    alphabet[s[i]] += 1

if count == 26:
  print('YES')
else:
  print('NO')