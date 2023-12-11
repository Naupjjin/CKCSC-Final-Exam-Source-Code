import os
from Crypto.Cipher import AES
from flag import FLAG
import random
import string
import base64

def generate_random_string(length):

    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=length))
    return random_string


def affine_encrypt(plain_text):
    a=77
    b=15
    encrypted_text=""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                encrypted_char=chr(((a*(ord(char)-ord('A'))+b)%26)+ord('A'))
            else:
                encrypted_char=chr(((a*(ord(char)-ord('a'))+b)%26)+ord('a'))
            encrypted_text+=encrypted_char
        else:
            encrypted_text+=char
    return encrypted_text

def base(key2_m):
    j=key2_m.encode()
    for i in range(12):
        j=base64.b64encode(j)
    return j.decode()

def pad(m):
    padlen = -len(m) % 16
    return m + bytes([0] * padlen)

KEY = os.urandom(16)

def stage():
    key1_ans=input("key1?")

    if key1_m==key1_ans:
        print("success!!")
    else:
        exit()
    
    key2_ans=input("key2?")

    if key2_m==key2_ans:
        print("success!!")
    else:
        exit()
    

    aes = AES.new(KEY, AES.MODE_ECB)
    
    while True:
        message = bytes.fromhex(input('message = ').strip())
        cipher = aes.encrypt(pad(message + FLAG))
        print(f'cipher = {cipher.hex()}')


try:
    print("-"*30)
    print("")
    print("-"*30)
    key1_m = generate_random_string(20)+"-key1"
    print("encrypt key1:",affine_encrypt(key1_m))

    key2_m = generate_random_string(20)+"-key2"
    print("encrypt key2:",base(key2_m))

    stage()
    
except:
    exit()