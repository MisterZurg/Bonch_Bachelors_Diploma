# Сборка демо веб-приложения в Docker контейнере 
## Цель лабораторной работы:
- Часть 1: Запуск виртуальной машины DEVASC
- Часть 2: Создаём простой Bash скрипт
- Часть 3: Создаём демо веб-приложение
- Часть 4: Настройка веб-приложения для использования файлов веб-сайта
- Часть 5: Создаём Bash скрипт для создания и запуска Docker контейнера 
- Часть 6: Сборка, запуск и проверка Docker контейнера

## Необходимые ресурсы:
- 1 ПК
- Virtual Box или VMWare
- DEVASC виртуальная машина

##Порядок выполнения работы
## Часть 1: Запуск виртуальной машины DEVASC
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.

## Часть 2: Создаём простой Bash скрипт
> Знание Bash крайне важно для работы с Continuous Integration, Continuous Deployment, контейнерами и со средой разработки. Bash скрипт помогают программистам автоматизировать множество задач в одном файле сценария.

### Шаг 1: Создайте пустой файл bash.
Измените рабочий каталог на ~/labs/devnet-src/sample-app и добавьте новый файл user-input.sh.
```shell
devasc@labvm:~$ cd labs/devnet-src/sample-app/
devasc@labvm:~/labs/devnet-src/sample-app$ touch user-input.sh
```

### Шаг 2: Откройте файл в текстовом редакторе nano.
Используйте команду nano, чтобы открыть текстовый редактор nano.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ nano user-input.sh
```

### Шаг 3: Добавьте "she-bang" в начало сценария.
Отсюда вы можете вводить команды для вашего сценария bash. Используйте клавиши со стрелками для навигации в nano. Обратите внимание на команды внизу (здесь не показаны) для управления файлом. Символ карата (^) указывает на использование клавиши CTRL или Command на клавиатуре. Например, чтобы выйти из nano, введите CTRL+X. 
Добавьте 'she-bang', который сообщает системе, что этот файл включает команды, которые необходимо выполнить в оболочке bash.
```bash
#!/bin/bash
```

> Примечание: Вы можете использовать графический текстовый редактор или открыть файл с помощью VS Code. Однако будет здорово, иметь опыт работы с текстовыми редакторами командной строки, такими как nano и vim.

### Шаг 4: Добавьте bash скрипт простые команды.
Введите несколько простых команд bash. Следующие команды будут запрашивать у пользователя имя, устанавливать это имя в переменную userName и выводить на экран строку текста с именем пользователя.
```bash
echo -n "Введите ваше имя: "
read userName
echo "Ваше имя — $userName."
```

### Шаг 5: Выйдите из редактора nano и сохраните скрипт.
Нажмите CTRL+X, затем Y, затем ENTER, чтобы выйти из nano и сохранить скрипт.

### Шаг 6: Запустите свой скрипт из командной строки.
Вы можете запустить его непосредственно из командной строки с помощью следующей команды.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ bash user-input.sh 
Введите ваше имя: Impostor
Ваше имя — Impostor.
devasc@labvm:~/labs/devnet-src/sample-app$
```

### Шаг 7: Измените режим скрипта на исполняемый файл для всех пользователей.
Измените режим скрипта на исполняемый с помощью команды chmod. Установите параметры a+x, чтобы сделать скрипт исполняемым (x) для всех пользователей (a). После использования команды chmod обратите внимание, что разрешения были изменены для пользователей, групп и других, чтобы включить "x" (исполняемый).
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ ls -l user-input.sh
-rw-rw-r-- 1 devasc devasc 108 мая  4 09:46 user-input.sh 

devasc@labvm:~/labs/devnet-src/sample-app$ chmod a+x user-input.sh

devasc@labvm:~/labs/devnet-src/sample-app$ ls -l user-input.sh
-rwxrwxr-x 1 devasc devasc 108 мая  4 09:46 user-input.sh
```

### Шаг 8: Переименуйте файл, чтобы удалить расширение .sh.
Вы можете переименовать файл, удалив расширение, чтобы пользователям не приходилось добавлять .sh к команде для выполнения сценария.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ mv user-input.sh user-input
```

