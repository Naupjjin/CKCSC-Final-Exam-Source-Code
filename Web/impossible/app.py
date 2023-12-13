from flask import *
import jwt
import os
app = Flask(__name__)

class JWT:
    def __init__(self):
        self.key=os.urandom(3)
        
    def JWT_user(self):
        
        payload={"id":1 ,"role":"user"}
        encoded_token = jwt.encode(payload, self.key, algorithm='HS256')
        return encoded_token

    def JWT_admin(self):
        
        payload={"id":2 ,"role":"admin"}
        encoded_token = jwt.encode(payload, self.key, algorithm='HS256')
        return encoded_token

@app.route("/")
def home():
    return render_template("index.html")

