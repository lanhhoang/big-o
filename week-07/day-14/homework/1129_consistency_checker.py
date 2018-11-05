# http://lightoj.com/volume_showproblem.php?problem=1129

class Node:
  def __init__(self):
    self.child = dict()
    self.countWord = 0
    self.count = 0

def addWord(root, s):
  tmp = root
  for ch in s:
    if ch not in tmp.child:
      tmp.child[ch] = Node()
    tmp = tmp.child[ch]
    tmp.count += 1
  tmp.countWord += 1

def findWord(root, s):
  tmp = root
  for ch in s:
    if ch in tmp.child:
      tmp = tmp.child[ch]
    if tmp.count > 1 and tmp.countWord == 1:
      return True
  return False

T = int(input())
for t in range(T):
  n = int(input())
  arr = []
  root = Node()
  res = 'YES'
  for _ in range(n):
    arr.append(input())
  for num in arr:
    addWord(root, num)
  for num in arr:
    if findWord(root, num) == True:
      res = 'NO'
      break
  print('Case {}: {}'.format(t + 1, res))