### Шаг 9: Запустите скрипт из командной строки.
Теперь сценарий можно запустить из командной строки без команды source или расширения. Чтобы запустить сценарий bash без исходной команды, вы должны предварять сценарий символом "./".
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ ./user-input
Введите ваше имя: Sus
Ваше имя —  Bob.
devasc@labvm:~/labs/devnet-src/sample-app$
```

## Часть 3: Создаём демо веб-приложение
> Прежде чем запускать приложение в Docker контейнере, нам сначала нужно это приложение. В этой части мы создадим очень простой сценарий на Python, который будет отображать IP-адрес клиента при посещении им веб-страницы.

### Шаг 1: Установите Flask и откройте порт на брандмауэре DEVASC VM.
Разработчики веб-приложений, использующие Python, обычно используют фреймворк. Фреймворк — это библиотека кода, облегчающая разработчикам создание надежных, масштабируемых и поддерживаемых веб-приложений. Flask — это фреймворк для веб-приложений, написанный на языке Python. Другие фреймворки включают Tornado и Pyramid. 
Вы будете использовать этот фреймворк для создания примера веб-приложения. Flask получает запросы, а затем предоставляет ответ пользователю в веб-приложении. Это полезно для динамических веб-приложений, поскольку позволяет взаимодействовать с пользователем и создавать динамический контент. Что делает ваше демо веб-приложение динамическим, так это то, что он будет показывать IP-адрес клиента.
Откройте окно терминала и устанавите flask.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ pip3 install flask
devasc@labvm:~/labs/devnet-src/sample-app$ pip3 install flask
Requirement already satisfied: flask in /home/devasc/.local/lib/python3.8/site-packages (1.1.2)
Requirement already satisfied: Werkzeug>=0.15 in /home/devasc/.local/lib/python3.8/site-packages (from flask) (1.0.1)
Requirement already satisfied: Jinja2>=2.10.1 in /home/devasc/.local/lib/python3.8/site-packages (from flask) (2.11.2)
Requirement already satisfied: click>=5.1 in /home/devasc/.local/lib/python3.8/site-packages (from flask) (7.1.2)
Requirement already satisfied: itsdangerous>=0.24 in /home/devasc/.local/lib/python3.8/site-packages (from flask) (1.1.0)
Requirement already satisfied: MarkupSafe>=0.23 in /home/devasc/.local/lib/python3.8/site-packages (from Jinja2>=2.10.1->flask) (1.1.1)
devasc@labvm:~/labs/devnet-src/sample-app$ 
```

### Шаг 2: Откройте файл sample_app.py.
Откройте файл sample_app.py, расположенный в каталоге /sample-app. Вы можете сделать это внутри VS Code или использовать текстовый редактор командной строки, например, nano или vim.

### Шаг 3: Импортируйте flask.
Добавьте следующие команды для импорта необходимых методов из библиотеки flask.
```python
from flask import Flask
from flask import request
```

### Шаг 4: Создайте экземпляр класса Flask.
Создайте экземпляр класса Flask и назовите его sample. Обязательно используйте два символа подчеркивания до и после "name".
```python
sample = Flask(__name__)
```

### Шаг 5: Определите метод показывающий IP-адреса клиента.
Далее настройте Flask так, чтобы при посещении пользователем страницы по умолчанию (корневой каталог) выводилось сообщение с IP-адресом клиента.
```shell
@sample.route("/")
def main():
    return "Ты заходишь на меня с " + request.remote_addr + "\n"
```
Обратите внимание на анотацию `@sample.route("/")` Flask. Такие фреймворки, как Flask, используют технику маршрутизации (.route) для ссылки на URL приложения (это не следует путать с сетевой маршрутизацией). Здесь "/" (корневой каталог) привязан к функции main(). Таким образом, когда пользователь перейдет по URL http://localhost:8080/ (корневой каталог), в браузере будет отображен результат оператора возврата.

### Шаг 6: Настройте приложение для локального запуска.
Наконец, настройте Flask на локальный запуск приложения по адресу http://0.0.0.0:8080, который также является http://localhost:8080. Обязательно используйте два знака подчеркивания до и после "name", а также до и после "main".
```python
if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)
```

### Шаг 7: Сохраните и запустите ваше демо веб-приложение.
Сохраните скрипт и запустите его из командной строки. Вы должны увидеть следующий результат, который указывает на то, что ваш сервер "sample-app" запущен. Если вы не видите следующего вывода или получаете сообщение об ошибке, внимательно проверьте ваш скрипт sample_app.py.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ python3 sample_app.py 
 * Serving Flask app "sample-app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
