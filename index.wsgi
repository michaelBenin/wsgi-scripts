import json
import urllib.request
import random
import itertools

def application(environ, start_response):
   
    allcons = list(itertools.combinations('bcdfghjklmnpqrstvwxyz', 4))
    allvowl = list(itertools.combinations('aeiou', 2))
    listcons = []
    allvowls = []	
    allsets = []
    
    for i in allcons:
        t = list(i)
        listcons.append(t)

    for i in allvowl:
        t = list(i)
        allvowls.append(t)

    for i in listcons:
        for v in allvowls:
            z = i+v
            allsets.append(z)
    
#   '''with open('corncob_lowercase.txt') as f:
 #        raw = f.readlines()
   #  words = set([w.strip() for w in raw if len(w.strip()) <= 6])
    # words = []
    # e = {}
    # for i in allsets:
      #   b = []
        # c = []
       #  t = "".join(i)
       #  x = itertools.permutations(t, 3)
       #  y = itertools.permutations(t, 4)
       #  z = itertools.permutations(t, 5)
       #  a = itertools.permutations(t, 6)
       #  for e in x:
       #      b.append("".join(e))
       #  for e in y:
       #      b.append("".join(e))
       #  for e in z:
        #     b.append("".join(e))
        # for e in a:
         #    b.append("".join(e))
       #  for i in b:
         #    if i in words:
          #       c.append(i)                
        # e[t]=c
    # r = json.dump(e)'''
    screen = str(allsets)
    req = urllib.request.urlopen('http://words.bighugelabs.com/api/2/8d3479c49640d29f2222950de32e83ff/word/json')
    reqbytes = req.read()
    reqdec = reqbytes.decode("utf8")
    jsonreq = json.dumps(reqdec)      
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(screen)))]
    start_response(status, response_headers)

    return [screen]
