import string
from pwn import *
import binascii
r = remote('127.0.0.1', 30000)

def oracle(m):
    r.sendlineafter('You can input some words > ', m.hex())
    r.recvlines(2)
    return bytes.fromhex(r.recvline().strip().partition(b' = ')[2].decode())

flag = b''
for i in range(19):
    prefix = b'A' * (32 - 1 - i)
    target = oracle(prefix)[:32]
    for c in string.printable:
        test = oracle(prefix + flag + bytes([ord(c)]))[:32]
        if test == target:
            flag += bytes([ord(c)])
            print(flag)
            break

r.interactive()