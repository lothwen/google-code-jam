from sys import stdin as i
 
def search(seq, val, i, j):
    if (i >= j):
        return False
    pos = (i + j) / 2
    if val > seq[pos]:
        return search(seq, val, pos + 1, j)
    if val < seq[pos]:
        return search(seq, val, i, pos)
    return True
 
for j in range(int(i.readline())):
    c = int(i.readline())
    t = int(i.readline())
    s1 = map(lambda x: int(x), i.readline().split(" "))
    s2 = sorted(s1)
    for x in range(t):
        if search(s2, c-s2[x], x+1, t):
            a = s1.index(s2[x])
            if c - s2[x] == s2[x]:
                b = s1.index(c-s2[x], a+1)
            else:
                b = s1.index(c-s2[x])
            print "Case #%d: %d %d" % (j+1, min(a,b)+1, max(a,b)+1)
            break
