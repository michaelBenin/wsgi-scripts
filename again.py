import itertools
allcons = list(itertools.combinations('bcdfghjklmnpqrstvwxyz', 4))
allvowl = list(itertools.combinations('aeiou', 2))
listcons = []
allvowl = []
allsets = []

for i in allcons:
  t = list(i)
  listcons.append(t)

for i in allvowl:
  t = list(i)
  allvowl.append(t)

for i in listcons: 
  allsets.append(i+allvowl[i])
print(allsets)