```

### Шаг 8: Убедитесь, что сервер запущен.
Вы можете проверить работу сервера одним из двух способов.
- Откройте веб-браузер Chromium и введите 0.0.0.0:8080 в поле URL. Вы должны получить следующий результат:
Если вы получаете ответ "HTTP 400 Bad Request", внимательно проверьте свой скрипт sample_app.py.
-	Откройте другое окно терминала и используйте инструмент URL командной строки (cURL) для проверки ответа сервера
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ curl http://0.0.0.0:8080
Ты заходишь на меня с 127.0.0.1
devasc@labvm:~/labs/devnet-src/sample-app$
```

### Шаг 9: Остановите сервер.
Вернитесь в окно терминала, в котором запущен сервер, и нажмите CTRL+C, чтобы остановить сервер.

## Часть 4: Настройка веб-приложения для использования файлов веб-сайта
> В этой части мы создадим демо веб-приложение, содержащую index.html и style.css. index.html обычно является первой страницей, загружаемой в браузере клиента при посещении вашего сайта. style.css - стили, используемые для красоты веб-страницы.

### Шаг 1: Изучите каталоги, которые будут использоваться веб-приложением.
Каталоги templates и static уже находятся в каталоге sample-app. Откройте index.html и style.css, чтобы просмотреть их содержимое. Если вы знакомы с HTML и CSS, не стесняйтесь настраивать эти каталоги и файлы как угодно. Однако убедитесь, что вы сохранили встроенный {{request.remote_addr}} Python-код в файле index.html, поскольку это динамический аспект примера веб-приложения.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ cat templates/index.html 
```
```html
<html>
<head>
    <title>Sample app</title>
    <link rel="stylesheet" href="/static/style.css" />
</head>
<body>
    <h1>Ты заходишь на меня с {{request.remote_addr}}</h1>
</body>
</html>
```
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ cat static/style.css 
```
```css
body {background: lightsteelblue;}
```
```shell
devasc@labvm:~/labs/devnet-src/sample-app$
```

### Шаг 2: Обновите демо веб-приложение.
Теперь, когда вы изучили основные файлы веб-сайта, необходимо обновить файл sample_app.py, чтобы он отображал файл index.html, а не просто возвращал данные. Генерирование HTML-контента с помощью кода Python может быть громоздким, особенно при использовании условных операторов или повторяющихся структур. HTML-файл может быть отрисован во Flask автоматически с помощью функции render_template. Для этого необходимо импортировать метод render_template из библиотеки flask и внести правки в возвращаемую функцию. Внесите выделенные правки в ваш скрипт.
```python
from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)
```

### Шаг 3: Сохраните и запустите свой скрипт.
Сохраните и запустите `sample_app.py`. Вы должны получить результат, подобный следующему:
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ python3 sample_app.py 
 * Serving Flask app "sample-app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
