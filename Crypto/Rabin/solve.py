import gmpy2
import codecs

def squareMod(c, mod):         
    assert(mod % 4 == 3)
    res = gmpy2.powmod(c, (mod+1)//4, mod)
    return res, mod - res

def getPlaintext(x, y, p, q):  
    res = x*q*gmpy2.invert(q, p) + y*p*gmpy2.invert(p, q)
    return res % (p*q)

def solve(c, p, q):            
    px = squareMod(c, p)
    py = squareMod(c, q)

    for x in px:
        for y in py:
            yield getPlaintext(x, y, p, q)

c = 36385155708314824172407130300080762276636346601376110917605592084732474782930

p = 275127860351348928173285174381581152299
q = 319576316814478949870590164193048041239

for msg in solve(c, p, q):
    res = hex(msg)[2:]
    if len(res) % 2 == 1:
        res = '0' + res

    print(codecs.decode(res, 'hex'))