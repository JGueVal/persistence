from math import prod

###--NECESARIO A PARTIR DE PYTHON 3.10.7--
#from sys import set_int_max_str_digits
#set_int_max_str_digits(0)

PERST = 12
r = range(100000)

pwrs9 = [9**p9 for p9 in r]
pwrs8 = [8**p8 for p8 in r]
pwrs7 = [7**p7 for p7 in r]
pwrs3 = [1, 3]
pwrs2 = [1, 2, 4]

r = range(99999, -1, -1)

def docprint():
    try:
        print(f'{p9}, {p8}, {p7}, {p3}, {p2}')
        with open('perst.txt', 'a') as t:
            t.write(f'{p9} 9s, {p8} 8s, {p7} 7s, {p3} 3s, {p2} 2s\n')
    except:
        try:
            print(f'{p9}, {p8}, {p7}, {p3}, {p2}')
            with open('perstB.txt', 'a') as t:
                t.write(f'{p9} 9s, {p8} 8s, {p7} 7s, {p3} 3s, {p2} 2s\n')
        except:
            print(f'ERROR at: {p9}, {p8}, {p7}, {p3}, {p2}')

# Se puede usar itertools, pero es conveniente esto en caso de querer interrumpir el programa
# EJEMPLO: "if p9 > 99997: continue", "if p9 >= 99997 and p8 > 65535: continue"
# en números más pequeños, buscar si hay un 0 o un 5 lo ralentiza
for p9 in r:
    for p8 in r:
        p98 = pwrs9[p9] * pwrs8[p8]
        for p7 in r:
            p987 = p98 * pwrs7[p7]
            for p3 in range(2):
                for p2 in range(3):
                    if p9+p8+p7+p3+p2 < 20000:
                        continue
                    step = p987 * pwrs3[p3] * pwrs2[p2]
                    count = 1
                    print(f'{p9}, {p8}, {p7}, {p3}, {p2}',
                        end='\r', flush=True)
                    while count < PERST:
                        numstr = [int(dig) for dig in str(step)]
                        if len(numstr) == 1:
                            break
                        elif 0 in numstr:
                            if count == PERST-1:
                                docprint()
                            break
                        step = prod(numstr)
                        count += 1
                    if count == PERST:
                        docprint()
