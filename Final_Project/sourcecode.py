from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
import sqlite3 as sql
app = Flask(__name__)
Bootstrap(app)

@app.route("/home")
def home():
   return render_template("home.htm")

@app.route("/result")
def result():
   return render_template("result.htm")

@app.route("/add")
def add():
    return render_template("add.htm")


@app.route("/addrec/", methods = ["POST", "GET"])
def addrec():
    if request.method == "POST":
        # try:
        item_id = request.form["item_id"]
        nm = request.form["nm"]
        item_type = request.form["item_type"]
        price = request.form["price"]
        amt = request.form["amt"]

        with sql.connect("edge_db.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO drinks (item_id, name, type, price, amount) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(item_id, nm, item_type, price, amt))
            con.commit()
        # except:
        #     con.rollback()
        #     msg = "Error"
        # finally:
        return render_template("result.htm")
        con.Close()

@app.route("/inventory")
def list():
    con = sql.connect("edge_db.db")
    con.row_factory = sql.Row 

    cur = con.cursor()
    cur.execute("SELECT * FROM drinks")

    rows = cur.fetchall()
    return render_template("inventory.htm", rows = rows)

if __name__ == "__main__":
    app.run(debug=True)