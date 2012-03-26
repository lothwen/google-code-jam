# http://code.google.com/codejam/contest/351101/dashboard#s=p0
from sys import stdin as i
for j in range(int(i.readline())):
    c = int(i.readline())
    t = int(i.readline())
    l = [int(x) for x in i.readline().split(" ")]

    for x in range(t):
	for y in range(t):
	    if x is y: continue
	    if l[x] + l[y] == c:
                print "Case #%d: %d %d" % (j+1, x+1, y+1)
		break
	else:
            continue
        break


