import os
from Crypto.Cipher import AES

import random
import string
import base64

FLAG=b"ckcscCTF{1_v3ry_L0v3_my_Own3r_LOVELOVELOVE!}"



def pad(m):
    padlen = -len(m) % 16
    return m + bytes([0] * padlen)

KEY = os.urandom(16)

def stage():
    
    
    print("沒想到你這麼強，準備來好破解我的秘密啦!")
    aes = AES.new(KEY, AES.MODE_ECB)
    
    while True:
        message = bytes.fromhex(input('You can input some words > ').strip())
        cipher = aes.encrypt(pad(message + FLAG))
        print("encrypt...")
        print("-"*30)
        print(f'cipher = {cipher.hex()}')
        print("-"*30)

stage()
    
