# https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/search-engine/

class Node:
  def __init__(self):
    self.child = dict()
    self.countWord = 0
    self.maxValue = 0

def addWord(root, s, value):
  tmp = root
  for ch in s:
    if ch not in tmp.child:
      tmp.child[ch] = Node()
    tmp = tmp.child[ch]
    tmp.maxValue = max(tmp.maxValue, value)
  tmp.countWord += 1

def findWord(root, s):
  tmp = root
  for ch in s:
    if ch not in tmp.child:
      return -1
    tmp = tmp.child[ch]
  return tmp.maxValue

n, q = map(int, input().split())
root = Node()
for _ in range(n):
  inp = input().split()
  word, weight = inp[0], int(inp[1])
  addWord(root, word, weight)
for _ in range(q):
  t = input()
  res = findWord(root, t)
  print(res)