from Crypto.Util.number import *
import gmpy2
import codecs
msg = "ckcscCTF{fake_FLAG}"
hex_msg = int(codecs.encode(msg.encode(), 'hex'), 16)

p=getPrime(100)
q=getPrime(100)
n=p*q
e=65537

phi=(p-1)*(q-1)
d=gmpy2.invert(e,phi)

print("d=",d)
c=pow(hex_msg,e,n)

print("e=",e)
print("c=",c)

print("----------")
print("p+q=",p+q)
print("(p+1)*(q+1)=",(p+1)*(q+1))
