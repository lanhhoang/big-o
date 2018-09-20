s = input()
t = input()
length = len(s)

if length == 1:
  dist = abs(ord(t) - ord(s))
  if dist > 1:
    print(chr(ord(s) + 1))
  else:
    print('No such string')
else:
  s_clone = list(s)
  for i in range(length - 1, -1, -1):
    dist = abs(ord(t[i]) - ord(s[i]))
    if dist >= 0:
      if s[i] == 'z':
        s_clone[i] = 'a'
      else:
        s_clone[i] = chr(ord(s[i]) + 1)
    if ''.join(s_clone) > s and ''.join(s_clone) < t:
      print(''.join(s_clone))
      exit()
  print('No such string')