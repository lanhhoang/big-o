# In case of length of s and t equal 1
#   Calculate difference between s and t
#   If difference is larger than 1
#     Print next alphabet character in ASCII table
#   Else
#     Print 'No such string'
# Else
#   Create a new string which is a clone of s
#   Loop from start to end of both string s and t
#     Calculate absolute difference between s[i] and t[i]
#     If difference is larger than or equal to 0
#       Identify next alphabet character
#       If s[i] equal to 'z'
#         Replace current character of clone string with 'a'
#       Else
#         Replace current character of clone string with next alphabet character in ASCII table
#     Compare clone string with s and t
#       If clone string is larger than s and smaller than t
#         Print clone string
#         Exit from program
#
#   If there is no such string are printed while looping
#     Print 'No such string'

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