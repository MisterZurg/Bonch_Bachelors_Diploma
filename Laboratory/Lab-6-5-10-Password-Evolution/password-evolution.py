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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")

