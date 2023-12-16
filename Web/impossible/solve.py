from tqdm import tqdm
from itertools import product
import jwt
data = {'id': 2, 'role': "User"}
def jwtjwt(secret_key):
    token = jwt.encode(data, secret_key, algorithm='HS256')
    return token

realkey=""
for new_key in tqdm(product(range(256), repeat=3)):
    new_key = bytes(new_key)
    if jwtjwt(new_key) == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Miwicm9sZSI6IlVzZXIifQ.IfoUSUGjtgd9vqQ4Z-dDg3Jd8vZr3FgLTNgSx3Rh3oQ":
        realkey=new_key
        break

print(realkey)