```

### Шаг 4: Убедитесь, что ваша программа запущена.
Опять же, вы можете проверить, что ваша программа запущена, одним из двух способов.

### Шаг 5: Остановите сервер.
Вернитесь в окно терминала, в котором запущен сервер, и нажмите CTRL+C, чтобы остановить сервер.

## Часть 5: Создаём Bash скрипт для создания и запуска Docker контейнера
> Приложение может быть развернуто на сервере (физический сервер, предназначенный для однопользовательской среды) или на виртуальной машине, как вы только что сделали в предыдущей части. Оно также может быть развернуто в контейнерном решении, таком как Docker. В этой части мы создадим bash скрипт, который создаёт и запускает Docker контейнер.

### Шаг 1: Создайте временные директории для хранения файлов сайта.
Откройте bash скрипт `sample-app.sh` в каталоге ~/labs/devnet-src/sample-app. Добавьте 'she-bang' и команды для создания структуры каталогов с tempdir в качестве родительской папки.
```bash
#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static
```

### Шаг 2: Скопируйте каталоги сайта и sample_app.py во временную директорию.
В файл `sample-app.sh` добавьте команды для копирования каталога сайта и скрипта в tempdir.
```bash
cp sample_app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.
```

### Шаг 3: Создайте Dockerfile.
На этом шаге мы добавим необходимые команды bash echo в файл sample-app.sh для создания Dockerfile в tempdir. Этот Dockerfile будет использоваться для сборки контейнера.
Вам нужен Python, запущенный в контейнере, поэтому добавьте команду Docker FROM для установки Python в контейнер.
```bash
echo "FROM python" >> tempdir/Dockerfile
```
Вашему приложению sample_app.py нужен Flask, поэтому добавьте команду Docker RUN для установки Flask в контейнер.
```bash
echo "RUN pip install flask" >> tempdir/Dockerfile
```
Вашему контейнеру понадобятся каталоги сайта и `sample_app.py` для запуска приложения, поэтому добавьте команды Docker COPY, чтобы добавить их в каталог в контейнере Docker. В этом примере вы создадите /home/myapp в качестве родительского каталога внутри контейнера Docker. Помимо копирования файла sample_app.py в Dockerfile, вы также скопируете файл index.html из каталога templates и файл style.css из каталога static.
```bash
echo "COPY  ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY  ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY  sample_app.py /home/myapp/" >> tempdir/Dockerfile
```
С помощью команды Docker EXPOSE откройте порт 8080 для использования веб-сервером.
```bash
echo "EXPOSE 8080" >> tempdir/Dockerfile
```
Наконец, добавьте команду Docker CMD для выполнения сценария Python.
```bash
echo "CMD python3 /home/myapp/sample_app.py" >> tempdir/Dockerfile
```

### Шаг 4: Соберите Docker контейнер.
Добавьте команды в файл `sample-app.sh` для перехода в каталог tempdir и сборки контейнера Docker. Опция -t команды docker build позволяет указать имя контейнера, а задняя точка (.) указывает, что вы хотите, чтобы контейнер был собран в текущем каталоге.
```bash
cd tempdir
docker build -t sampleapp .
```

### Шаг 5: Запустите контейнер и убедитесь, что он работает.
Добавьте команду docker run в файл `sample-app.sh`, чтобы запустить контейнер.
```bash
docker run -t -d -p 8080:8080 --name samplerunning sampleapp
```
В параметрах запуска docker указано следующее:
- `-t` указывает, что для контейнера создаётся терминал, для доступа к нему через командную строку.
- `-d` указывает, что контейнер будет работать в фоновом режиме, а также печатает container ID при выполнении команды docker ps -a.
- `-p` указывает, что вы хотите опубликовать внутренний порт контейнера на хосте. Первое "8080" указывает на порт приложения, запущенного в контейнере docker (наше демо). Второе "8080" указывает docker использовать этот порт на хосте. Эти значения не обязательно должны быть одинаковыми. Например, внутренний порт 80 на внешний 800 (80:800).
- `--name` указывает сначала то, как вы хотите назвать экземпляр контейнера (samplerunning), а затем образ контейнера, на котором будет основан экземпляр (sampleapp). Имя экземпляра может быть любым. Однако имя образа должно соответствовать имени контейнера, которое вы указали в команде сборки docker (sampleapp).
Добавьте команду `docker ps -a` для отображения всех запущенных в данный момент контейнеров Docker. Эта команда будет последней, выполняемой bash скриптом.
```bash
docker ps -a
```

### Шаг 6: Сохраните ваш bash скрипт.

## Часть 6: Сборка, запуск и проверка Docker контейнера
> В этой части мы запустим bash скрипт, который создаст каталоги, скопирует файлы, создаст Dockerfile, соберёт Docker контейнер, запустит экземпляр контейнера Docker и отобразит вывод команды docker ps -a с подробной информацией о запущенном контейнере. Затем вы исследуете контейнер Docker, остановите его работу и удалите контейнер.
> Примечание: Убедитесь, что вы остановили все другие процессы веб-сервера, которые могли быть запущены в предыдущих частях этой лабораторной работы.

### Шаг 1: Запустите bash-скрипт.
Запустите bash-скрипт из командной строки. Вы должны увидеть вывод, похожий на следующий. После создания каталогов tempdir сценарий выполняет команды для создания контейнера Docker. Обратите внимание, что шаг 7/7 в выводе выполняет sample_app.py, который создает веб-сервер. Также обратите внимание на идентификатор контейнера. Вы увидите его в командной строке Docker позже в лабораторной работе.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ bash ./sample-app.sh 
Sending build context to Docker daemon  6.144kB
Step 1/7 : FROM python
latest: Pulling from library/python
90fe46dd8199: Pulling fs layer 
35a4f1977689: Pulling fs layer 
bbc37f14aded: Pull complete 
74e27dc593d4: Pull complete 
4352dcff7819: Pull complete 
deb569b08de6: Pull complete 
98fd06fa8c53: Pull complete 
7b9cc4fdefe6: Pull complete 
512732f32795: Pull complete 
Digest: sha256:ad7fb5bb4770e08bf10a895ef64a300b288696a1557a6d02c8b6fba98984b86a
Status: Downloaded newer image for python:latest
 ---> 4f7cd4269fa9
Step 2/7 : RUN pip install flask
 ---> Running in 32d28026afea
Collecting flask
  Downloading Flask-1.1.2-py2.py3-none-any.whl (94 kB)
Collecting click>=5.1
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
Collecting Jinja2>=2.10.1
  Downloading Jinja2-2.11.2-py2.py3-none-any.whl (125 kB)
Collecting Werkzeug>=0.15
  Downloading Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Collecting itsdangerous>=0.24
  Downloading itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting MarkupSafe>=0.23
  Downloading MarkupSafe-1.1.1-cp38-cp38-manylinux1_x86_64.whl (32 kB)
Installing collected packages: click, MarkupSafe, Jinja2, Werkzeug, itsdangerous, flask
Successfully installed Jinja2-2.11.2 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 flask-1.1.2 itsdangerous-1.1.0
Removing intermediate container 32d28026afea
 ---> 619aee23fd2a
Step 3/7 : COPY  ./static /home/myapp/static/
 ---> 15fac1237eec
Step 4/7 : COPY  ./templates /home/myapp/templates/
 ---> dc807b5cf615
Step 5/7 : COPY  sample_app.py /home/myapp/
 ---> d4035a63ae14
Step 6/7 : EXPOSE 8080
 ---> Running in 40c2d35aa29a
Removing intermediate container 40c2d35aa29a
 ---> eb789099a678
Step 7/7 : CMD python3 /home/myapp/sample_app.py
 ---> Running in 41982e2c6209
Removing intermediate container 41982e2c6209
 ---> a2588e9b0593
Successfully built a2588e9b0593
Successfully tagged sampleapp:latest
8953a95374ff8ebc203059897774465312acc8f0ed6abd98c4c2b04448a56ba5
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                  PORTS                    NAMES
f674aad75d9e        sampleapp           "/bin/sh -c 'python …"   1 second ago        Up Less than a second   0.0.0.0:8080->8080/tcp   samplerunning
devasc@labvm:~/labs/devnet-src/sample-app$
```

