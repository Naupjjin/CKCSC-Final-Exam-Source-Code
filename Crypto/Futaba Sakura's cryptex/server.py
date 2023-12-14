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


def dec_a(plain_text):
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

def dec_b(key2_m):
    j=key2_m.encode()
    for i in range(12):
        j=base64.b64encode(j)
    return j.decode()

def dec_c(m,k):
    chip = []
    for i in range(0,len(m),k):
        chip.append(m[i:i+k])
    c = ""
    for j in range(k):
        for ch in chip:
            if j < len(ch):
                c += ch[j]
    return c


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

    key3_ans=input("key3?")
    if key3_m==key3_ans:
        print("success!!")
    else:
        exit()
    
    print("沒想到你這麼強，準備來好破解我的秘密啦!")
    aes = AES.new(KEY, AES.MODE_ECB)
    
    while True:
        message = bytes.fromhex(input('You can input some words > ').strip())
        cipher = aes.encrypt(pad(message + FLAG))
        print("encrypt...")
        print("-"*30)
        print(f'cipher = {cipher.hex()}')
        print("-"*30)


        


try:
    print("-"*30)
    print("你好呀!我是由人稱天才少女的佐倉雙葉主人所製作密碼盒，可以叫我-小綾~")
    print("如果你能夠破解我的話，我就會告訴你我的秘密喔~")
    print("不過在正式開始前，先給你一個小測試，要是你能找到三把key，就可以獲得挑戰的權利!")
    print("-"*30)

    key1_m = generate_random_string(20)+"-key1"
    print("encrypt key1:",dec_a(key1_m))
    
    print()
    key2_m = generate_random_string(20)+"-key2"
    print("encrypt key2:",dec_b(key2_m))

    print()
    key3_m = generate_random_string(20)+"-key3"
    print("encrypt key3:",dec_c(key3_m,11))

    print("-"*30)
    stage()
    
except:
    print()
    print("我已經停止運作囉!不知道~你有沒有成功找出我的秘密")
    exit()