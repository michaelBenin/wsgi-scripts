import itertools

allcons = list(itertools.combinations('bceioudfghjklmnpqrstvwxyz', 4))
allvowl = list(itertools.combinations('aeiou', 2))
listcons = []
allvowl = []
allsets = []
words = []

with open('corncob_lowercase.txt') as f:
 raw = f.readlines()

words = set([w.strip() for w in raw if len(w.strip()) <= 6]) 

for i in allcons:
 t = "".join(i)
 if t in words:
    print t
