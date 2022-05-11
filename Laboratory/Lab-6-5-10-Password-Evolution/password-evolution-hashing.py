import pyotp    # генерирует одноразовые пароли
import sqlite3  # база данных для имени пользователя/паролей
import hashlib  # безопасные хэши и дайджесты сообщений
import uuid     # cоздание уникальных идентификаторов
from flask import Flask, request
app = Flask(__name__) # Обязательно используйте два знака подчеркивания до и после "name"

db_name = "test.db"


@app.route("/")
def index():
    return "Эволюция парольных систем!"


######################################### Открытый Текст #########################################################
@app.route("/signup/v1", methods=["POST"])
def signup_v1():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_PLAIN
           (USERNAME  TEXT    PRIMARY KEY NOT NULL,
            PASSWORD  TEXT    NOT NULL);''')
    conn.commit()
    try:
        c.execute("INSERT INTO USER_PLAIN (USERNAME,PASSWORD) "
                  "VALUES ('{0}', '{1}')".format(request.form["username"], request.form["password"]))
        conn.commit()
    except sqlite3.IntegrityError:
        return "username has been registered."
    print("username: ", request.form["username"], " password: ", request.form["password"])
    return "signup success"


def verify_plain(username, password):
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    query = "SELECT PASSWORD FROM USER_PLAIN WHERE USERNAME = '{0}'".format(username)
    c.execute(query)
    records = c.fetchone()
    conn.close()
    if not records:
        return False
    return records[0] == password


@app.route("/login/v1", methods=["GET", "POST"])
def login_v1():
    error = None
    if request.method == "POST":
        if verify_plain(request.form["username"], request.form["password"]):
            error = "login success"
        else:
            error = "Invalid username/password"
    else:
        error = "Invalid Method"
    return error



######################################### Хеширование Пароля #########################################################
@app.route("/signup/v2", methods=["GET", "POST"])
def signup_v2():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_HASH
           (USERNAME  TEXT    PRIMARY KEY NOT NULL,
            HASH      TEXT    NOT NULL);''')
    conn.commit()
    try:
        hash_value = hashlib.sha256(request.form["password"].encode()).hexdigest()
        c.execute("INSERT INTO USER_HASH (USERNAME, HASH) "
                  "VALUES ('{0}', '{1}')".format(request.form["username"], hash_value))
        conn.commit()
    except sqlite3.IntegrityError:
        return "username has been registered."
    print("username: ", request.form["username"], " password: ", request.form["password"], " hash: ", hash_value)
    return "signup success"


@app.route("/login/v2", methods=["GET", "POST"])
def login_v2():
    error = None
    if request.method == 'POST':
        if verify_hash(request.form['username'], request.form['password']):
            error = "login success"
        else:
            error = "Invalid username/password"
    else:
        error = "Invalid Method"
    return error


def verify_hash(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    query = "SELECT HASH FROM USER_HASH WHERE USERNAME = '{0}'".format(username)
    c.execute(query)
    records = c.fetchone()
    conn.close()
    if not records:
        return False
    return records[0] == hashlib.sha256(password.encode()).hexdigest()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")
