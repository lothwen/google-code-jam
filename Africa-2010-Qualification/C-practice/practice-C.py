# http://code.google.com/codejam/contest/351101/dashboard#s=p2
from sys import stdin as i

d = {
    'a': '2',        
    'b': '22',        
    'c': '222',        
    'd': '3',        
    'e': '33',        
    'f': '333',        
    'g': '4',        
    'h': '44',        
    'i': '444',        
    'j': '5',        
    'k': '55',        
    'l': '555',        
    'm': '6',        
    'n': '66',        
    'o': '666',        
    'p': '7',        
    'q': '77',        
    'r': '777',        
    's': '7777',        
    't': '8',        
    'u': '88',        
    'v': '888',        
    'w': '9',        
    'x': '99',        
    'y': '999',        
    'z': '9999',
    ' ': '0'
}
for j in range(int(i.readline())):
    res = ''
    for c in i.readline()[:-1]:
        if len(res) and res[-1]  == d[c][0]: res += ' '
        res += d[c]
    
    print "Case #%d: %s" % ((j+1), res)
