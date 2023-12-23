import sqlite3
from flask import *
import json
from flask_session import *
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/")
def home1():
    session['level']=1
    return render_template("home1.html")

@app.route("/login", methods=["GET", "POST"])
def login():
 
    username = request.values["username"]
    password = request.values["password"]
    

    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    query = f"SELECT id, username FROM users WHERE username = '{username}' AND password = '{password}'"

    cursor.execute(query)

    user = cursor.fetchone()

    conn.close()
    if user:
        session['level']=2
        return redirect('level2')
        
    else:
        return render_template('get_flag.html')
    
@app.route("/level2")
def level2():
    if session['level']==1:
        return redirect('/')
    return render_template("home2.html")

@app.route("/login2", methods=["GET", "POST"])
def login2():
    
    username = request.values["username"].lower()
    password = request.values["password"].lower()
    

    filter=['or', 'and', 'true' ,'false', 'like' ,'=', '>', '<', ';' ,'--', '/*' ,'*/' ,'admin']
    for i in filter:
        if i in username or i in password:
            return render_template('filter.html') 
    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()

    query = f"SELECT id, username FROM users WHERE username = '{username}' AND password = '{password}'"
 
    cursor.execute(query)

    user = cursor.fetchone()

    conn.close()
    if user:
        session['level']=3
        return redirect('level3')
        
    else:
        return render_template('lose.html')

@app.route("/level3")
def level3():
    if session['level']==1:
        return redirect('/')
    if session['level']==2:
        return redirect('level2')
    return render_template("home3.html")

@app.route("/login3", methods=["GET", "POST"])
def login3():
        
  
    data = request.get_json()

    conn = sqlite3.connect('user_database.db')
    cursor = conn.cursor()
    
    
    query = f"SELECT id, username FROM users WHERE username = 'admin' AND password = '{data['password'][0]}'"
 
    cursor.execute(query)

    user = cursor.fetchone()

    conn.close()
    
    if user:
        return render_template('get_flag.html')
    else:
        return render_template('lose.html')
        

    



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="50003")