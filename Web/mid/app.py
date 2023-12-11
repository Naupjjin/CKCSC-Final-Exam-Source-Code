from flask import *


app = Flask(__name__)

@app.route("/")
def home():
    resp = make_response(render_template("index.html"))
    resp.set_cookie(key='VIP', value='68934a3e9455fa72420237eb05902327')
    return resp

@app.route("/search")
def search():
    cookie_value = request.cookies.get('VIP')
    if cookie_value!="b326b5062b2f0e69046810717534cb09":
        return redirect(url_for('home'))
    return render_template("search.html")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="10003")