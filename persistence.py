import math as m
import itertools as i

pwrs2 = []
pwrs3 = []
pwrs7 = []

r = range(0,100000)

for c in r:
    pw = 7**c
    pwrs7.append(pw)
    pw = 3**c
    pwrs3.append(pw)
    pw = 2**c
    pwrs2.append(pw)
    print(c,"completo")

n = 12

rr = range(99999,-1,-1)

for p in i.product(rr, repeat=3):
    droot = pwrs7[p[0]]*pwrs3[p[1]]*pwrs2[p[2]]
    count = 1
    print(p)
    while count < n:
        string = [int(dig) for dig in str(droot)]
        if len(string) == 1:
            break
        elif string.count(0) > 0:
            if count == n-1:
                t = open("perst.csv","a")
                t.write("!"+str(p)+" ("+str(m.fsum(p))+")\n")
                t.close()
                break
            else:
                break
        elif string.count(5) > 0:
            if count >= n-2:
                t = open("perst.csv","a")
                t.write("!!"+str(p)+" ("+str(m.fsum(p))+")\n")
                t.close()
                break
            else:
                break
        else:
            droot = m.prod(string)
            count += 1
    if count == n:
        t = open("perst.csv","a")
        t.write(str(p)+" ("+str(m.fsum(p))+")\n")
        t.close()
