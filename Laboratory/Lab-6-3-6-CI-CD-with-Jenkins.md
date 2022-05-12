# Построение CI/CD Пайплайна с помощью Jenkins 
## Цель лабораторной работы:
- Часть 1: Запуск виртуальной машины DEVASC
- Часть 2: Закоммитьте Sample App на Git
- Часть 3: Изменение Sample App и внесение изменений в Git
- Часть 4: Загрузка и запуск Jenkins Docker Image
- Часть 5: Конфигурация Jenkins
- Часть 6: Использование Jenkins для запуска сборки вашего приложения
- Часть 7: Использование Jenkins для тестирования сборки
- Часть 8: Создание Пайплайна в Jenkins

## Необходимые ресурсы:
- 1 ПК
- Virtual Box или VMWare
- DEVASC виртуальная машина

## Порядок выполнения работы
## Часть 1: Запуск виртуальной машины DEVASC
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.

## Часть 2: Закоммитьте Sample App на Git
> В этой части вы создадите репозиторий GitHub для коммита файлов Sample App, созданного в 6.2.7. Вы создали учетную запись GitHub в предыдущей части. Если вы еще не сделали этого, посетите сайт github.com и создайте учетную запись.

### Шаг 1: Войдите на GitHub и создайте новый репозиторий.
Войдите на сайт `https://github.com/`, используя свои учетные данные.
Выберите кнопку "New repository" или нажмите на значок "+" в правом верхнем углу и выберите "New repository". 

Создайте репозиторий, используя следующую информацию:
- **Имя репозитория**: sample-app
- **Описание**: Изучение CI/CD с помощью GitHub и Jenkins
- **Видимость**: Private

> Примечание: Дополнительно можете выбрать чек бокс Add a README file в меню Initialize this repository withng, для более подробной информации зачем вам таковой.

Нажмите Create repository

### Шаг 2: Настройте учетные данные Git локально на виртуальной машине.
Откройте окно терминала с VS Code в DEVASC VM. Используйте свое имя вместо "Sample User" для имени в кавычках " ". Используйте @example.com для адреса электронной почты.
```shell
devasc@labvm:~$ git config --global user.name "Sample User"
devasc@labvm:~$ git config --global user.email sample@example.com
```

### Шаг 3: Инициализируйте каталог в качестве репозитория Git.
Мы будем использовать файлы sample-app, которые вы создали в предыдущей лабораторной работе. Однако эти файлы также хранятся для вашего удобства в каталоге /labs/devnet-src/jenkins/sample-app. Перейдите в каталог jenkins/sample-app и инициализируйте его как Git-репозиторий.
```shell
devasc@labvm:~$ cd labs/devnet-src/jenkins/sample-app/
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ git init
Initialized empty Git repository in /home/devasc/labs/devnet-src/jenkins/sample-app/.git/
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$
```

### Шаг 4: Свяжите локальный Git-репозиторий с репозиторием на GitHub.
С помощью команды `git remote add origin <URL>` свяжем локальный репозиторий, со вновь созданный репозиторий на GitHub. Используя URL репозитория Git, который вы создали в Шаге 1, вам нужно только заменить github-username в следующей команде на ваше имя пользователя GitHub.
```shell
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ git remote add origin https://github.com/github-username/sample-app.git
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ 
```

