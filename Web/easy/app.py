from flask import *
from flask_session import *
import os
app=Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/announcement")
def announcement():
    return render_template("announcement.html")

@app.route("/teacher")
def teacher():
    return render_template("teacher.html")

@app.route("/staryu")
def staryu():
    return render_template("staryu.html")

#登入頁面
@app.route("/adminlogin")
def adminlogin():
    if "role" in session:
        if session["role"]=="admin":
            return redirect('adminPage')
    
    return render_template("adminlogin.html")

@app.route("/userlogin")
def userlogin():
    
    if "role" in session:
        if session["role"]=="user":
            return redirect("userPage")
    return render_template("userlogin.html")

#登入後頁面
@app.route("/adminPage")
def adminPage():
    if "role" not in session:
        return redirect('/')
    
    if session["role"]!="admin":
        return redirect('/')
    return render_template("adminPage.html")

@app.route("/userPage")
def userPage():
    if "role" not in session:
        return redirect('/')
    if session["role"]!="user":
        return redirect('/')    
    return render_template("userPage.html")

#登入處理
@app.route("/login",methods=["GET", "POST"])
def login():
    username = request.values["username"]
    password = request.values["password"]
    if username=="kaori@RIDDLE.JOKER" and password=="#1011":
        session["role"]="admin"
        return redirect('adminPage')
    
    else:
        return "LOSE"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="8080",debug=True)