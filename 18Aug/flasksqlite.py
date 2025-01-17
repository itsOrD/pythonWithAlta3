#!/usr/bin/python3
from flask import Flask
from flask import render_template
from flask import request
import sqlite3 as sql
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/enternew")
def new_student():
    return render_template("student.html")

@app.route("/addrec",methods = ["POST", "GET"])
def addrec():
    if request.method == "POST":
        try:
            nm = request.form["nm"]
            addr = request.form["add"]
            city = request.form["city"]
            pin = request.form["pin"]

            with sql.connect("database.db") as con:
                cur = con.cursor() 
                con.execute('''CREATE TABLE IF NOT EXISTS STUDENTS
                (NAME       TEXT    NOT NULL,
                ADDR        TEXT    NOT NULL,
                CITY        TEXT    NOT NULL,
                PIN INT PRIMARY KEY NOT NULL);''')
                cur = con.cursor()

                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",
                (nm,addr,city,pin))
                con.commit()
                msg = "Record successfully added"
             
        except:
            con.rollback()
            msg = "error in insert operation"
       
        finally:
            return render_template("result.html",msg = msg)
            con.close()
 
@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    
    cur = con.cursor()
    cur.execute("select * from students")
    
    rows = cur.fetchall();
    return render_template("list.html",rows = rows)
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

