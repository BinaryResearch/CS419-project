#!/usr/bin/python3

import itertools

a = ['a','b','c','d','e','f','g','h']
b = ['1','2','3','4','5','6','7','8']

c = list(itertools.product(a,b))
for i in c:
    print('"' + i[0] + ',' + i[1] + '"')

for i in range(len(c)):
    a = c[i][0] + "," + c[i][1]
    b = c[i+1][0] + "," + c[i+1][1]
    print(a + " " + b) 
