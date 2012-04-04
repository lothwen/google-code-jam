# http://code.google.com/codejam/contest/32016/dashboard#s=p2
from sys import stdin as i

for t in range(int(i.readline())):
    print "Case #%d: %03d" % ((t+1), int(str(int(5.23606797749979 ** int(i.readline())))[-3:])) 

