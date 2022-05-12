# Unit-тестирование на Python
![Иллюстрация к работе](../../Resourses/README-LR-3-5-7.png)
## Цель лабораторной работы:
- Часть 1: Запуск виртуальной машины DEVASC
- Часть 2: Изучение опций в unittest Framework
- Часть 3: Тестирование функции Python с помощью unittest
## Необходимые ресурсы:
- 1 ПК
- Virtual Box или VMWare
- DEVASC виртуальная машина

## Порядок выполнения работы
## Часть 1: Запуск виртуальной машины DEVASC
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.

## Часть 2: Изучение возможностей в unittest Framework
> Python предоставляет фреймворк модульного тестирования (называемый unittest) как часть стандартной библиотеки Python. Если вы не знакомы с этим фреймворком, изучите "Python unittest Framework" для ознакомления. Найдите его в Интернете, чтобы найти документацию на сайте python.org. Вам понадобятся эти знания или документация, чтобы ответить на вопросы этой части.

**Ответьте на следующие вопросы**
- Какой класс unittest вы используете для создания отдельного блока тестирования?

Программа запуска тестов отвечает за выполнение тестов и предоставление вам результатов. Программа запуска тестов может иметь графический интерфейс, но пока мы ограничимя командной строкой для запуска тестов.

- Как программа запуска тестов узнает, какие методы являются тестом?
- Какая команда выведет все опции для unittest, показанные в следующем выводе?
```shell
devasc@labvm:~/labs/devnet-src$ команда, дающая вывод ниже 
<вывод опущен>
optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        Verbose output
  -q, --quiet          Quiet output
  --locals             Show local variables in tracebacks
  -f, --failfast       Stop on first fail or error
  -c, --catch          Catch Ctrl-C and display results so far
  -b, --buffer         Buffer stdout and stderr during tests
  -k TESTNAMEPATTERNS  Only run tests which match the given substring

Examples:
  python3 -m unittest test_module               - run tests from test_module
  python3 -m unittest module.TestClass          - run tests from module.TestClass
  python3 -m unittest module.Class.test_method  - run specified test method
  python3 -m unittest path/to/test_file.py      - run tests from test_file.py
<Вывод опущен>
For test discovery all test modules must be importable from the top level
directory of the project.
devasc@labvm:~/labs/devnet-src$
```

## Часть 3: Тестирование функции Python с помощью unittest
> В этой части вы будете использовать unittest для тестирования функции, выполняющей рекурсивный поиск в объекте JSON. Функция возвращает значения, помеченные заданным ключом. Программистам часто приходится выполнять подобные операции с объектами JSON, возвращаемыми вызовами API.
> В этом тесте будут использоваться три файла, представленные в следующей таблице:

|Файл|Описание|
|---|----|
|`recursive_json_search.py`|	Этот скрипт будет включать функцию `json_search()`, которую мы хотим протестировать|
|`test_data.py`|	Это данные, которые ищет функция `json_search()`|
|`test_json_search.py`|	Это файл, который вы создадите для тестирования функции `json_search()` в сценарии `recursive_json_search.py`|

### Шаг 1: Просмотрите файл test_data.py.
Откройте файл ~/labs/devnet-src/unittest/test_data.py и изучите его содержимое. Эти данные в формате JSON типичны для данных, возвращаемых при вызове Cisco DNA Center API. Образец данных достаточно сложен, чтобы быть хорошим тестом. Например, в нем чередуются типы dict и list.
```shell
devasc@labvm:~/labs/devnet-src$ more unittest/test_data.py 
key1 = "issueSummary"
key2 = "XY&^$#*@!1234%^&"

data = {
  "id": "AWcvsjx864kVeDHDi2gB",
  "instanceId": "E-NETWORK-EVENT-AWcvsjx864kVeDHDi2gB-1542693469197",
  "category": "Warn",
  "status": "NEW",
  "timestamp": 1542693469197,
  "severity": "P1",
  "domain": "Availability",
  "source": "DNAC",
  "priority": "P1",
  "type": "Network",
  "title": "Device unreachable",
  "description": "This network device leaf2.abc.inc is unreachable from controll
er. The device role is ACCESS.",
  "actualServiceId": "10.10.20.82",
  "assignedTo": "",
  "enrichmentInfo": {
    "issueDetails": {
      "issue": [
        {
--More--(12%)
```