### Шаг 2: Исследуйте запущенный Docker контейнер и веб-приложение.
Создание каталогов tempdir не отображается в выводе. Вы можете добавить команду echo для вывода сообщений об успешном создании каталогов. Вы также можете убедиться в их наличии с помощью команды ls. Помните, что в этом каталоге находятся файлы и папки, используемые для создания контейнера и запуска веб-приложения. Это не контейнер, который был создан.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ ls tempdir/
Dockerfile  sample_app.py  static  templates
devasc@labvm:~/labs/devnet-src/sample-app$
```
Обратите внимание на Dockerfile, созданный вашим сценарием bash. Откройте этот файл, чтобы посмотреть, как он выглядит в окончательном виде без команд echo.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ cat tempdir/Dockerfile 
FROM python
RUN pip install flask
COPY  ./static /home/myapp/static/
COPY  ./templates /home/myapp/templates/
COPY  sample_app.py /home/myapp/
EXPOSE 8080
CMD python3 /home/myapp/sample_app.py
```
Вывод команды docker ps -a может быть трудночитаемым в зависимости от ширины экрана вашего терминала. Вы можете перенаправить его в текстовый файл, где его можно будет лучше просмотреть без обводки слов.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ docker ps -a >> running.txt
devasc@labvm:~/labs/devnet-src/sample-app$
```
Контейнер Docker создает свой собственный IP-адрес из адресного пространства частной сети. Убедитесь, что веб-приложение запущено и сообщает IP-адрес. В веб-браузере по адресу http://localhost:8080 вы должны увидеть сообщение Ты заходишь на меня с 172.17.0.1, отформатированное как H1 на светло-стальном голубом фоне. 

При желании вы также можете использовать команду curl.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ curl http://172.17.0.1:8080
```
```html
<html>
<head>
    <title>Sample app</title>
    <link rel="stylesheet" href="/static/style.css" />
</head>
<body>
    <h1>Ты заходишь на меня с 172.17.0.1</h1>
</body>
</html>devasc@labvm:~/labs/devnet-src/sample-app$ 
```
```shell
devasc@labvm:~/labs/devnet-src/sample-app$
```
По умолчанию Docker использует подсеть IPv4 172.17.0.0/16 для сети контейнеров. (При необходимости этот адрес можно изменить.) Введите команду ip address, чтобы отобразить все IP-адреса, используемые вашим экземпляром виртуальной машины DEVASC. Вы должны увидеть loopback-адрес 127.0.0.1, который веб-приложение использовало ранее в лабораторной работе, и новый интерфейс Docker с IP-адресом 172.17.0.1.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ ip address
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
<вывод опущен>
4: docker0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
    link/ether 02:42:c2:d1:8a:2d brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:c2ff:fed1:8a2d/64 scope link 
       valid_lft forever preferred_lft forever
