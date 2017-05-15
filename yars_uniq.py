#!/usr/bin/env python
import rdflib
import string
import hashlib
import sys
from urlparse import urlparse
g=rdflib.Graph()
g.parse(sys.argv[1]+".ttl", format="turtle")
vertexes = []
for s,p,o in g:
  s = s.encode('utf-8',errors='ignore')
  p = p.encode('utf-8',errors='ignore')
  o = o.encode('utf-8',errors='ignore')
  if s != o:
    sh = hashlib.md5(s).hexdigest()
    shu = "(\na" + sh + "\n{\nv:\n'" + s + "'\n}\n)"
    oh = hashlib.md5(o).hexdigest()
    ohu = "(\na" + oh + "\n{\nv:\n'" + o + "'\n}\n)"
    if(shu not in vertexes):
      vertexes.append(shu)
      print shu
    if(ohu not in vertexes):
      vertexes.append(ohu)
      print ohu
    print "(\na" + sh + "\n)\n-[\n" + p + "\n]->\n(\na" + oh + "\n)"

