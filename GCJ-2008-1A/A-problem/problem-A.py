# http://code.google.com/codejam/contest/32016/dashboard#s=p0
from sys import stdin as i
from operator import mul

for j in range(int(i.readline())):
    n = i.readline()
    l1 = [int(x) for x in i.readline().split(' ')]
    l2 = [int(x) for x in i.readline().split(' ')]
    print "Case #%d: %d" % ((j+1), sum(map(mul,sorted(l1),reversed(sorted(l2)))))