### Шаг 5: Застэйджите, закоммитьте и переместите файлы sample-app в репозиторий GitHub.
Используйте команду `git add` для стэджа файлов в каталог jenkins/sample-app. Используйте аргумент "звездочка" (*) для постановки всех файлов в текущем каталоге.
```shell
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ git add *
```
Используйте команду `git status`, чтобы увидеть файлы и каталоги, которые поставлены и готовы к коммиту в вашем репозитории GitHub.
```shell
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   sample-app.sh
        new file:   sample_app.py
        new file:   static/style.css
        new file:   templates/index.html

devasc@labvm:~/labs/devnet-src/jenkins/sample-app$
```
Используйте команду `git commit` для коммита стэйджовых файлов и начала отслеживания изменений. Добавьте сообщение по своему выбору или используйте предоставленное здесь.
```shell
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ git commit -m "Коммит файлов sample-app."
[master 4030ab6] Коммит файлов sample-app.
 4 files changed, 45 insertions(+)
 create mode 100644 sample-app.sh
 create mode 100644 sample_app.py
 create mode 100644 static/style.css
 create mode 100644 templates/index.html
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$
```
Используйте команду `git push`, чтобы перенести локальные файлы sample-app в ваш репозиторий GitHub.
```shell
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ git push origin master
Username for 'https://github.com': username
Password for 'https://MisterZurg@github.com': password 
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 2 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (8/8), 1.05 KiB | 1.05 MiB/s, done.
Total 8 (delta 0), reused 0 (delta 0)
To https://github.com/MisterZurg/sample-app.git
   d0ee14a..4030ab6  master -> master
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ 
```
После чего в браузере вам предолжат ввести ваши учётные данные.
> Примечание: Если вместо запроса имени пользователя вы получаете сообщение от VS Code с текстом: "Расширение 'Git' хочет войти, используя GitHub", значит, вы неправильно настроили учетные данные GitHub в Шаге 2 и/или URL GitHub в Шаге 4. URL должен содержать правильное имя пользователя с учетом регистра и имя репозитория, который вы создали в Шаге 1. Чтобы отменить предыдущую команду git add, выполните команду git remote rm origin. Затем вернитесь к Шагу 2, убедившись, что ввели правильные учетные данные, а в Шаге 4 введите правильный URL.

> Примечание: Если после ввода имени пользователя и пароля вы получаете фатальную ошибку о том, что репозиторий не найден, скорее всего, вы ввели неверный URL. Вам необходимо отменить команду git add командой git remote rm origin.

## Часть 3: Изменение Sample App и внесение изменений в Git
> В части 4 вы установите образ Jenkins Docker, который будет использовать порт 8080. Вспомните, что ваши файлы sample-app также указывают порт 8080. Сервер Flask и сервер Jenkins не могут одновременно использовать 8080.
В этой части вы измените номер порта, используемого файлами образца-приложения, запустите образец-приложение снова, чтобы убедиться, что оно работает на новом порту, а затем перенесите изменения в свой репозиторий GitHub.

### Шаг 1: Откройте файлы sample-app.
Убедитесь, что вы все еще находитесь в каталоге ~/labs/devnet-src/jenkins/sample-app, поскольку именно эти файлы связаны с вашим репозиторием GitHub. Откройте оба файла sample_app.py и sample-app.sh для редактирования.

### Шаг 2: Отредактируйте файлы sample-app.
В файле `sample_app.py` измените один экземпляр порта 8080 на 5050, как показано ниже.
```python
from flask import Flask
from flask import request
from flask import render_template

sample = Flask(__name__)

@sample.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=5050)
```
В файле sample-app.sh измените три экземпляра порта 8080 на 5050, как показано ниже.
```bash
#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp sample_app.py tempdir/.
cp -r templates/* tempdir/templates/.
cp -r static/* tempdir/static/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "COPY  ./static /home/myapp/static/" >> tempdir/Dockerfile
echo "COPY  ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY  sample_app.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python3 /home/myapp/sample_app.py" >> tempdir/Dockerfile

cd tempdir

docker build -t sampleapp .

docker run -t -d -p 5050:5050 --name samplerunning sampleapp
docker ps -a
```

### Шаг 3: Соберете и проверьте sample-app.
Введите команду bash для создания вашего приложения с использованием нового порта 5050.
```shell
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ bash ./sample-app.sh 
Sending build context to Docker daemon  6.144kB
Step 1/7 : FROM python
 ---> 2b7ca628da40
Step 2/7 : RUN pip install flask
 ---> Using cache
 ---> 4e39a3a408ea
Step 3/7 : COPY  ./static /home/myapp/static/
 ---> Using cache
 ---> 30711f334fd9
Step 4/7 : COPY  ./templates /home/myapp/templates/
 ---> Using cache
 ---> b7a429dbaaea
Step 5/7 : COPY  sample_app.py /home/myapp/
 ---> Using cache
 ---> 0eb49020f706
Step 6/7 : EXPOSE 5050
 ---> Using cache
 ---> 4dfe279482f4
Step 7/7 : CMD python /home/myapp/sample_app.py
 ---> Using cache
 ---> 90449d63de2c
Successfully built 90449d63de2c
Successfully tagged sampleapp:latest
99dcbf867e96843ff5bffdec30331659f9612898e7cc86d6953e21de88dcf8a3
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                  PORTS                    NAMES
99dcbf867e96        sampleapp           "/bin/sh -c 'python …"   1 second ago        Up Less than a second   0.0.0.0:5050->5050/tcp   samplerunning
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$
```
Откройте вкладку браузера и перейдите на localhost:5050. Вы должны увидеть сообщение Ты заходишь на меня с 172.17.0.1.
Выключите сервер, когда убедитесь, что он работает на порту 5050. Вернитесь в окно терминала, в котором запущен сервер, и нажмите CTRL+C, чтобы остановить сервер.

