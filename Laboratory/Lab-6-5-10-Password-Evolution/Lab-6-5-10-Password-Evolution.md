# Исследование эволюции парольных систем
## Цель лабораторной работы:
- Часть 1: Запуск виртуальной машины DEVASC
- Часть 2: Python: пароли в обычном тексте
- Часть 3: Python: парольный хэша

## Необходимые ресурсы:
- 1 ПК
- Virtual Box или VMWare
- DEVASC виртуальная машина

## Порядок выполнения работы
## Часть 1: Запуск виртуальной машины DEVASC
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.

## Часть 2: Демонстрация приложения
> Ваш преподаватель может продемонстрировать приложение "Простой текст пароля и хэширование". Однако мы постепенно, шаг за шагом, создадим его, что называется from scratch.
Сначала приложение сохраняет имя пользователя и пароль в виде обычного текста в базе данных веб-службы. Затем оно проверяет, что учетные данные были сохранены и работают правильно. Второй метод, хэширование пароля, также сохраняет их и проверяет в базе данных веб-службы.

## Часть 3: Установка пакетов и создание веб-службы
### Шаг 1: Откройте каталог безопасности в VS Code и установите пакеты Python.
Откройте VS Code. Затем нажмите File > Open Folder... и перейдите в каталог devnet-src/security. Нажмите OK.
На панели EXPLORER откройте password-evolution.py, чтобы открыть его.
Откройте терминал в VS Code. Щелкните Terminal > New Terminal.

Используйте следующие команды для установки пакетов, необходимых в этой лабораторной работе. Эти пакеты могут быть уже установлены на вашей виртуальной машине. В этом случае вы получите сообщение Requirement already satisfied.
```shell
devasc@labvm:~/labs/devnet-src/security$ pip3 install pyotp
Requirement already satisfied: pyotp in /home/devasc/.local/lib/python3.8/site-packages (2.3.0)
devasc@labvm:~/labs/devnet-src/security$ pip3 install flask
Requirement already satisfied: flask in /home/devasc/.local/lib/python3.8/site-packages (1.1.2)
Requirement already satisfied: itsdangerous>=0.24 in /home/devasc/.local/lib/python3.8/site-packages (from flask) (1.1.0)
Requirement already satisfied: click>=5.1 in /home/devasc/.local/lib/python3.8/site-packages (from flask) (7.1.2)
Requirement already satisfied: Werkzeug>=0.15 in /home/devasc/.local/lib/python3.8/site-packages (from flask) (1.0.1)
Requirement already satisfied: Jinja2>=2.10.1 in /home/devasc/.local/lib/python3.8/site-packages (from flask) (2.11.2)
Requirement already satisfied: MarkupSafe>=0.23 in /home/devasc/.local/lib/python3.8/site-packages (from Jinja2>=2.10.1->flask) (1.1.1)
devasc@labvm:~/labs/devnet-src/security$
```

### Шаг 2: Импорт библиотек.
В файл `password-evolution.py` добавьте следующий код. Обратите внимание на команду, db_name = 'test.db'. Это база данных SQL (sqlite3), в которой хранятся имена пользователей и пароли, которые вы будете создавать.
```python
import pyotp    # генерирует одноразовые пароли
import sqlite3  # база данных для имени пользователя/паролей
import hashlib  # безопасные хэши и дайджесты сообщений
import uuid     # cоздание уникальных идентификаторов
from flask import Flask, request
app = Flask(__name__) # Обязательно используйте два знака подчеркивания до и после "name"

db_name = "test.db" 
```

### Шаг 3: Создайте веб-сервис.
Далее добавьте в файл следующий код Flask для отображения фразы веб-контента по корневому пути. Когда пользователь перейдет по URL (корневой каталог), в браузере будет отображен вывод оператора возврата.
```python
@app.route("/")
def index():
    return "Эволюция парольных систем!"
```
Добавьте в файл следующий код для создания веб-сервиса на порту 5000 с самоподписанным сертификатом TLS. Параметр ssl_context="adhoc" позволяет запускать приложение через HTTPS без необходимости использования сертификатов или при использовании самоподписанного сертификата. Обязательно используйте два знака подчеркивания до и после name и main.
```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")
```
Сохраните и запустите файл password-evolution.py. Команда nohup (no hangup) поддерживает процесс даже после выхода из оболочки или терминала. & заставляет команду работать в фоновом режиме.
```shell
devasc@labvm:~/labs/devnet-src/security$ nohup python3 password-evolution.py &
[1] 3417
devasc@labvm:~/labs/devnet-src/security$ nohup: ignoring input and appending output to 'nohup.out'

devasc@labvm:~/labs/devnet-src/security$
```
Нажмите Enter, чтобы получить новую командную строку.
Теперь ваш сервер Flask запущен. В VS Code в дириктории /security вы должны увидеть текстовый файл nohup.out, созданный Flask. Щелкните файл, чтобы прочитать его вывод.

