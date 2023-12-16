from flask import *
import jwt
import os

app = Flask(__name__)

class JWT_class:
    def __init__(self):
        
        self.secret_key =os.urandom(3)

    def JWT_user(self):
        data = {'id': 2, 'role': "User"}

        token = jwt.encode(data, self.secret_key, algorithm='HS256')
        return token

    def JWT_admin(self):
        data = {'id': 1, 'role': "Admin"}

        token = jwt.encode(data, self.secret_key, algorithm='HS256')

        return token
    
JWT_ob=JWT_class()


@app.route("/")
def home():


    return send_from_directory(app.static_folder,"aaa.jpg")

@app.route("/asdfsdfasfwae")
def flag():

    return render_template("s.html")

@app.route("/afaiueyruioqhoeQEROIYEROQskf")
def bttnpage():
    
    resp = make_response(render_template("bttn.html"))
  
    resp.set_cookie(key='ToKEn', value=JWT_ob.JWT_user())
    
    return resp

@app.route("/button")
def button():
    AD_TOKEN=JWT_ob.JWT_admin()

    cookie_value = request.cookies.get('ToKEn')
    if cookie_value==AD_TOKEN:
        return render_template("admin.html")
    else:
        return render_template("LOSE.html")
    
@app.route("/robots.txt")
def ro():
    return send_from_directory(app.static_folder,"robots.txt")

@app.route("/UUUUser")
def UUUUser():
    cookie_value = request.cookies.get('ToKEn')

    if cookie_value==JWT_ob.JWT_user():
        return render_template("user.html")
    else:
        return render_template("LOSE.html")
    

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="10003")