### Шаг 4: Запуште изменения на GitHub.
Теперь мы готовы перенести изменения в свой репозиторий GitHub. Введите следующие команды.
```shell
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ git add *
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   sample-app.sh
        modified:   sample_app.py
        new file:   tempdir/Dockerfile
        new file:   tempdir/sample_app.py
        new file:   tempdir/static/style.css
        new file:   tempdir/templates/index.html

devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ git commit -m "Изменён порт с 8080 на 5050."
[master 98d9b2f] Изменён порт с 8080 на 5050.
 6 files changed, 33 insertions(+), 3 deletions(-)
 create mode 100644 tempdir/Dockerfile
 create mode 100644 tempdir/sample_app.py
 create mode 100644 tempdir/static/style.css
 create mode 100644 tempdir/templates/index.html
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ git push origin master
```
> Примечание: Если вы авторизовывались через расширение GitHub Visual Studio, см. выше, повторный запрос пароля ниже, будет отстутствовать. И файлы сразу запушаться на GitHub.
```shell
Username for 'https://github.com': username
Password for 'https://MisterZurg@github.com': password
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 2 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 748 bytes | 748.00 KiB/s, done.
Total 6 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/MisterZurg/sample-app.git
   a6b6b83..98d9b2f  master -> master
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$
```
Вы можете проверить, что ваш репозиторий GitHub обновлен, посетив сайт https://github.com/github-user/sample-app. Вы должны увидеть новое сообщение (Изменён порт с 8080 на 5050.) и обновленную временную метку последнего коммита.

## Часть 4: Загрузка и запуск Jenkins Docker Image
> В этой части мы загрузим Jenkins Docker образ. Затем запустите его экземпляр и убедимся, что сервер Jenkins запущен.

### Шаг 1: Загрузите Jenkins Docker образ.
Docker Образ Jenkins хранится здесь: `https://hub.docker.com/r/jenkins/jenkins`. На момент написания этого пункта лабораторной работы в Overview указано, что для загрузки последней версии контейнера Jenkins следует использовать команду `docker pull jenkins/jenkins`.

Вы должны получить результат, похожий на следующий:
```shell
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ docker pull jenkins/jenkins
Using default tag: latest
latest: Pulling from jenkins/jenkins
6aefca2dc61d: Already exists 
53c03cc52d80: Pull complete 
4d0896265ff9: Pull complete 
2f62ad119e69: Pull complete 
44704a7fc5b5: Pull complete 
f4410ed22112: Pull complete 
7c492eb9cb22: Pull complete 
a3e3d06d7857: Pull complete 
7f5bbec44f2d: Pull complete 
be0b9dc5868f: Pull complete 
99dcd0e51757: Pull complete 
d5b8a7dcd362: Pull complete 
a16b1d85dde6: Pull complete 
9320f233b43f: Pull complete 
04c4ee4c1673: Pull complete 
0115957bf5a4: Pull complete 
929b8088475f: Pull complete 
Digest: sha256:f1058caddd535b238c80f49a2a7b0a9de71a82bb58d642472eba1f40258dc189
Status: Downloaded newer image for jenkins/jenkins:latest
docker.io/jenkins/jenkins:latest
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$
```

