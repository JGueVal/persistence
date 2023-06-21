from math import prod
from random import sample

PERST = 12
r = range(100000)

pwrs9 = [9**p9 for p9 in r]
pwrs8 = [8**p8 for p8 in r]
pwrs7 = [7**p7 for p7 in r]
pwrs3 = [1, 3]
pwrs2 = [1, 2, 4]

r = range(99999, -1, -1)
#r = sample(r,len(r))    # aleatorio


def docPrint(doc):
    print(f'{p9}_{p8}_{p7}_{p3}_{p2}___________')
    with open(doc, 'a') as t:
        t.write(f'{p9} 9s, {p8} 8s, {p7} 7s, {p3} 3s, {p2} 2s\n')

# A veces me ha saltado un error en escritura en ficheros, y no sé replicarlo.
def tryDocPrint():
    try:
        docPrint('perst.txt')
    except:
        try:
            docPrint('perstB.txt')
        except:
            print(f'ERROR at: {p9}_{p8}_{p7}_{p3}_{p2}___________')


# He intentado usar el multithreading,
# ocurría que no paraba de aumentar la escritura en RAM.
# Algún día lo volveré a intentar.

for p9 in r:
    for p8 in r:
        m1 = pwrs9[p9] * pwrs8[p8]
        for p7 in r:
            m2 = m1 * pwrs7[p7]
            for p3 in range(2):
                for p2 in range(3):
                    if p9+p8+p7+p3+p2 <= 20000:     # antes había un continue
                        step = m2 * pwrs3[p3] * pwrs2[p2]
                        count = 1
                        print(f'Check P{PERST}@{p9}_{p8}_{p7}_{p3}_{p2}___',
                            end='\r', flush=True)
                        go_on = True    # breaks en while sustituidos
                        while count < PERST and go_on:
                            numstr = [int(dig) for dig in str(step)]
                            if step < 10:   # cambiado desde len(numstr) == 1 (pero no es más rápido)
                                go_on = False
                                count -= 1  # para corregir la suma extra siguiente
                            if 0 in numstr:
                                go_on = False
                            step = prod(numstr)
                            count += 1  # antes esto no nos daba problemas habiendo breaks
                        if count == PERST:
                            tryDocPrint()


# IVLIVS mppr.
