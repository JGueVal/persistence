import math
import itertools

digits = [9,8,7,6,4,3,2]
#digits = [9,8,7,3,2]

per11 = [2,7**6,8**6,9**2]
x = math.prod(per11)
### ===========================================================

for numlng in range(50000,19999,-1): #reverse
    for c in itertools.combinations_with_replacement(digits, numlng):
        if c[0] == 9:
##            continue
##        elif candidate[0] == 8:
#            continue
#        elif candidate[0] == 7:
            print(c.count(9),"9s",c.count(8),"8s",c.count(7),"7s",c.count(6),"6s",c.count(4),"4s",c.count(3),"3s",c.count(2),"2s")
#            print(c.count(9),"9s",c.count(8),"8s",c.count(7),"7s",c.count(3),"3s",c.count(2),"2s")
            result = math.prod(c)
            numstring = [int(dig) for dig in str(result)]
            if math.prod(numstring) == x:
                per12 = ''.join([str(n) for n in candidate])[::-1]
                print("FOUND IT!")
                t = open("perst.txt", "a")
                t.write(per12+"\n"+numlng)
                t.close()
                print("Succesfully printed")
                break
        else:
            break
### ===========================================================