### Шаг 2: Запустите Jenkins Docker-контейнер.
Введите следующую команду в одну строку, она запустит Jenkins Docker-контейнер, а затем позволит выполнять команды Docker внутри вашего сервера Jenkins.
```shell
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ docker run --rm -u root -p 8080:8080 -v jenkins-data:/var/jenkins_home -v $(which docker):/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock -v "$HOME":/home --name jenkins_server jenkins/jenkins
```
Ниже перечислены опции, используемые в этой команде docker run:
- `--rm` — автоматически удаляет контейнер Docker, когда вы прекращаете его запуск.
- `-u` — указывает пользователя; этот Docker-контейнер запускается от имени root, соответственно, все команды Docker, введенные внутри сервера Jenkins, будут разрешены.
- `-p` — указывает порт, на котором будет локально работать сервер Jenkins.
- `-v` — связывают монтируемые тома, необходимые для Jenkins и Docker. Первый -v указывает, где будут храниться данные Jenkins. Второй -v указывает, где взять Docker, чтобы можно было запустить Docker внутри контейнера Docker, в котором запущен сервер Jenkins. Третий -v указывает переменную PATH для домашнего каталога.

## Шаг 3: Убедитесь, что сервер Jenkins запущен.
Теперь сервер Jenkins должен быть запущен. Скопируйте пароль администратора, который отображается в выводе, как показано ниже.
Не вводите никаких команд в этом окне сервера. Если вы случайно остановите сервер Jenkins, вам нужно будет снова ввести команду docker run из Шага 2 выше. После первоначальной установки пароль администратора отображается, как показано ниже.
```shell
<вывод опущен>
*************************************************************
*************************************************************
*************************************************************

Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

05ac6e20f40b40749ea8323b83129c99 <-- Ваш пароль будет другим

This may also be found at: /var/jenkins_home/secrets/initialAdminPassword

*************************************************************
*************************************************************
*************************************************************
<вывод опущен>
2022-05-04 20:10:47.055+0000 [id=22]    INFO    hudson.WebAppMain$3#run: Jenkins is fully up and running
```
> Примечание: Если вы потеряли пароль, или он не отображается, как показано выше, или вам необходимо перезапустить сервер Jenkins, вы всегда можете получить пароль, обратившись к командной строке докер-контейнера Jenkins. Создайте второе окно терминала в VS Code и введите следующие команды, чтобы не останавливать сервер Jenkins:

```shell
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ docker exec -it jenkins_server /bin/bash
root@f674aa47a54e:/# cat /var/jenkins_home/secrets/initialAdminPassword 
05ac6e20f40b40749ea8323b83129c99
root@f674aa47a54e:/# exit
exit
devasc@labvm:~/labs/devnet-src/jenkins/sample-app$
```

### Шаг 4: Исследуем уровни абстракции, которые в настоящее время работают на вашем компьютере.
Следующая диаграмма иллюстрирует уровни абстракции в этой реализации Docker-inside-Docker (dind). Такой уровень сложности не является необычным в современных сетях и облачных инфраструктурах.
```
+----------------------------------------+
| Операционная система вашего компьютера |
|  +----------------------------------+  |
|  | Вируальная Машина                |  |
|  |  +----------------------------+  |  |
|  |  | Docker контейнер           |  |  |
|  |  |  +----------------------+  |  |  |
|  |  |  | Jenkins сервер       |  |  |  |
|  |  |  |  +----------------+  |  |  |  |
|  |  |  |  |Docker контейнер|  |  |  |  |
|  |  |  |  +----------------+  |  |  |  |
|  |  |  +----------------------+  |  |  |
|  |  +----------------------------+  |  |
|  +----------------------------------+  |
+----------------------------------------+
```

## Часть 5: Конфигурация Jenkins
> В этой части мы завершим начальную настройку сервера Jenkins.

### Шаг 1: Откройте вкладку веб-браузера.
Перейдите по адресу `http://localhost:8080/` и войдите в систему, используя скопированный пароль администратора.

### Шаг 2: Установите рекомендуемые плагины Jenkins.
Нажмите Install suggested plugins и подождите, пока Jenkins загрузит и установит плагины. В окне терминала вы увидите сообщения журнала по мере выполнения установки. Убедитесь, что вы не закрыли это окно терминала. Вы можете открыть другое окно терминала для доступа к командной строке.

### Шаг 3: Пропустите создание нового администратора.
После завершения установки появится окно Create First Admin User. Пока что внизу нажмите Skip and continue as admin.

### Шаг 4: Пропустите создание экземпляра конфигурации.
В окне Instance Configuration ничего не меняйте. Нажмите кнопку Save and Finish.

