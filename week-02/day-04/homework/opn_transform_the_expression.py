# https://www.spoj.com/problems/ONP/
# Reference: https://en.wikipedia.org/wiki/Shunting-yard_algorithm

n = int(input())
expressions = []
for i in range(n):
  expressions.append(input())

for i in range(n):
  s = list(expressions[i])
  stack = []
  res = []

  for i in range(len(s)):
    if s[i] >= 'a' and s[i] <= 'z':
      res.append(s[i])
    elif s[i] == '(':
      continue
    else:
      if s[i] != ')':
        stack.append(s[i])
      elif len(stack) != 0 and s[i] == ')':
        res.append(stack[-1])
        stack.pop()

  print(''.join(res))