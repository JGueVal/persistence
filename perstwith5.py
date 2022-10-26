from math import prod

MAXR = int(input("Enter max range.\n \
    \r400 has been tried with persistence 6 without success: "))
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
        try:
            with open('perstwith5.txt', 'a') as t:
                t.write(f'{z} 9s, {y} 8s, {x} 7s, {w} 5s, {v} 3s, {u} 2s\n')
        except:
            print(f'ERROR at: {z} {y} {x} {w} {v} {u}')

def jove(p):
    for p5 in range(1,MAXR):
        for p9 in r:
            p59 = pw5[p5] * pw9[p9]
            for p8 in r:
                p598 = p59 * pw8[p8]
                for p7 in r:
                    for p3 in range(2):
                        for p2 in range(3):
                            print(f'{p9}, {p8}, {p7}, {p5}, {p3}, {p2}', end='\r', flush=True)
                            dr = p598 * pw7[p7] * pw3[p3] * pw2[p2]
                            cn = 1
                            while cn < p:
                                st = [int(d) for d in str(dr)]
                                if len(st) == 1:
                                    break
                                elif 0 in st:
                                    if cn in [p-3, p-2, p-1]:
                                        print(f'{p-cn}: {p9}, {p8}, {p7}, {p5}, {p3}, {p2}')
                                        docprint(p9, p8, p7, p5, p3, p2)
                                        #return
                                    break
                                dr = prod(st)
                                cn += 1
                            if cn in [p-2, p-1, p]:
                                print(f'{p-cn}: {p9}, {p8}, {p7}, {p5}, {p3}, {p2}')
                                docprint(p9, p8, p7, p5, p3, p2)
                                #return


# ==============================
b = int(input("Enter persistence (5 is highest sure hit): "))
print("P: n, o, s, c, t, d")
jove(b)
