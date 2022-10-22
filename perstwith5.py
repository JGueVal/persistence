from math import prod

MAXR = 10
r = range(MAXR)

pw9 = [9**p9 for p9 in r]
pw8 = [8**p8 for p8 in r]
pw7 = [7**p7 for p7 in r]
pw5 = [5**p5 for p5 in r]
pw3 = [1, 3]
pw2 = [1, 2, 4]

def docprint(z, y, x, w, v, u):
    try:
        with open('perstwith5.txt', 'a') as t:
            t.write(f'{z} 9s, {y} 8s, {x} 7s, {w} 5s, {v} 3s, {u} 2s\n')
    except:
        with open('errlog.txt', 'a') as e:
            e.write(f'ERROR at: {z} {y} {x} {w}\n')

def jove(p):
    for p9 in r:
        for p8 in r:
            p98 = pw9[p9] * pw8[p8]
            for p7 in r:
                p987 = p98 * pw7[p7]
                for p5 in range(1,MAXR):
                    for p3 in range(2):
                        for p2 in range(3):
                            print(f'{p9}, {p8}, {p7}, {p5}, {p3}, {p2}',
                                end='\r', flush=True)
                            dr = p987 * pw5[p5] * pw3[p3] * pw2[p2]
                            cn = 1
                            while cn < p:
                                st = [int(d) for d in str(dr)]
                                if len(st) == 1:
                                    break
                                dr = prod(st)
                                cn += 1
                            if cn == p:
                                print(f'{p}: {p9}, {p8}, {p7}, {p5}, {p3}, {p2}')
                                #docprint(p9, p8, p7, p5, p3, p2)
                                return

def loop(maxp):
    for perst in range(1,maxp):
        jove(perst)

# ==============================

loop(7)
