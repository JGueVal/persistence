import math
import itertools

digits = [9,8,7,6,4,3,2]

numlng = int(input("Number length: "))
per11 = [2,7**6,8**6,9**2]
x = math.prod(per11)
### ===========================================================
for candidate in itertools.combinations_with_replacement(digits, numlng):
    if candidate[0] == 9:
##        continue
##    elif candidate[0] == 8:
#        continue
#    elif candidate[0] == 7:
        result = math.prod(candidate)
        numstring = [int(dig) for dig in str(result)]
        if math.prod(numstring) == x:
            per12 = ''.join([str(n) for n in candidate])[::-1]
            print("FOUND IT!")
            t = open("perst.txt", "a")
            t.write(per12)
            t.close()
            print("Succesfully printed")
            break
    else:
        break
### ===========================================================
"""
La raíz numérica multiplicativa es el producto de todas las cifras de un número.
La persistencia es el número de veces que se puede hacer la raíz numérica multiplicativa consecutivamente hasta terminar con una cifra. Por ejemplo, 77:
7*7=49
4*9=36
3*6=18
1*8=8

Los números menores con su persistencia son:

 1	10 (0)
 2	25 (10,0)
 3	39 (27,14,4)
 4	77 (49,36,18,8)
 5	679 (378,168,48,32,6)
 6	6788 (2688,768,336,54,20,0)
 7	68889 (27648,2688,768,336,54,20,0)
 8	2677889 (338688,27648,2688,768,336,54,20,0)
 9	26888999 (4478976,338688,27648,2688,768,336,54,20,0)
10	3778888999 (438939648,4478976,338688,27648,2688,768,336,54,20,0)
11	277777788888899 (4996238671872,438939648,4478976,338688,27648,2688,768,336,54,20,0)

Se cree que no existe un número que tenga persistencia 12
NOTA: no hay número menor de 50 cifras con persistencia mayor de 11

El programa debe soportar números muy grandes (más de 20.000 cifras)
"""