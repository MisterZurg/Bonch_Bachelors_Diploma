# Исследование инструментов разработки на языке Python
![Иллюстрация к работе](../Resourses/README-LR-3-1-12.png)
## Цель лабораторной работы:
- Часть 1: Запуск виртуальной машины DEVASC
- Часть 2: Обзор установки Python
- Часть 3: Виртуальные среды PIP и Python
- Часть 4: Совместное использование виртуальной среды

## Необходимые ресурсы:
- 1 ПК
- Virtual Box или VMWare
- DEVASC виртуальная машина

## Порядок выполнения работы
## Часть 1: Запуск виртуальной машины DEVASC
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.

## Часть 2: Обзор установки Python
Эти команды предоставляют вам базовые методы для получения дополнительной информации о локальной среде Python.

В виртуальной машине DEVASC можно проверить версию уже установленного Python с помощью команды python3 -V.
```shell
devasc@labvm:~$ python3 -V
Python 3.8.2
devasc@labvm:~$
```
Чтобы увидеть каталог для локальной среды Python, используйте команду which python3.
```shell
devasc@labvm:~$ which python3
/usr/bin/python3
devasc@labvm:~$
```

## Часть 3: PIP и виртуальные среды Python
> PIP расшифровывается как Pip Installs Packages. Многие люди впервые узнают о PIP и начинают использовать команды pip3 install на общесистемной установке Python. Когда вы выполняете команду pip3 install в своей системе, вы можете внести конкурирующие зависимости в свою системную установку, которые могут понадобиться или не понадобиться для всех проектов Python. Поэтому лучшей практикой является включение виртуальной среды Python. Затем установите только те пакеты, которые необходимы для проекта в этой виртуальной среде. Таким образом, вы будете точно знать, какие пакеты установлены в тех или иных условиях. Вы сможете легко переключать зависимости пакетов при переходе на новую виртуальную среду, не допуская сбоев и проблем из-за конкурирующих версий программного обеспечения.
Чтобы установить виртуальную среду Python, используйте инструмент venv в Python 3, а затем активируйте виртуальную среду, как показано в следующих шагах.

### Шаг 1: Создайте виртуальную среду Python 3.
Внутри виртуальной машины DEVASC измените каталог labs/devnet-src/python.
```shell
devasc@labvm:~$ cd labs/devnet-src/python/
devasc@labvm:~/labs/devnet-src/python$
```
Введите следующую команду, чтобы использовать инструмент venv для создания виртуальной среды Python 3 с именем devfun. Переключатель -m указывает Python запустить модуль venv. Имя выбирается программистом.
```shell
devasc@labvm:~/labs/devnet-src/python$ python3 -m venv devfun
devasc@labvm:~/labs/devnet-src/python$
```

### Шаг 2: Активируйте и протестируйте виртуальную среду Python 3.
Активируйте виртуальную среду. Подсказка изменится, чтобы указать имя среды, в которой вы сейчас работаете, в данном примере это devfun. Теперь, когда вы используете форму команды pip3 install здесь, система будет устанавливать пакеты только для активной виртуальной среды.
```shell
devasc@labvm:~/labs/devnet-src/python$ source devfun/bin/activate
(devfun) devasc@labvm:~/labs/devnet-src/python$ 
```
Выполните команду `pip3 freeze`, чтобы убедиться в отсутствии дополнительных пакетов Python, установленных в настоящее время в среде devfun.
```shell
(devfun) devasc@labvm:~/labs/devnet-src/python$ pip3 freeze
(devfun) devasc@labvm:~/labs/devnet-src/python$
Теперь установите пакет Python requests в среду devfun.
(devfun) devasc@labvm:~/labs/devnet-src/python$ pip3 install requests
Collecting requests
  Downloading requests-2.23.0-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 290 kB/s 
Collecting urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1
  Downloading urllib3-1.25.9-py2.py3-none-any.whl (126 kB)
     |████████████████████████████████| 126 kB 1.7 MB/s 
Collecting idna<3,>=2.5
  Downloading idna-2.9-py2.py3-none-any.whl (58 kB)
     |████████████████████████████████| 58 kB 18.3 MB/s 
Collecting certifi>=2017.4.17
  Downloading certifi-2020.4.5.1-py2.py3-none-any.whl (157 kB)
     |████████████████████████████████| 157 kB 19.8 MB/s 
Collecting chardet<4,>=3.0.2
  Downloading chardet-3.0.4-py2.py3-none-any.whl (133 kB)
     |████████████████████████████████| 133 kB 59.2 MB/s 
Installing collected packages: urllib3, idna, certifi, chardet, requests
Successfully installed certifi-2020.4.5.1 chardet-3.0.4 idna-2.9 requests-2.23.0 urllib3-1.25.9
(devfun) devasc@labvm:~/labs/devnet-src/python$
```
Повторно введите команду `pip3 freeze`, чтобы увидеть пакеты, установленные теперь в среде devfun.
```shell
(devfun) devasc@labvm:~/labs/devnet-src/python$ pip3 freeze
certifi==2020.4.5.1
chardet==3.0.4
idna==2.10
requests==2.24.0
urllib3==1.25.9
(devfun) devasc@labvm:~/labs/devnet-src/python$
```
Чтобы деактивировать виртуальную среду и вернуться к своей системе, введите команду deactivate.
```shell
(devfun) devasc@labvm:~/labs/devnet-src/python$ deactivate
devasc@labvm:~/labs/devnet-src/python$
```