<вывод опущен>
```

### Шаг 3: Получите доступ и исследуйте работающий контейнер.
Помните, что контейнер Docker — это способ инкапсуляции всего необходимого для запуска приложения, чтобы его можно было легко развернуть в различных средах — не только в вашей виртуальной машине DEVASC.

Чтобы получить доступ к работающему контейнеру, введите команду docker exec -it, указав имя работающего контейнера (samplerunning) и то, что вам нужна оболочка bash (/bin/bash). Опция -i указывает, что вы хотите, чтобы он был интерактивным, а опция -t указывает, что вы хотите получить терминальный доступ. Приглашение изменится на root@containerID. ID вашего контейнера будет отличаться от показанного ниже. Обратите внимание, что ID контейнера совпадает с ID, показанным в выводе docker ps -a.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ docker exec -it samplerunning /bin/bash
root@f674aad75d9e:/#
```
Теперь у вас есть доступ root к Docker контейнеру samplerunning. Отсюда вы можете использовать команды Linux для изучения контейнера Docker. Введите ls, чтобы просмотреть структуру каталогов на корневом уровне.
```shell
root@f674aad75d9e:/# ls
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
root@f674aad75d9e:/#
```
Вспомните, что в своём bash скрипте мы добавили команды в Dockerfile, которые скопировали каталоги и файлы вашего приложения в каталог home/myapp. Введите команду ls еще раз для этой папки, чтобы увидеть сценарий sample_app.py и каталоги. Чтобы лучше понять, что включено в ваш контейнер Docker, вы можете использовать команду ls для изучения других каталогов, таких как /etc и /bin.
```shell
root@f674aad75d9e:/# ls home/myapp/
sample_app.py  static  templates
root@f674aad75d9e:/#
```
Выйдите из контейнера Docker, чтобы вернуться в командную строку DEVASC VM.
```shell
root@f674aad75d9e:/# exit
exit
devasc@labvm:~/labs/devnet-src/sample-app$
```

### Шаг 4: Остановите и удалите Docker контейнер.
Вы можете остановить Docker контейнер с помощью команды docker stop, указав имя запущенного контейнера. Потребуется несколько секунд для очистки и кэширования контейнера. Вы можете убедиться, что он все ещё существует, введя команду docker ps -a. Однако, если вы обновите веб-страницу `http://localhost:8080`, вы увидите, что веб-приложение больше не запущено.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ docker stop samplerunning 
samplerunning
devasc@labvm:~/labs/devnet-src/sample-app$ docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                       PORTS               NAMES
f674aad75d9e        sampleapp           "/bin/sh -c 'python3…"   11 minutes ago      Exited (137) 5 seconds ago                       samplerunning
devasc@labvm:~/labs/devnet-src/sample-app$
```
Остановленный контейнер можно перезапустить с помощью команды docker start. Контейнер немедленно запустится.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ docker start samplerunning 
samplerunning
devasc@labvm:~/labs/devnet-src/sample-app$
```
Чтобы окончательно удалить контейнер, сначала остановите его, а затем удалите с помощью команды docker rm. Вы всегда можете восстановить его снова, выполнив программу sample-app. Для проверки удаления контейнера используйте команду docker ps -a.
```shell
devasc@labvm:~/labs/devnet-src/sample-app$ docker stop samplerunning 
samplerunning
devasc@labvm:~/labs/devnet-src/sample-app$ docker rm samplerunning 
samplerunning
devasc@labvm:~/labs/devnet-src/sample-app$ docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
devasc@labvm:~/labs/devnet-src/sample-app$
```