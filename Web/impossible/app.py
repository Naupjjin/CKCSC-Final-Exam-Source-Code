from flask import *
import jwt
import os

app = Flask(__name__)
secret_key =os.urandom(3)


def JWT_user():
    data = {'id': 2, 'role': "User"}

    token = jwt.encode(data, secret_key, algorithm='HS256')
    return token

def JWT_admin():
    data = {'id': 1, 'role': "Admin"}

    token = jwt.encode(data, secret_key, algorithm='HS256')
    return token

@app.route("/")
def home():
    resp = make_response(render_template("index.html"))
    print(secret_key)
    resp.set_cookie(key='ToKEn', value=JWT_user())
    return resp

@app.route("/button")
def button():
    AD_TOKEN=JWT_admin()
    cookie_value = request.cookies.get('ToKEn')
    if cookie_value==AD_TOKEN:
        return render_template("admin.html")
    else:
        return render_template("LOSE.html")
    


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="10003")