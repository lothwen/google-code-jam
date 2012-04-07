# http://code.google.com/codejam/contest/90101/dashboard#s=p0
from sys import stdin as i
import re

l, d, n = i.readline().split()
words = [i.readline().rstrip() for x in range(int(d))]

for j in range(int(n)):
    case = i.readline().rstrip().replace('(','[').replace(')',']')
    print "Case #%d: %s" % ((j+1), len(filter(lambda w: re.match(case, w), words)))