### Шаг 2: Создайте функцию json_search(), которую вы будете тестировать.
Наша функция должна принимать ключ и объект JSON в качестве входных параметров и возвращать список совпавших пар ключ/значение. Вот текущая версия функции, которую необходимо протестировать, чтобы убедиться, что она работает так, как задумано. Цель этой функции - сначала импортировать тестовые данные. Затем она ищет данные, которые соответствуют ключевым переменным в файле test_data.py. Если она находит совпадение, то добавляет совпавшие данные в список. Функция print() в конце печатает содержимое списка для первой переменной key1 = "issueSummary".
```python
from test_data import *


def json_search(key,input_object):
    ret_val=[]

    if isinstance(input_object, dict): # Словарь для обхода
        for k, v in input_object.items(): # поиск ключа в словаре
            if k == key:
                temp={k:v}
                ret_val.append(temp)
            if isinstance(v, dict): # значение является другим словарём, поэтому повторим поиск в нём
                json_search(key,v)
            elif isinstance(v, list): # это список
                for item in v:
                    if not isinstance(item, (str,int)): # если словарь или список также повторим поиск
                        json_search(key,item)
    else: # Обход списка, поскольку некоторые API возвращают объект JSON в виде списка
        for val in input_object:
            if not isinstance(val, (str,int)):
                json_search(key,val)
    return ret_val

print(json_search("issueSummary",data))
```
Откройте файл ~/labs/devnet-src/unittest/recursive_json_search.py.
Скопируйте приведенный выше код в файл и сохраните.

Запустите код. Вы должны получить отсутствие ошибок и вывод [ ], указывающий на пустой список. Если функция json_search() была закодирована правильно (а это не так), то это говорит о том, что нет данных с ключом "issueSummary", о которых сообщают данные JSON, возвращаемые Cisco DNA Center API. Другими словами, нет никаких проблем, о которых можно было бы сообщить.
```shell
devasc@labvm:~/labs/devnet-src/unittest$ python3 recursive_json_search.py 
[]
devasc@labvm:~/labs/devnet-src/unittest$
```
Но как узнать, что функция json_search() работает так, как задумано? Вы можете открыть файл test_data.py и выполнить поиск по ключу "issueSummary", как показано ниже. Если вы это сделаете, то действительно обнаружите, что проблема существует. Это небольшой набор данных и относительно простой рекурсивный поиск. Однако производственные данные и код редко бывают настолько простыми. Поэтому тестирование кода жизненно важно для быстрого поиска и исправления ошибок в коде.
```json
<Вывод опущен>
      "issue": [
        {
          "issueId": "AWcvsjx864kVeDHDi2gB",
          "issueSource": "Cisco DNA",
          "issueCategory": "Availability",
          "issueName": "snmp_device_down",
          "issueDescription": "This network device leaf2.abc.inc is unreachable from controller. The device role is ACCESS.",
          "issueEntity": "network_device",
          "issueEntityValue": "10.10.20.82",
          "issueSeverity": "HIGH",
          "issuePriority": "",
          "issueSummary": "Network Device 10.10.20.82 Is Unreachable From Controller",
          "issueTimestamp": 1542693469197,
          "suggestedActions": [
            {
<Вывод опущен>
```

### Шаг 3: Создайте несколько модульных тестов, которые будут проверять, работает ли функция так, как задумано.
Откройте файл ~ labs/devnet-src/unittest/test_json_search.py.
В первой строке сценария после комментария импортируйте библиотеку unittest.
```python
import unittest
```
Добавьте строки для импорта тестируемой функции, а также тестовых данных JSON, которые использует функция.
```python
from recursive_json_search import *
from test_data import *
```
Теперь добавьте следующий код класса json_search_test в файл test_json_search.py. Код создает подкласс TestCase фреймворка unittest. Класс определяет некоторые тестовые методы, которые будут использоваться для функции json_search() в сценарии recursive_json_search.py. Обратите внимание, что каждый тестовый метод начинается с test_, что позволяет фреймворку unittest обнаруживать их автоматически. Добавьте следующие строки в нижнюю часть файла ~labs/devnet-src/unittest/test_json_search.py:
```python
class json_search_test(unittest.TestCase):
    '''тестовый модуль для проверки поиска в `recursive_json_search.py`'''
    def test_search_found(self):
        '''ключ должен быть найден, возвразаемый список не должен быть пустым'''
        self.assertTrue([]!=json_search(key1,data))
    def test_search_not_found(self):
        '''ключ не должен быть найден, возвразаемый список должен быть пустым '''
        self.assertTrue([]==json_search(key2,data))
    def test_is_a_list(self):
        '''должен вернуть список'''
        self.assertIsInstance(json_search(key1,data),list)
```
В коде unittest вы используете три метода для тестирования функции поиска:
1)	Учитывая существующий ключ в объекте JSON, проверьте, может ли тестирующий код найти такой ключ.
2)	Учитывая несуществующий ключ в объекте JSON, проверьте, подтверждает ли тестирующий код, что ключ не может быть найден.
3)	Проверьте, возвращает ли наша функция список, как она всегда должна делать.