### Шаг 5: Начните использовать Jenkins.
В следующем окне нажмите Start using Jenkins. Теперь вы должны оказаться на главном дашборде с сообщением Welcome to the club Buddy Jenkins!

## Часть 6: Использование Jenkins для запуска сборки вашего приложения
> Основной единицей Jenkins является job задание (также известная как проект). Вы можете создавать задания, которые выполняют различные задачи, включая следующие:
> - Получение кода из репозитория, например, GitHub.
> - Сборка приложения с помощью скрипта или инструмента сборки.
> - Упаковать приложение и запустить его на сервере.
>
> В этой части мы создадим простое задание Jenkins, которое получит последнюю версию вашего sample-app с GitHub и запустит сценарий сборки. Затем в Jenkins вы сможете протестировать свое приложение и добавить его в пайплайн разработки.

### Шаг 1: Создайте новое задание.
Щелкните ссылку Create a job прямо под сообщением Welcome to Jenkins! Кроме того, вы можете щелкнуть New Item в меню слева.

В поле Enter an item name заполните имя BuildAppJob.

Выберите проект Freestyle в качестве типа задания. В описании аббревиатура SCM означает управление конфигурацией программного обеспечения — это классификация программного обеспечения, которая отвечает за отслеживание и контроль изменений в программном обеспечении.

Прокрутите до самого низа и нажмите OK.

### Шаг 2: Настройте задание Jenkins BuildAppJob.
Теперь вы находитесь в окне конфигурации, где можно ввести подробную информацию о вашем задании. Вкладки в верхней части окна — это просто ярлыки для перехода к разделам ниже. Переходите по вкладкам, чтобы изучить параметры, которые можно настроить. Для этого простого задания вам нужно добавить только несколько деталей конфигурации.
Перейдите на вкладку General, добавьте описание для вашей работы. Например, "Моя первая работа в Jenkins".

Перейдите на вкладку Source Code Management и выберите кнопку Git. В поле Repository URL добавьте ссылку на репозиторий GitHub для примера приложения, указав имя пользователя с учетом регистра. Не забудьте добавить расширение .git в конце URL. Например:
`https://github.com/github-username/sample-app.git`
Поскольку парольная аутентификация нынче не в моде Support for password authentication was removed on August 13, 2021. Please use a personal access token instead.
Нам нужно создать personal access token если таковой отсутствует.
Перейдите на `https://github.com/settings/apps` 
В левой боковой панели нажмите Personal access tokens.

Нажмите **Generate new token**, после чего вам предложат ввести пароль.
Дайте своему Токену исчерпывающее имя, например. Jenkins BuildAppJob Token
Чтобы установить срок действия токена, выберите выпадающее меню Expiration, затем выберите значение по умолчанию или воспользуйтесь выбором календаря.

Выберите области действия, или разрешения, которые вы хотите предоставить этому токену. Чтобы использовать маркер для доступа к репозиториям из командной строки, выберите repo.

Обязательно скопируйте сгенерированный Personal access tokens. Поскольку больше не сможете его увидеть!
Воернитесь на вкладку Jenkins, в разделе Credentials нажмите кнопку Add и выберите Jenkins
В диалоговом окне Add Credentials введите имя пользователя и а на место пароля Personal access tokens который вы только что сгенерировали на GitHub, а затем нажмите кнопку Add.
Примечание: Вы получите сообщение об ошибке, что подключение не удалось. Это происходит потому, что вы еще не выбрали учетные данные.
В выпадающем списке Credentials, где сейчас написано None, выберите учетные данные, которые вы только что настроили.

После того как вы добавили правильный URL и учетные данные, Jenkins проверяет доступ к репозиторию. У вас не должно быть сообщений об ошибках. В противном случае проверьте URL и учетные данные. Вам нужно будет добавить их снова, поскольку на данном этапе нет возможности удалить ранее введенные.
В верхней части окна конфигурации BuildAppJob перейдите на вкладку Build.
В раскрывающемся списке Add build step выберите Execute shell.
В поле Command введите команду, которую вы используете для запуска сценария build for sample-app.sh.
```shell
bash ./sample-app.sh
```
Нажмите кнопку Save. Вы вернетесь на dashboard Jenkins с выбранным заданием BuildAppJob.

