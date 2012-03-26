# http://code.google.com/codejam/contest/351101/dashboard#s=p1
import sys

input = sys.stdin

n = int(input.readline().strip())

for i in range(n):
    l = list(input.readline().strip().split(' '))
    l.reverse()
    print "Case #%d: %s" % ((i+1), " ".join(l))

''' abeaumont's implementation
from sys import stdin as i
for j in range(int(i.readline())):
    print "Case #%d: %s" % (j+1, ' '.join(reversed(i.readline()[:-1].split(' '))))

'''