Для создания этих тестов сценарий использует некоторые встроенные методы assert класса unittest TestCase для проверки условий. Метод assertTrue(x) проверяет, истинно ли условие, а assertIsInstance(a, b) проверяет, является ли a экземпляром типа b. Здесь используется тип list.
Также обратите внимание, что комментарии для каждого метода задаются с помощью тройной одинарной кавычки ('''). Это необходимо, если вы хотите, чтобы при выполнении теста выводилось описание метода теста. Использование одинарного символа хэша (#) для комментария не позволит вывести описание неудачного теста.

В последней части сценария добавьте метод unittest.main(). Это позволит запускать unittest из командной строки. Цель if __name__ == '__main__' — убедиться, что метод unittest.main() запускается только при непосредственном выполнении скрипта. Если сценарий импортирован в другую программу, unittest.main() не будет запущен. Например, для выполнения этого теста вы можете использовать не unittest, а другую программу запуска тестов.
```python
if __name__ == '__main__':
    unittest.main()
```

### Шаг 4: Запустите тест, чтобы увидеть первые результаты.
Запустите тестовый сценарий в его текущем состоянии, чтобы посмотреть, какие результаты он возвращает в данный момент. Во-первых, вы видите пустой список. Во-вторых, вы видите выделенный символ .F. в выводе. Точка (.) означает, что тест прошел, а F означает, что тест не прошел. Таким образом, первый тест прошел, второй тест не прошел, а третий тест прошел.
```shell
devasc@labvm:~/labs/devnet-src/unittest$ python3 test_json_search.py 
 []
.F.
======================================================================
FAIL: test_search_found (__main__.json_search_test)
ключ должен быть найден, возвразаемый список не должен быть пустым
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_json_search.py", line 11, in test_search_found
    self.assertTrue([]!=json_search(key1,data))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
devasc@labvm:~/labs/devnet-src/unittest$
```
Чтобы вывести каждый тест и его результаты, запустите сценарий снова под unittest с опцией verbose (-v). Обратите внимание, что для сценария test_json_search.py не требуется расширение .py. Вы можете видеть, что ваш метод тестирования `test_search_found` не работает.

> Примечание: Python не обязательно запускает тесты по порядку. Тесты запускаются в алфавитном порядке на основе имен методов тестирования.
```shell
devasc@labvm:~/labs/devnet-src/unittest$ python3 -m unittest -v test_json_search
```

### Шаг 5: Исследуйте и исправьте первую ошибку в сценарии recursive_json_search.py.
Утверждение, `ключ должен быть найден, возвращаемый список не должен быть пустым .... FAIL`, указывает на то, что ключ не найден. Почему? Если мы посмотрим на текст нашей рекурсивной функции, то увидим, что выражение `ret_val=[ ]` выполняется многократно, каждый раз, когда вызывается функция. Это приводит к тому, что функция опустошает список и теряет накопленные результаты от выражения `ret_val.append(temp)`, который добавляет в список, созданный `ret_val=[ ]`.
```python
def json_search(key,input_object):
    ret_val=[]
    if isinstance(input_object, dict):
        for k, v in input_object.items():
            if k == key:
                temp={k:v}
                ret_val.append(temp)
```
Переместите ret_val=[ ] из нашей функции в recursive_json_search.py, чтобы итерация не перезаписывала каждый раз накопленный список.
```python
ret_val=[]
def json_search(key,input_object):
```
Сохраните и запустите сценарий. Вы должны получить следующий результат, который подтверждает, что вы решили проблему. После выполнения сценария список больше не пуст.
```shell
devasc@labvm:~/labs/devnet-src/unittest$ python3 recursive_json_search.py 
[{'issueSummary': 'Network Device 10.10.20.82 Is Unreachable From Controller'}]
devasc@labvm:~/labs/devnet-src/unittest$
```

### Шаг 6: Запустите тест снова, чтобы проверить, все ли ошибки в сценарии теперь исправлены.
Вы получили некоторый вывод при последнем запуске `recursive_json_search.py`, однако вы ещё не можете быть уверены, что устранили все ошибки в сценарии? Запустите unittest снова без опции -v и посмотрите, возвращает ли `test_json_search` какие-либо ошибки. Как правило, вы не испольуете опцию -v, чтобы минимизировать вывод на консоль и ускорить выполнение тестов. В начале журнала вы можете увидеть ..F, что означает третий тест не прошел. Также обратите внимание, что список все еще распечатывается. Вы можете остановить это поведение, удалив функцию `print()` в сценарии `resursive_json_search.py`. Но это не обязательно.
```shell
devasc@labvm:~/labs/devnet-src/unittest$ python3 -m unittest test_json_search
[{'issueSummary': 'Network Device 10.10.20.82 Is Unreachable From Controller'}]
..F
======================================================================
FAIL: test_search_not_found (test_json_search.json_search_test)
ключ не должен быть найден, возвразаемый список должен быть пустым
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/devasc/labs/devnet-src/unittest/test_json_search.py", line 14, in test_search_not_found
    self.assertTrue([]==json_search(key2,data))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (failures=1)
devasc@labvm:~/labs/devnet-src/unittest$
```
Откройте файл test_data.py и найдите `issueSummary`, который является значением для key1. Вы должны найти его дважды, но только один раз в объекте данных JSON. Но если вы будете искать значение key2, который является XY&^$#*@!1234%^&, вы обнаружите его только вверху, где он определен, потому что его нет в объекте JSON данных. Третий тест проверяет, что его там нет. В комментарии к третьему тесту говорится, что ключ не должен быть найден, должен возвращаться пустой список. Однако функция вернула непустой список.

### Шаг 7: Исследуйте и исправьте вторую ошибку в сценарии recursive_json_search.py.
Просмотрите код `recursive_json_search.py` ещё раз. Обратите внимание, что ret_val теперь является глобальной переменной после того, как вы исправили её в предыдущем шаге. Это означает, что её значение сохраняется при нескольких вызовах функции json_search(). Это хороший пример того, почему использование глобальных переменных в функциях - плохая практика.

Чтобы решить эту проблему, оберните функцию `json_search()` внешней функцией. Удалите существующую функцию json_search() и замените её рефакторингом, приведенным ниже: (Вызов функции дважды не повредит, но повторение функции - не лучшая практика :/).
```python
from test_data import *

def json_search(key,input_object):
    """
    Поиск ключа в объекте JSON, ничего не возвращается, если ключ не найден
    key : "keyword" для поиска, с учетом регистра
    input_object : JSON объект, который нужно разобрать, в данном случае test_data.py
    inner_function() фактически выполняет рекурсивный поиск
    возвращает список пар key:value
    """
    ret_val=[]
    def inner_function(key,input_object):
        if isinstance(input_object, dict): # Словарь для обхода
            for k, v in input_object.items(): # поиск ключа в словаре
                if k == key:
                    temp={k:v}
                    ret_val.append(temp)
                if isinstance(v, dict): # значение является другим словарём, поэтому повторим поиск в нём
                    inner_function(key,v)
                elif isinstance(v, list):
                    for item in v:
                        if not isinstance(item, (str,int)): # если это словарь или список также повторим поиск
                            inner_function(key,item)
        else: # Обход списка, поскольку некоторые API возвращают объект JSON в виде списка
            for val in input_object:
                if not isinstance(val, (str,int)):
                    inner_function(key,val)
    inner_function(key,input_object)
    return ret_val

print(json_search("issueSummary", data))
```
Сохраните файл и запустите unittest в каталоге. Вам не нужно имя файла. Это потому, что функция unittest Test Discovery запустит любой найденный локальный файл, имя которого начинается с test. Вы должны получить следующий результат. Обратите внимание, что все тесты теперь пройдены и список для ключа "issueSummary" заполнен. Вы можете смело удалить функцию print(), поскольку она обычно не используется, когда этот тест объединяется с другими тестами для более масштабного тестирования.
```shell
devasc@labvm:~/labs/devnet-src/unittest$ python3 -m unittest
[{'issueSummary': 'Network Device 10.10.20.82 Is Unreachable From Controller'}]
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
devasc@labvm:~/labs/devnet-src/unittest$
```