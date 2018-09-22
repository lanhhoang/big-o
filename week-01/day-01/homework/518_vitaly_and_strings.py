# Reverse loop string s
# Check the very last character of s
# If s[i] equals to 'z'
#   Replace s[i] to 'a'
# Else
#   Increse s[i]
#   Break from loop
#
# If modified s is difference from t
#   Print modified s
# Else
#   Print 'No such string'

s = input()
t = input()

s_list = list(s)

for i in range(len(s) - 1, -1, -1):
  if s[i] == 'z':
    s_list[i] = 'a'
  else:
    s_list[i] = chr(ord(s[i]) + 1)
    break

res = ''.join(s_list)

if res != t:
  print(res)
else:
  print('No such string')
