from math import prod

MAXR = int(input("Enter max range.\n \
    \r400 has been tried with persistence 6 without success: "))
r = range(MAXR)

pw9 = [9**p9 for p9 in r]
pw7 = [7**p7 for p7 in r]
pw5 = [5**p5 for p5 in r] # inutil multiplicar pares con 5
pw3 = [1, 3]

def docprint(z, x, w, v):
    try:
        with open('perstwith5.txt', 'a') as t:
            t.write(f'{z} 9s, {x} 7s, {w} 5s, {v} 3s\n')
    except:
        try:
            with open('perstwith5.txt', 'a') as t:
                t.write(f'{z} 9s, {x} 7s, {w} 5s, {v} 3s\n')
        except:
            print(f'ERROR at: {z} {x} {w} {v}')

def fnProc(p):
    for p5 in range(1,MAXR):
        for p9 in r:
            p59 = pw5[p5] * pw9[p9]
            for p7 in r:
                for p3 in range(2):
                    print(f'{p9},_{p7},_{p5},_{p3}_____', end='\r', flush=True)
                    dr = p59 * pw7[p7] * pw3[p3]
                    cn = 1
                    while cn < p:
                        st = [int(d) for d in str(dr)]
                        if len(st) == 1:
                            break
                        elif 0 in st:
                            if cn in [p-5, p-4, p-3, p-2, p-1]:
                                print(f'{cn+1}: {p9}, {p7}, {p5}, {p3}')
                                docprint(p9, p7, p5, p3)
#                                return
                            break
                        dr = prod(st)
                        cn += 1
                    if cn in [p-4, p-3, p-2, p-1, p]:
                        print(f'{cn}: {p9}, {p7}, {p5}, {p3}')
                        docprint(p9, p7, p5, p3)
#                        return


# ==============================
b = int(input("Enter persistence (5 is highest sure hit): "))
print(f'Checking persistences from {b} to {b+4}...')
print("P: n, s, c, t")
fnProc(b+4)

# IVLIVS mppr.
