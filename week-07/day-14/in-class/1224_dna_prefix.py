# http://lightoj.com/volume_showproblem.php?problem=1224

class Node:
  def __init__(self):
    self.child = dict()
    self.value = 0
    

def addWord(root, s):
  tmp = root
  for ch in s:
    if ch not in tmp.child:
      tmp.child[ch] = Node()
    tmp = tmp.child[ch]
    tmp.value += 1

def findWord(root, s):
  tmp = root
  len = 0
  max_value = 0
  for ch in s:
    if ch in tmp.child:
      tmp = tmp.child[ch]
    len += 1
    max_value = max(max_value, tmp.value * len)
  return max_value

T = int(input())
for t in range(T):
  n = int(input())
  root = Node()
  arr = []
  res = 0
  for _ in range(n):
    arr.append(input())
  for dna_string in arr:
    addWord(root, dna_string)
  for dna_string in arr:
    res = max(res, findWord(root, dna_string))
  print("Case {}: {}".format(t + 1, res))