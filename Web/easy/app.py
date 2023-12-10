from flask import *

app=Flask(__name__)

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


if __name__ == "__main__":
    app.run(host="0.0.0.0",port="8080",debug=True)