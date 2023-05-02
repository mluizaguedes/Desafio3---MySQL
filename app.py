from flask import Flask, render_template, request, url_for, jsonify
from flask_mysqldb import MySQL



def create_app():
    from app import routes
    routes.init_app(app)

    return app

app= Flask(__name__)

app.config['MYSQL_Host'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'contatos'

mysql = MySQL (app)

@app.route("/")
@app.route("/index")
def home():
    return render_template("home.html")

@app.route("/quemsomos")
def quem_somos():
    return render_template("quemsomos.html")