Убедитесь, что веб-сервис запущен. Обязательно используйте HTTPS, а не HTTP. Параметр -k позволяет curl выполнять "небезопасные" SSL-соединения и передачи. Без опции -k вы получите сообщение об ошибке "SSL certificate problem: self-signed certificate". Команда выведет сообщение из команды return, которую вы закодировали в своем сценарии.
```shell
devasc@labvm:~/labs/devnet-src/security$ curl -k https://0.0.0.0:5000/

Эволюция парольных систем!devasc@labvm:~/labs/devnet-src/security$
```
Нажмите Enter, чтобы получить командную строку с новой строки.
Прежде чем продолжить, завершите работу программы. Используйте следующую команду для её остановки:
```shell
devasc@labvm:~/labs/devnet-src/security$ pkill -f password-evolution.py
devasc@labvm:~/labs/devnet-src/security$
```

## Часть 4: Исследование Python программы, хранящей пароли в обычном тексте
> При первом использовании паролей, они просто хранились в базе данных в виде обычного текста. Когда пользователь вводил свои учетные данные, система просматривала пароль на предмет его совпадения. Система была очень проста в реализации, но в то же время очень небезопасна. В этой части мы изменим password-evolution.py, чтобы позволить ему хранить идентификационные данные пользователя в базе данных test.db. Затем мы создадите пользователя и выполните аутентификацию по этим учетным данным. Наконец, мы познакомимся с базой данных test.db, чтобы убедиться, что они хранились в открытом виде.

### Шаг 1: Удалите конфигурацию сервера.
Удалите следующие строки из файла password-evolution.py.
```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")
```

### Шаг 2: Настройте сервер для хранения учетных данных.
Добавьте следующий код Flask, чтобы настроить сервер на хранение имени пользователя и пароля пользователя в открытом виде. Используя метод HTTP POST, этот код позволяет пользователю создать ("signup") новое имя пользователя и пароль, которые будут храниться в файле базы данных test.db. Позже, когда пользователь введет имя пользователя и пароль, этот код вернет сообщение "signup success".
```python
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
                  "VALUES ('{0}', '{1}')".format(request.form['username'], request.form['password']))
        conn.commit()
    except sqlite3.IntegrityError:
        return "username has been registered."
    print('username: ', request.form['username'], ' password: ', request.form['password'])
    return "signup success"
```

> Примечание:Убедитесь в правильности отступов, иначе код может работать некорректно.

Добавьте следующий код Flask в файл password-evolution.py для проверки новых учетных данных.
```python
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
```
Добавьте следующий код Flask в файл password-evolution.py. Этот код используется при каждой попытке входа в систему для чтения параметров из HTTP-запроса и проверки учетной записи. В случае успешного входа будет возвращено сообщение "login success", в противном случае пользователь увидит сообщение "Invalid username/password".
```python
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
```

### Шаг 3: Запустите сервер и протестируйте его.
Добавьте обратно код конфигурации сервера, который вы удалили ранее.
```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")
```
Сохраните программу как `password-evolution-plain-text.py` и запустите для запуска обновленной веб-службы.
```shell
devasc@labvm:~/labs/devnet-src/security$ nohup python3 password-evolution-plain-text.py &
[1] 3765
devasc@labvm:~/labs/devnet-src/security$ nohup: ignoring input and appending output to 'nohup.out'
```
Используйте следующие команды curl для создания (регистрации) двух учетных записей пользователей, alice и bob, и отправки POST в веб-сервис. Каждая команда включает имя пользователя, пароль и вызываемую функцию регистрации, которая хранит эту информацию, включая пароль, в виде открытого текста. Вы должны увидеть сообщение "signup success" из команды return, которую вы включили в предыдущий шаг.

