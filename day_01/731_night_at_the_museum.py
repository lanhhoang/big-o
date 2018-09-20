name = list(raw_input())

pointer = ord('a')
count = 0

for c in name:
  dist = abs(pointer - ord(c))
  if dist < 13:
    count += dist
  else:
    count += 26 - dist
  pointer = ord(c)

print(count)