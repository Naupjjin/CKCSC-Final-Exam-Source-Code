import sqlite3
from flask import *
import json
app = Flask(__name__)

@app.route("/")
def home1():
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
        return redirect('oeajifpojaqeiowrjiwoejwiojrieowjri')
        
    else:
        return render_template('get_flag.html')
    
@app.route("/oeajifpojaqeiowrjiwoejwiojrieowjri")
def oeajifpojaqeiowrjiwoejwiojrieowjri():
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
        return redirect('foshdfiaopreiaowjfpoaweituripowa')
        
    else:
        return render_template('lose.html')

@app.route("/foshdfiaopreiaowjfpoaweituripowa")
def foshdfiaopreiaowjfpoaweituripowa():
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
    app.run(debug=True)