### Шаг 3: Проверьте текущие пакеты, установленные в системной среде.
Введите команду s`ystem wide python3 -m pip freeze`, чтобы посмотреть, какие пакеты установлены в системной среде.
> Примечание: Поскольку Python 3 вызывается с помощью следующей команды, вы используете pip вместо pip3.

```shell
devasc@labvm:~/labs/devnet-src/python$ python3 -m pip freeze
ansible==2.9.4
apache-libcloud==2.8.0
appdirs==1.4.3
argcomplete==1.8.1
astroid==2.3.3
bcrypt==3.1.7
blinker==1.4
certifi==2019.11.28
<вывод опущен>
xmltodict==0.12.0
zipp==1.0.0
devasc@labvm:~/labs/devnet-src/python$
```
Если вы хотите быстро найти версию установленного пакета, передайте вывод в команду grep. Введите следующее, чтобы узнать версию установленного пакета requests.

```shell
devasc@labvm:~/labs/devnet-src/python$ python3 -m pip freeze | grep requests
requests==2.22.0
requests-kerberos==0.12.0
requests-ntlm==1.1.0
requests-toolbelt==0.9.1
requests-unixsocket==0.2.0
devasc@labvm:~/labs/devnet-src/python$ 
```

## Часть 4: Совместное использование виртуальной среды
> Вывод команды `pip3 freeze` имеет определенный формат не просто так. Вы можете использовать все перечисленные зависимости, чтобы другие люди, которые хотят работать над тем же проектом, что и вы, могли получить такое же окружение, как у вас.
Разработчик может создать файл требований, например, requirements.txt, с помощью команды pip3 freeze > requirements.txt. Затем другой разработчик может из другой активированной виртуальной среды использовать команду pip3 install -r requirements.txt для установки пакетов, необходимых проекту.

Повторно активируйте виртуальную среду devfun.
```shell
devasc@labvm:~/labs/devnet-src/python$ source devfun/bin/activate
(devfun) devasc@labvm:
```
Отправьте вывод команды pip3 freeze в текстовый файл requirements.txt.
```shell
(devfun) devasc@labvm:~/labs/devnet-src/python$ pip3 freeze > requirements.txt
```
Деактивируйте виртуальную среду devfun. С помощью команды ls можно увидеть, что файл requirements.txt находится в каталоге /python.
```shell
(devfun) devasc@labvm:~/labs/devnet-src/python$ deactivate
devasc@labvm:~/labs/devnet-src/python$ ls
devfun       file-access-input.py  if-acl.py       requirements.txt
devices.txt  file-access.py        if-vlan.py      while-loop.py
devnew       hello-world.py        person-info.py
```

Создайте и активируйте новую виртуальную среду Python под названием devnew.
```shell
devasc@labvm:~/labs/devnet-src/python$ python3 -m venv devnew
devasc@labvm:~/labs/devnet-src/python$ source devnew/bin/activate
(devnew) devasc@labvm:~/labs/devnet-src/python$
```
Используйте команду `pip3 install -r requirements.txt` для установки тех же пакетов, которые установлены в виртуальной среде devfun.
```shell
(devnew) devasc@labvm:~/labs/devnet-src/python$ pip3 install -r requirements.txt 
Collecting certifi==2020.4.5.1
  Using cached certifi-2020.4.5.1-py2.py3-none-any.whl (157 kB)
Collecting chardet==3.0.4
  Using cached chardet-3.0.4-py2.py3-none-any.whl (133 kB)
Collecting idna==2.9
  Using cached idna-2.9-py2.py3-none-any.whl (58 kB)
Requirement already satisfied: pkg-resources==0.0.0 in ./devnew/lib/python3.8/site-packages (from -r requirements.txt (line 4)) (0.0.0)
Collecting requests==2.23.0
  Using cached requests-2.23.0-py2.py3-none-any.whl (58 kB)
Collecting urllib3==1.25.9
  Using cached urllib3-1.25.9-py2.py3-none-any.whl (126 kB)
Installing collected packages: certifi, chardet, idna, urllib3, requests
Successfully installed certifi-2020.4.5.1 chardet-3.0.4 idna-2.9 requests-2.23.0 urllib3-1.25.9
(devnew) devasc@labvm:~/labs/devnet-src/python$
```
При вводе `pip3 freeze` в среде `devnew` вы должны увидеть следующий вывод.
```shell
(devnew) devasc@labvm:~/labs/devnet-src/python$ pip3 freeze
certifi==2020.4.5.1
chardet==3.0.4
idna==2.9
pkg-resources==0.0.0
requests==2.23.0
urllib3==1.25.9
```
Деактивируйте виртуальную среду `devnew`.
```shell
(devnew) devasc@labvm:~/labs/devnet-src/python$ deactivate
devasc@labvm:~/labs/devnet-src/python$
```