### Шаг 3: Поручите Jenkins создание приложения.
В левой части нажмите Build Now, чтобы запустить задание. Jenkins загрузит ваш Git-репозиторий и выполнит команду сборки bash ./sample-app.sh. Ваша сборка должна пройти успешно, потому что вы ничего не изменили в коде со времен части 3, когда вы модифицировали код.

### Шаг 4: Перейдите к деталям сборки.
Слева, в разделе Build History, нажмите на номер сборки, который должен быть №1, если вы не создавали приложение несколько раз.

### Шаг 5: Просмотрите вывод консоли.
Слева нажмите Console Output. Вы должны увидеть вывод, похожий на следующий. Обратите внимание на сообщения об успехе внизу, а также на вывод команды docker ps -a. Запущены два контейнера docker: один для вашего примера приложения работает на локальном порту 5050, а другой для Jenkins на локальном порту 8080.
```shell
Started by user admin
Running as SYSTEM
Building in workspace /var/jenkins_home/workspace/BuildAppJob
The recommended git tool is: NONE
using credential d31d1631-758c-4dc9-959d-a5417c3ba0ca
Cloning the remote Git repository
Cloning repository https://github.com/MisterZurg/sample-app.git
 > git init /var/jenkins_home/workspace/BuildAppJob # timeout=10
Fetching upstream changes from https://github.com/MisterZurg/sample-app.git
 > git --version # timeout=10
 > git --version # 'git version 2.30.2'
using GIT_ASKPASS to set credentials 
 > git fetch --tags --force --progress -- https://github.com/MisterZurg/sample-app.git +refs/heads/*:refs/remotes/origin/* # timeout=10
 > git config remote.origin.url https://github.com/MisterZurg/sample-app.git # timeout=10
 > git config --add remote.origin.fetch +refs/heads/*:refs/remotes/origin/* # timeout=10
Avoid second fetch
 > git rev-parse refs/remotes/origin/master^{commit} # timeout=10
Checking out Revision 2c32bef4efadc265ffa4dd4aec2594be2e76e6fc (refs/remotes/origin/master)
 > git config core.sparsecheckout # timeout=10
 > git checkout -f 2c32bef4efadc265ffa4dd4aec2594be2e76e6fc # timeout=10
Commit message: "Изменён порт с 8080 на 5050."
First time build. Skipping changelog.
[BuildAppJob] $ /bin/sh -xe /tmp/jenkins2049920068478646052.sh
+ bash ./sample-app.sh
mkdir: cannot create directory ‘tempdir’: File exists
mkdir: cannot create directory ‘tempdir/templates’: File exists
mkdir: cannot create directory ‘tempdir/static’: File exists
Sending build context to Docker daemon  6.656kB

Step 1/21 : FROM python
 ---> 2b7ca628da40
Step 2/21 : RUN pip install flask
 ---> Using cache
 ---> 4e39a3a408ea
Step 3/21 : COPY  ./static /home/myapp/static/
 ---> 85db350158f2
Step 4/21 : COPY  ./templates /home/myapp/templates/
 ---> 7a94185b6f05
Step 5/21 : COPY  sample_app.py /home/myapp/
 ---> 05dee7755ba7
Step 6/21 : EXPOSE 5050
 ---> Running in 8be5870fa2ac
Removing intermediate container 8be5870fa2ac
 ---> 444ec13b27e3
Step 7/21 : CMD python /home/myapp/sample_app.py
 ---> Running in af2a51be6b25
Successfully built af2a51be6b25
Successfully tagged sampleapp:latest
See 'docker run --help'.
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                     PORTS                               NAMES
5c85551452e9        jenkins/jenkins     "/sbin/tini -- /usr/…"   About an hour ago   Up About an hour           0.0.0.0:8080->8080/tcp, 50000/tcp   jenkins_server
99dcbf867e96        90449d63de2c        "/bin/sh -c 'python …"   2 hours ago         Exited (137) 2 hours ago                                       samplerunning
Finished: SUCCESS
```

### Шаг 6: Откройте другую вкладку веб-браузера и убедитесь, что образец приложения запущен.
Введите локальный адрес, localhost:5050. Вы должны увидеть, что содержимое вашего index.html отображается в светло-стальном синем цвете фона, а "Ты заходишь на меня с 172.17.0.1" отображается как H1.

