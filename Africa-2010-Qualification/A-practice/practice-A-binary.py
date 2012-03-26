# http://code.google.com/codejam/contest/351101/dashboard#s=p0
from sys import stdin as i

def binary_search(l, k, imin, imax):
    while imin <= imax:
        imid = (imax + imin) / 2
        if l[imid] > k:
            imax = imid - 1
        elif l[imid] < k:
            imin = imid + 1
        else:
            return imid

for j in range(int(i.readline())):
    c = int(i.readline())
    t = int(i.readline())
    l = [int(x) for x in i.readline().split(" ")]
    l2 = sorted(l)

    for k in range(t):
        founded = binary_search(l2, (c-l2[k]), k+1, t-1)
        if founded:
            a = l.index(l2[k]) 
            if c - l[a] == l[a]:
                b = l.index(l2[founded], a+1)
            else:
                b = l.index(l2[founded])
            print "Case #%d: %d %d" % (j+1, min(a,b)+1, max(a,b)+1)
            break 

