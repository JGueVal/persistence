from math import prod

PERS = 12
ran = range(99999, -1, -1)

pwrs9 = []
pwrs8 = []
pwrs7 = []
pwrs6 = [1, 6]
pwrs3 = [1, 3]
pwrs2 = [1, 2, 4]

for c in range(100000):
    pw = 9**c
    pwrs9.append(pw)
    pw = 8**c
    pwrs8.append(pw)
    pw = 7**c
    pwrs7.append(pw)
    print(f'{c} completo')

def docprint():
    with open('perst.txt', 'a') as t:
        t.write(f'{p9} 9s, {p8} 8s, {p7} 7s, {p6} 6s, {p3} 3s, {p2} 2s\n')

#   Se puede usar itertools, pero es conveniente esto en caso de querer interrumpir el programa.
#   EJEMPLO: "if p9 > 99997: continue", "if p9 >= 99997 and p8 > 65535: continue".

for p9 in ran:
    for p8 in ran:
        for p7 in ran:
            for p6 in range(2):
                for p3 in range(2):
                    for p2 in range(3):
                        if p9+p8+p7+p6+p3+p2 < 20000:
                            continue
                        droot = pwrs9[p9] * pwrs8[p8] * pwrs7[p7] * pwrs6[p6] * pwrs3[p3] * pwrs2[p2]
                        count = 1
                        print(f'{p9}, {p8}, {p7}, {p6}, {p3}, {p2}')
                        while count < PERS:
                            string = [int(dig) for dig in str(droot)]
                            if len(string) == 1:
                                break
                            elif string.count(0) > 0:
                                if count == PERS-1:
                                    docprint()
                                    break
                                break
                            elif string.count(5) > 0:
                                if count >= PERS-2:
                                    docprint()
                                    break
                                break
                            droot = prod(string)
                            count += 1
                        if count == PERS:
                            docprint()
