# http://code.google.com/codejam/contest/32016/dashboard#s=p1
from sys import stdin as i

for j in range(int(i.readline())):
    n = i.readline() #flavors
    for k in range(int(i.readline())): #customers
        m = [int(x) for x in i.readline()[:-1].split(' ')][1:] #customer likes 
        print "Case #%d: %s" % ((j+1), m)
        