> Примечание: После каждой команды нажмите Enter.
```shell
devasc@labvm:~/labs/devnet-src/security$ curl -k -X POST -F 'username=alice' -F 'password=myalicepassword'  'https://0.0.0.0:5000/signup/v1'
signup successdevasc@labvm:~/labs/devnet-src/security$

devasc@labvm:~/labs/devnet-src/security$ curl -k -X POST -F 'username=bob' -F 'password=passwordforbob'  'https://0.0.0.0:5000/signup/v1'
signup successdevasc@labvm:~/labs/devnet-src/security$
devasc@labvm:~/labs/devnet-src/security$
```

### Шаг 4: Убедитесь, что новые пользователи могут войти в систему.
Используйте следующие команды curl, чтобы проверить, что оба пользователя могут войти в систему со своими паролями, которые хранятся в открытом виде.
```shell
devasc@labvm:~/labs/devnet-src/security$ curl -k -X POST -F 'username=alice' -F 'password=myalicepassword' 'https://0.0.0.0:5000/login/v1'
login successdevasc@labvm:~/labs/devnet-src/security$
devasc@labvm:~/labs/devnet-src/security$

devasc@labvm:~/labs/devnet-src/security$ curl -k -X POST -F 'username=bob' -F 'password=passwordforbob' 'https://0.0.0.0:5000/login/v1'
login successdevasc@labvm:~/labs/devnet-src/security$
```

Завершите работу сервера.
```shell
login successdevasc@labvm:~/labs/devnet-src/security$ pkill -f password-evolution-plain-text.py
[1]+  Terminated              nohup python3 password-evolution.py
devasc@labvm:~/labs/devnet-src/security$
```

### Шаг 5: Проверьте содержимое файла test.db.
Возможно, вы заметили, что SQLite создал файл test.db в дириктории /security. Вы можете открыть этот файл и посмотреть имя пользователя и пароли для alice и bob. Однако в этом шаге вы будете использовать приложение для просмотра файлов базы данных SQLite.
Откройте приложение DB Browser for SQLite
После запуска DB Browser for SQLite откройте файл test.db:
- Выберите: File > Open database…
- Перейдите в каталог labs/devnet-src/security и выберите test.db. 
- Нажмите кнопку Open.
На вкладке Database Structure обратите внимание на таблицу USER_PLAIN, которая совпадает с кодом, созданным ранее.
Разверните таблицу, чтобы увидеть два поля: USERNAME и PASSWORD.
Выберите вкладку Browse Data.
Таблица: USER_PLAIN уже выбрана. Здесь вы можете увидеть имена пользователей bob и alice вместе с их паролями в открытом виде.

Закройте приложение DB Browser for SQLite

## Часть 5: Хеширование паролей в Python
> Вместо того чтобы хранить пароли в открытом виде, вы можете хэшировать их в момент создания. Когда пароль хэшируется, он преобразуется в нечитаемый набор символов. Это позволяет невозможность обратного преобразования. Даже если база данных будет украдена, ее нельзя будет использовать, поскольку хэш неизвестен. Сейчас мы изменим файл password-evolution-plain-text.py, чтобы создать веб-API, который может принимать веб-запросы и сохранять пароль нового пользователя в хэшированном формате.

### Шаг 1: Удалите конфигурацию сервера.
Ещё раз удалите следующие две строки из файла password-evolution-plain-text.py. Эти строки будут добавлены позже.
```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")
```

### Шаг 2: Настройте сервер для хранения учетных данных.
Добавьте следующий код, чтобы сервер мог хэшировать пароль, используя алгоритм SHA256. Этот код позволяет пользователю создать ("signup") новое имя пользователя и пароль, которые будут храниться в файле базы данных test.db SQL. Разница в том, что пароли будут храниться в виде хэш-значений, а не в открытом виде. Эта процедура использует sha256, но не солит хэш. Последствия использования хэша без соли вы увидите при просмотре файла базы данных test.db.
```python
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
```
Добавьте (скопируйте) следующий код в файл `password-evolution-plain-text.py` для проверки того, что пароль был сохранен только в хэш-формате. Код определяет функцию verify_hash, которая сравнивает имя пользователя и пароль в хэш-формате. Если сравнение истинно, то пароль был сохранен только в хэш-формате.
```python
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
```
Добавьте следующий код в файл `password-evolution-plain-text.py`. Следующий код считывает параметры из HTTP POST запроса и проверяет, что пользователь указал правильный пароль при входе в систему.
```python
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
```