## Часть 7: Использование Jenkins для тестирования сборки
> В этой части вы создадите второе задание, которое протестирует сборку, чтобы убедиться, что она работает правильно.
> Примечание: Вам необходимо остановить и удалить докер-контейнер samplerunning.
> ```shell
> devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ docker stop samplerunning 
> samplerunning
> devasc@labvm:~/labs/devnet-src/jenkins/sample-app$ docker rm samplerunning 
> samplerunning
> ```

### Шаг 1: Начните новое задание для тестирования вашего образца-приложения.
Вернитесь на вкладку в браузере с Jenkins и вернитнсь на главную страницу.
Щелкните ссылку **New Item**, чтобы создать новое задание.
В поле **Enter an item** name введите имя TestAppJob.
В качестве типа задания выберите **Freestyle project**.
Прокрутите страницу до самого низа и нажмите OK.

### Шаг 2: Настройте задание Jenkins TestAppJob.
Добавьте описание вашего задания. Например, "Мой первый тест Jenkins".
Оставьте для параметра Source Code Management значение None.
Перейдите на вкладку Build Triggers и установите флажок Build after other projects are built. Для Projects to watch заполните имя BuildAppJob.

### Шаг 3: Напишите тестовый скрипт, который должен запускаться после стабильной сборки BuildAppJob.
Перейдите на вкладку Build.
Нажмите Add build step и выберите **Execute shell**.
Введите следующий скрипт. Команда if должна быть вся на одной строке, включая ; then. Эта команда выполнит grep вывода, возвращаемого командой cURL, чтобы увидеть, возвращается ли сообщение You are calling me from 172.17.0.1. Если true, сценарий завершается с кодом 0, что означает отсутствие ошибок в сборке BuildAppJob. Если false, сценарий завершается с кодом 1, что означает, что BuildAppJob не удалось.
```shell
if curl http://172.17.0.1:5050/ | grep "Ты заходишь на меня с 172.17.0.1"; then
   exit 0
else
   exit 1
fi
```
Нажмите кнопку Save, а затем ссылку Back to Dashboard.

### Шаг 4: Попросите Jenkins снова запустить задание BuildAppJob.
Обновите веб-страницу с помощью кнопки обновления браузера.
Теперь вы должны увидеть два задания, перечисленные в таблице. Для задания BuildAppJob нажмите кнопку сборки в крайнем правом углу (часы со стрелкой).

### Шаг 5: Убедитесь, что оба задания выполнены.
Если все идет хорошо, вы должны увидеть, что временная метка в столбце Last Success обновилась как для BuildAppJob, так и для TestAppJob. Это означает, что ваш код для обоих заданий выполнился без ошибок. Но вы также можете проверить это самостоятельно.

> Примечание: Если временные метки не обновляются, убедитесь, что включена функция автоматического обновления, нажав на ссылку в правом верхнем углу.
> Примечание: Если TestAppJob фейлится, возможно потому, что в index.html в заголвке располагается You are calling me from 172.17.0.1, вам потребуется либо изменить `<h1>` в `index.html` на `<h1>Ты заходишь на меня с {{request.remote_addr}}</h1>` либо в конфигурации TestAppJob заменить `grep "You are calling me from с 172.17.0.1`"

Щелкните ссылку для TestAppJob. В разделе Permalinks щелкните ссылку для последней сборки, а затем щелкните Console Output. Вы должны увидеть вывод, похожий на следующий:
```shell
Started by upstream project "BuildAppJob" build number 6
originally caused by:
 Started by user admin
Running as SYSTEM
Building in workspace /var/jenkins_home/workspace/TestAppJob
[TestAppJob] $ /bin/sh -xe /tmp/jenkins17682716252211920304.sh
+ curl http://172.17.0.1:5050/
+ grep Ты заходишь на меня с 172.17.0.1
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100   192  100   192    0     0  96000      0 --:--:-- --:--:-- --:--:-- 96000
    <h1>Ты заходишь на меня с 172.17.0.1</h1>
+ exit 0
Finished: SUCCESS
```
Нет необходимости проверять, запущен ли ваш Sample App, поскольку TestAppJob уже сделал это за вас. Однако вы можете открыть вкладку браузера для 172.17.0.1:5050, чтобы убедиться, что оно действительно запущено.

