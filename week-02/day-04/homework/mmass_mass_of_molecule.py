# https://www.spoj.com/problems/MMASS/

molecule = input().replace(' ', '')

ATOMS = {
  'H': 1,
  'C': 12,
  'O': 16
}

def mmass(molecule):
  stack = []
  mass = 0
  for c in molecule:
    if c.isalpha():
      stack.append(ATOMS[c])
    elif c == '(':
      stack.append(-1)
    elif c == ')':
      w = 0
      while stack[-1] != -1:
        w += stack.pop()
      stack.pop() # remove -1
      stack.append(w)
    elif c.isdigit():
      m = int(c) * stack.pop()
      stack.append(m)
  
  while len(stack) != 0:
    mass += stack.pop()
  
  print(mass)

mmass(molecule)