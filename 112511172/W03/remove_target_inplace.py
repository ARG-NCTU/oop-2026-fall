def remove_target(L, target):
  i = 0
  while i < len(L):
    if L[i] == target:
      L.pop(i)
    else:
      i += 1

L = [6, 6, 6, 6]
target = 6

remove_target(L, target)
print(L)