### Шаг 3: Запустите сервер и протестируйте его.
Добавьте обратно код конфигурации сервера, который вы удалили ранее.
```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context="adhoc")
```
Сохраните файл как `password-evolution-hashing.py`, а затем запустите сценарий для запуска обновленной веб-службы.
```shell
devasc@labvm:~/labs/devnet-src/security$ nohup python3 password-evolution-hashing.py &
[1] 4282
devasc@labvm:~/labs/devnet-src/security$ nohup: ignoring input and appending output to 'nohup.out'
```
Используйте следующие команды curl для создания трех новых учетных записей пользователей с хэшированным паролем. Обратите внимание, что два пользователя, rick и allan, используют один и тот же пароль.
```shell
devasc@labvm:~/labs/devnet-src/security$ curl -k -X POST -F 'username=rick' -F 'password=samepassword' 'https://0.0.0.0:5000/signup/v2'
signup successdevasc@labvm:~/labs/devnet-src/security$

devasc@labvm:~/labs/devnet-src/security$ curl -k -X POST -F 'username=allan' -F 'password=samepassword' 'https://0.0.0.0:5000/signup/v2'
signup successdevasc@labvm:~/labs/devnet-src/security$

devasc@labvm:~/labs/devnet-src/security$ curl -k -X POST -F 'username=dave' -F 'password=differentpassword' 'https://0.0.0.0:5000/signup/v2'
signup successdevasc@labvm:~/labs/devnet-src/security$
```
Используйте команды curl для проверки входа всех трех пользователей с их паролями, сохраненными в хэш-памяти. Пользователь allan введен дважды, первый раз с неправильным паролем. Обратите внимание на сообщение "Invalid username/password", которое совпадает с кодом для этой функции, который вы добавили в предыдущем шаге.
```shell
devasc@labvm:~/labs/devnet-src/security$ curl -k -X POST -F 'username=rick' -F 'password=samepassword' 'https://0.0.0.0:5000/login/v2'
login successdevasc@labvm:~/labs/devnet-src/security$

devasc@labvm:~/labs/devnet-src/security$ curl -k -X POST -F 'username=allan' -F 'password=wrongpassword' 'https://0.0.0.0:5000/login/v2'
Invalid username/passworddevasc@labvm:~/labs/devnet-src/security$

devasc@labvm:~/labs/devnet-src/security$ curl -k -X POST -F 'username=allan' -F 'password=samepassword' 'https://0.0.0.0:5000/login/v2'
login successdevasc@labvm:~/labs/devnet-src/security$

devasc@labvm:~/labs/devnet-src/security$ curl -k -X POST -F 'username=dave' -F 'password=differentpassword' 'https://0.0.0.0:5000/login/v2'
login successdevasc@labvm:~/labs/devnet-src/security$
```
Это подтверждает, что хэшированный пароль надежно хранится, а пароли пользователей защищены в случае их компрометации.
Завершить работу сервера
```shell
devasc@labvm:~/labs/devnet-src/security$ pkill -f password-evolution-hashing.py
[1]+  Terminated              nohup python3 password-evolution.py
devasc@labvm:~/labs/devnet-src/security$
```

### Шаг 4: Проверьте содержимое файла test.db.
Откройте приложение DB Browser for SQLite.
Откройте файл test.db.
Выберите вкладку Database Structure. 
Вы заметите две структуры, которые совпадают с кодом, который вы включили ранее: USER_PLAIN и USER HASH.

Выберите вкладку Browse Data. 
Таблица: USER_HASH уже должна быть выбрана. Теперь вы увидите имена пользователей rick, allan и dave вместе с их хэшированными паролями.

Обратите внимание, что у rick и allan одинаковые хэшированные пароли. Это потому, что у них был один и тот же пароль, а хэш-функция не включала соль, чтобы сделать их хэш уникальным. “Соление хэша” — это процесс добавления случайных данных к хэшу. Чтобы гарантировать уникальность паролей, повысить их сложность и предотвратить атаки на пароли даже при одинаковых входных данных, на вход хэш-функции необходимо добавить соль.

## Часть 6: Обзор окончательной программы
Ниже приведен полный сценарий, который вы создали в этой лабораторной работе.
```python
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
```