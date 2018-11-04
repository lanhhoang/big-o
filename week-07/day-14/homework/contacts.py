# https://www.hackerrank.com/challenges/contacts/problem

class Node:
  def __init__(self):
    self.child = dict()
    self.count = 0

def addWord(root, s):
  tmp = root
  for ch in s:
    if ch not in tmp.child:
      tmp.child[ch] = Node()
    tmp = tmp.child[ch]
    tmp.count += 1

def findWord(root, s):
  tmp = root
  for ch in s:
    if ch not in tmp.child:
      return 0
    tmp = tmp.child[ch]
    if tmp == None:
      return 0
  return tmp.count

n = int(input())
root = Node()
for _ in range(n):
  operation = input().split()
  if operation[0] == 'add':
    addWord(root, operation[1])
  else:
    print(findWord(root, operation[1]))