## Часть 8: Создание Пайплайна в Jenkins
> Хотя в настоящее время вы можете запустить два задания, просто нажав кнопку Build Now для BuildAppJob, проекты по разработке программного обеспечения обычно намного сложнее. Эти проекты могут значительно выиграть от автоматизации сборок для непрерывной интеграции изменений кода и постоянного создания сборок разработки, готовых к развертыванию. В этом и заключается суть CI/CD. Пайплайе может быть автоматизирован для запуска на основе различных триггеров, в том числе периодически, на основе “прослушивания” GitHub на предмет изменений или из удаленно запущенного скрипта. Однако в этой части мы напишем скрипт пайплайна в Jenkins, который будет запускать ваши два приложения каждый раз, когда вы нажмете кнопку Build Now.

### Шаг 1: Создайте задание Pipeline.
Нажмите Jenkins в левом верхнем углу, а затем New Item.
В поле Enter an item name введите SamplePipeline. 
Выберите Pipeline в качестве типа задания.

Прокрутите страницу до самого низа и нажмите OK.

### Шаг 2: Настройте задание SamplePipeline.
Вдоль верхней части перейдите по вкладкам и изучите каждый раздел страницы конфигурации. Обратите внимание, что существует несколько различных способов инициировать сборку. Для задания SamplePipeline вы будете запускать его вручную.
В разделе Pipeline добавьте следующий сценарий.
```shell
node {
   stage('Preparation') {
       catchError(buildResult: 'SUCCESS') {
          sh 'docker stop samplerunning'
          sh 'docker rm samplerunning'
       }
   }
   stage('Build') {
       build 'BuildAppJob'
   }
   stage('Results') {
       build 'TestAppJob'
   }
}
```
Этот скрипт выполняет следующие действия:
- Он создает сборку состоящую из одной ноды в отличие от распределенной или мульти-нодовой. Распределенные или мульти-нодовой конфигурации предназначены для более крупных пайплайнов.
- На этапе Preparation SamplePipeline сначала убедится, что все предыдущие экземпляры Docker -контейнера BuildAppJob остановлены и удалены. Но если еще нет запущенного контейнера, вы получите ошибку. Поэтому мы используем функцию catchError, чтобы отловить любые ошибки и вернуть значение "SUCCESS". Это обеспечит продолжение работы пайплайна на следующем этапе.
- На этапе Build, SamplePipeline создаст ваше задание BuildAppJob.
- На этапе результатов SamplePipeline создаст ваше задание TestAppJob.
Нажмите кнопку Save, и вы вернетесь на дашбоард Jenkins для задания SamplePipeline.

### Шаг 3: Запустите SamplePipeline.
Слева нажмите Build Now, чтобы запустить задание SamplePipeline. Если вы написали скрипт Pipeline без ошибок, то в представлении Stage View должны появиться три зеленых поля с количеством секунд, затраченных на сборку каждого этапа. Если это не так, нажмите Configure слева, чтобы вернуться к конфигурации SamplePipeline и проверить свой сценарий Pipeline.

### Шаг 4: Проверьте вывод SamplePipeline.
Щелкните на ссылке последней сборки в разделе Permalinks, а затем щелкните Console Output. Вы должны увидеть вывод, похожий на следующий:
```shell
Started by user admin
[Pipeline] Start of Pipeline
[Pipeline] node
Running on Jenkins in /var/jenkins_home/workspace/SamplePipeline
[Pipeline] {
[Pipeline] stage
[Pipeline] { (Preparation)
[Pipeline] catchError
[Pipeline] {
[Pipeline] sh
+ docker stop samplerunning
samplerunning
[Pipeline] sh
+ docker rm samplerunning
samplerunning
[Pipeline] }
[Pipeline] // catchError
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Build)
[Pipeline] build (Building BuildAppJob)
Scheduling project: BuildAppJob
Starting building: BuildAppJob #7
[Pipeline] }
[Pipeline] // stage
[Pipeline] stage
[Pipeline] { (Results)
[Pipeline] build (Building TestAppJob)
Scheduling project: TestAppJob
Starting building: TestAppJob #5
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
```