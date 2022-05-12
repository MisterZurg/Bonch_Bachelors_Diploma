# Интеграция REST API и Python приложения
## Цель лабораторной работы:
- Часть 1: Запуск виртуальной машины DEVASC
- Часть 2: Демонстрация приложения MapQuest Directions
- Часть 3: Получение API-ключа MapQuest
- Часть 4: Создание базового приложения MapQuest Direction
- Часть 5: Обновление приложения MapQuest Directions с помощью дополнительных функций
- Часть 6: Тестирование полной функциональности приложения

## Необходимые ресурсы:
- 1 ПК
- Virtual Box или VMWare
- DEVASC виртуальная машина

## Порядок выполнения работы
## Часть 1: Запуск виртуальной машины DEVASC
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.

## Часть 2: Демонстрация приложения MapQuest Directions
> В этой лабораторной работе мы создадим сценарий для MapQuest Directions Application шаг за шагом.
> Приложение запрашивает начальное местоположение и пункт назначения. Затем оно запрашивает JSON-данные из MapQuest Directions API, анализирует их и отображает полезную информацию.
> ```shell
> >>>
> Начальное местоположение: Washington
> Место назначения: Baltimore
> URL: https://www.mapquestapi.com/directions/v2/route?key=ваш_api_ключ&from=Washington&to=Baltimore
> API Статус: 0 = Успешный вызов маршрута.
> 
> Маршрут из Washington в Baltimore
> Продолжительность поездки:   00:49:19
> Километры:      61.32
> Использованное топливо (Литр.): 6.24
> =============================================
> Start out going north on 6th St/US-50 E/US-1 N toward Pennsylvania Ave/US-1 Alt N. (1.28 км)
> Turn right onto New York Ave/US-50 E. Continue to follow US-50 E (Crossing into Maryland). (7.51 км)
> Take the Balt-Wash Parkway exit on the left toward Baltimore. (0.88 км)
> Merge onto MD-295 N. (50.38 км)
> Turn right onto W Pratt St. (0.86 км)
> Turn left onto S Calvert St/MD-2. (0.43 км)
> Welcome to BALTIMORE, MD. (0.00 км)
> =============================================
> 
> Начальное местоположение: quit
> >>>
> ```

## Часть 3: Получение API-ключа MapQuest
> Перед созданием приложения необходимо выполнить следующие шаги, чтобы получить ключ MapQuest API.

Перейдите по адресу: `https://developer.mapquest.com/`.
Нажмите кнопку **Sign Up** в верхней части страницы.
Заполните форму для создания новой учетной записи. Для компании введите SPbSUT
После нажатия кнопки `Sign Me Up` вы будете перенаправлены на страницу Manage Profile, нажмите Manage Keys в списке опций слева.
Разверните My Application и нажмите Approve.

Скопируйте Consumer Key в текстовый файл для дальнейшего использования. Этот ключ, будет использовать до конца этой лабораторной работы.

## Часть 4: Создание базового приложения MapQuest Direction
> В этой части вы создадите сценарий Python для отправки URL запроса к MapQuest directions API. Затем вы протестируете свой вызов API. На протяжении всей этой лабораторной работы вы будете создавать свой скрипт по частям, каждый раз сохраняя файл с новым именем. Это поможет в изучении частей приложения, а также даст вам серию сценариев, к которым вы сможете вернуться, если столкнетесь с какими-либо проблемами в текущей версии вашего приложения.

### Шаг 1: Создайте новый файл в VS Code.
Откройте VS Code.
Select File > Open Folder...
Перейдите в каталог ~/labs/devnet-src/mapquest и нажмите OK. Этот каталог в настоящее время пуст, и в нем вы будете хранить каждую итерацию вашего приложения.
Select File > New File.
Select File > Save as..., назовите файл mapquest_parse-json_1.py и нажмите Save.

### Шаг 2: Импорт модулей для приложения.
Чтобы начать сценарий разбора данных JSON, вам нужно импортировать два модуля из библиотеки Python: requests и urllib.parse. Модуль requests предоставляет функции для получения данных JSON из URL. Модуль urllib.parse предоставляет множество функций, которые позволят вам разбирать и манипулировать данными JSON, полученными в результате запроса к URL.
Добавьте следующие импорты в верхней части вашего сценария.
```python
import urllib.parse
import requests
```
Выберите Terminal > New Terminal, чтобы открыть терминал внутри VS Code.
Сохраните и запустите свой сценарий. Вы не должны получить никаких ошибок. Для проверки функциональности кода, вам придётся часто сохранять и запускать свои скрипты.
```shell
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_1.py 
devasc@labvm:~/labs/devnet-src/mapquest$
```

### Шаг 3: Создайте URL для запроса к API направлений MapQuest.
Первым шагом в создании запроса API является создание URL, который ваше приложение будет использовать для вызова. Первоначально URL будет представлять собой комбинацию следующих переменных:
- main_api — основной URL, к которому вы обращаетесь
- orig — параметр для точки отправления
- dest — параметр для пункта назначения
- key — ключ API MapQuest, который вы получили с сайта разработчика.
Создайте переменные для построения URL, который будет отправлен в запросе. В следующем коде замените ваш_api_ключ на Consumer Key, который вы скопировали из своего аккаунта разработчика MapQuest.
```python
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C."
dest = "Baltimore, Md"
key = "ваш_api_ключ"
```
Объедините четыре переменные main_api, orig, dest и key, чтобы отформатировать запрошенный URL. Используйте метод urlencode для правильного форматирования значения адреса. Эта функция формирует часть параметров URL и преобразует возможные специальные символы в значении адреса в допустимые (например, пробел в "+", а запятую в "%2C").
```python
url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 
```
Создайте переменную для хранения ответа запрашиваемого URL и выведите возвращаемые данные в формате JSON. В переменной json_data хранится представление словаря Python's Dictionary ответа в формате json, полученного методом get модуля requests. Метод requests.get выполнит вызов API MapQuest API. Оператор print будет временно использоваться для проверки возвращаемых данных. Вы замените этот оператор print на более сложные варианты отображения данных позже в лабораторной работе.
```python
json_data = requests.get(url).json()
print(json_data)
```
Ваш окончательный код должен выглядеть следующим образом, но с другим значением для ключа.
```python
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington, D.C."
dest = "Baltimore, Md"
key = "DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy" #Замените на свой ключ MapQuest

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)
```

### Шаг 4: Протестируйте URL-запрос.
Сохраните и запустите сценарий `mapquest_parse-json_1.py` и убедитесь, что он работает.
При необходимости устраните неполадки в коде. Хотя ваш результат может немного отличаться, вы должны получить ответ в формате JSON, похожий на следующий. Обратите внимание, что выходной сигнал представляет собой словарь с двумя парами ключ/значение. Значением для ключевого маршрута является другой словарь, который включает дополнительные словари и списки. Ключ info включает пару ключ/значение statuscode, которую вы будете использовать позже в лабораторной работе.
```shell
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_1.py
{'route': {'hasTollRoad': False, 'hasBridge': True, 'boundingBox': {'lr': {'lng': -76.612137, 'lat': 38.892063}, 'ul': {'lng': -77.019913, 'lat': 39.290443}}, 'distance': 38.089, 'hasTimedRestriction': False, 'hasTunnel': False, 'hasHighway': True, 'computedWaypoints': [], 'routeError': {'errorCode': -400, 'message': ''}, 'formattedTime': '00:49:29', 'sessionId': '5eadfc17-00ee-5f21-02b4-1a24-0647e6e69816', 'hasAccessRestriction': False, 'realTime': 2915, 'hasSeasonalClosure': False, 'hasCountryCross': False, 'fuelUsed': 1.65, 'legs': [{'hasTollRoad': False, 'hasBridge': True, 'destNarrative': 'Proceed to BALTIMORE, MD.', 'distance': 38.089, 'hasTimedRestriction': False, 'hasTunnel': False, 'hasHighway': True, 'index': 0, 'formattedTime': '00:49:29', 'origIndex': -1, 'hasAccessRestriction': False, 'hasSeasonalClosure': False, 'hasCountryCross': False, 'roadGradeStrategy': [[]], 'destIndex': 3, 'time': 2969, 'hasUnpaved': False, 'origNarrative': '', 'maneuvers': [{'distance': 0.792, 'streets': ['6th St', 'US-50 E', 'US-1 N'], 'narrative': 'Start out going north on 6th St/US-50 E/US-1 N toward Pennsylvania Ave/US-1 Alt N.', 'turnType': 0, 'startPoint': {'lng': -77.019913, 'lat': 38.892063}, 'index': 0, 'formattedTime': '00:02:06', 'directionName': 'North', 'maneuverNotes': [], 'linkIds': [], 'signs': [{'extraText': '', 'text': '50', 'type': 2, 'url': 'http://icons.mqcdn.com/icons/rs2.png?n=50&d=EAST', 'direction': 8}, {'extraText': '', 'text': '1', 'type': 2, 'url': 'http://icons.mqcdn.com/icons/rs2.png?n=1&d=NORTH', 
<<<<<                  >>>>>
      вывод опущен
<<<<<                  >>>>>
'geocodeQuality': 'CITY', 'adminArea1Type': 'Country', 'adminArea3Type': 'State', 'latLng': {'lng': -76.61233, 'lat': 39.29044}}], 'time': 2969, 'hasUnpaved': False, 'locationSequence': [0, 1], 'hasFerry': False}, 'info': {'statuscode': 0, 'copyright': {'imageAltText': '© 2019 MapQuest, Inc.', 'imageUrl': 'http://api.mqcdn.com/res/mqlogo.gif', 'text': '© 2019 MapQuest, Inc.'}, 'messages': []}}
devasc@labvm:~/labs/devnet-src/mapquest$
```
Измените переменные orig и dest. Повторно запустите сценарий, чтобы получить другие результаты. Чтобы получить желаемые результаты, лучше всего указывать и город, и штат для городов в США. При указании городов в других странах обычно используется либо английское название города и страны, либо родное название. Например:
```python
orig = "Saint-Petersburg, Russia"
dest = "Rome, Italy"
```
или
```python
orig = "Moscow, Russia"
dest = "Roma, Italia"
```

### Шаг 5: Выведите URL и проверьте статус JSON-запроса.
Теперь, когда вы знаете, что JSON-запрос работает, вы можете добавить еще немного функциональности в приложение.
Сохраните свой сценарий под именем `mapquest_parse-json_2.py`.
Удалите оператор `print(json_data)`, поскольку вам больше не нужно проверять правильность форматирования запроса.
Добавьте приведенные ниже утверждения, которые будут выполнять следующие действия:
- Выведите построенный URL, чтобы пользователь мог увидеть точный запрос, сделанный приложением.
- Разберите данные JSON, чтобы получить значение statuscode.
- Запустите цикл if, который проверяет успешность вызова, на что указывает возвращаемое значение 0. Добавьте оператор print для отображения значения statuscode и его значения. \n добавляет пустую строку под выводом.
```python
print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Статус: " + str(json_status) + " = Успешный вызов маршрута.\n")
```

### Шаг 6: Проверка состояния и команды печати URL.
В приведенном здесь примере используются следующие параметры.
```python
orig = "Washington, D.C."
dest = "Baltimore, Md"
```
Сохраните и запустите сценарий `mapquest_parse-json_2.py` и убедитесь, что он работает. При необходимости устраните неполадки в коде. Вы должны получить результат, похожий на следующий. Обратите внимание, что ваш ключ встроен в URL-запрос.
```shell
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_2.py
URL: https://www.mapquestapi.com/directions/v2/route?key=DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy&from=Washington%2C+D.C.&to=Baltimore%2C+Md
API Статус: 0 = Успешный вызов маршрута.

devasc@labvm:~/labs/devnet-src/mapquest$
```

### Шаг 7: Пользовательские данные для начального и конечного местоположений.
Вы использовали статические значения для переменных местоположения. Однако приложение требует, чтобы пользователь вводил их. Давайте обновим приложение:
Сохраните свой сценарий под именем `mapquest_parse-json_3.py`.
Перенесите переменные orig и dest внутрь цикла while, в котором запрашивается ввод пользователем начального местоположения и пункта назначения. Цикл while позволяет пользователю продолжать делать запросы для различных направлений. Добавьте следующий код, выделенный ниже, после ключевого параметра. Убедитесь, что весь оставшийся код правильно расположен с отступом внутри цикла while.
```python
import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?" 
key = "DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy"

while True:
   orig = input("Начальное местоположение: ")
   dest = input("Место назначения: ")
   url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
   print("URL: " + (url))
   json_data = requests.get(url).json()
   json_status = json_data["info"]["statuscode"]
   if json_status == 0:
       print("API Статус: " + str(json_status) + " = Успешный вызов маршрута.\n")
```

### Шаг 8: Протестируйте функциональность пользовательского ввода.
Запустите сценарий `mapquest_parse-json_3.py` и убедитесь, что он работает. При необходимости устраните неполадки в коде. Вы должны получить результат, подобный тому, что показан ниже. Чтобы завершить работу программы, введите Ctrl+C. Вы получите ошибку KeyboardInterrupt, как показано на рисунке ниже. Чтобы прекратить работу приложения более изящно, вы добавите функцию выхода из программы в следующем шаге.
```shell
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_3.py
Starting Location: Washington, D.C.
Destination: Baltimore, Md
URL: https://www.mapquestapi.com/directions/v2/route?key=fZadaFOY22VIEEemZcBFfxl5vjSXIPpZ&from=Washington%2C+D.C.&to=Baltimore%2C+Md
API Статус: 0 = Успешный вызов маршрута.

Starting Location: ^CTraceback (most recent call last):
  File "mapquest_parse-json_3.py", line 9, in <module>
    orig = input("Начальное местоположение: ")
KeyboardInterrupt

devasc@labvm:~/labs/devnet-src/mapquest$
```

### Шаг 9: Добавьте функцию выхода из приложения.
Вместо принудительного выхода из приложения с помощью прерывания клавиатуры вы добавите возможность для пользователя ввести q или quit в качестве ключевых слов для выхода из приложения. Выполните следующие шаги для обновления приложения:
Сохраните свой сценарий под именем `mapquest_parse-json_4.py`.
Добавьте оператор if после каждой переменной местоположения, чтобы проверить, вводит ли пользователь q или quit, как показано ниже.
```python
while True:
    orig = input("Начальное местоположение: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Место назначения: ")
    if dest == "quit" or dest == "q":
        break
```

### Шаг 10: Протестируйте функциональность выхода из системы.
Запустите сценарий `mapquest_parse-json_4.py` четыре раза, чтобы проверить каждую переменную местоположения. Убедитесь, что и quit, и q завершают работу приложения. При необходимости устраните неполадки в коде. Вы должны получить результат, похожий на следующий.
```shell
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_4.py
Начальное местоположение: q
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_4.py
Начальное местоположение: quit
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_4.py
Начальное местоположение: Washington, D.C
Место назначения: q
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_4.py
Начальное местоположение Starting Location: Washington, D.C.
Место назначения: quit
devasc@labvm:~/labs/devnet-src/mapquest$ 
```

### Шаг 11: Отображение данных JSON в JSONView.
Браузер Chromium в виртуальной машине DEVASC содержит расширение JSONView. Вы можете использовать его для просмотра объекта JSON в удобном для чтения, цветном и сворачиваемом формате.

Запустите ваш mapquest_parse-json_4.py снова и скопируйте код, возвращаемый для URL. Не используйте код, приведенный ниже. Ваш результат будет включать ваш ключ API.
```shell
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_4.py
Начальное местоположение: Washington, D.C.
Место назначения: Baltimore, Md
URL: https://www.mapquestapi.com/directions/v2/route?key=DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy&from=Washington%2C+D.C.&to=Baltimore%2C+Md
API Статус: 0 = Успешный вызов маршрута.
 
Starting Location: quit
devasc@labvm:~/labs/devnet-src/mapquest$
```
Вставьте URL в адресную строку браузера Chromium.
Сверните данные JSONView, выбрав тире "-" перед route, вы увидите, что есть два корневых словаря: route и info
```json
{
 - route:{
      hasTollRoad: false,
      hasBridge: true,
 <вывод опущен>
```
Вы увидите, что есть два корневых словаря: route и info. Обратите внимание, что info содержит пару ключ/значение statuscode, используемую в вашем коде.
```json
{
 + route: {},
 - info: {
       statuscode: 0,
     - copyright: {
           imageAltText: "© 2022 MapQuest, Inc.",
           imageUrl: "http://api.mqcdn.com/res/mqlogo.gif",
           text: "© 2022 MapQuest, Inc."
       },
       messages: [ ]
   }
}
```
Разверните словарь маршрутов route (нажмите на знак плюс "+" перед route) и изучите богатые данные. Там есть значения, указывающие, есть ли на маршруте платные дороги, мосты, туннели, шоссе, закрытия или пересечения с другими странами. Вы также должны увидеть значения расстояния, общего времени, которое займет поездка, и расхода топлива. Чтобы разобрать и отобразить эти данные в вашем приложении, вы должны указать словарь route, а затем выбрать пару ключ/значение, которую вы хотите вывести. В следующей части лабораторной работы вы выполните разбор словаря маршрутов.

## Часть 5: Обновление приложения MapQuest Directions с помощью дополнительных функций
В этой части мы добавим дополнительные функции в приложение MapQuest Directions, чтобы предоставить пользователю больше информации. Включим краткую информацию о поездке, а затем список направлений, разобранных из словаря ног. В качестве заключительного шага мы добавим базовую проверку ошибок для подтверждения вводимых пользователем данных.

### Шаг 1: Отображение краткой информации о поездке, включающей продолжительность, расстояние и использованное топливо.
Сохраните свой сценарий под именем `mapquest_parse-json_5.py`.
Ниже команды печати статуса API добавьте несколько операторов печати, которые отображают местоположение "от" и "до", а также ключи formattedTime, distance и fuelUsed.
Дополнительные операторы также включают операторы print, которые будут выводить двойную строку перед следующим запросом о начальном местоположении. Убедитесь, что эти утверждения встроены в функцию while True.
```python
if json_status == 0:
        print("API Статус: " + str(json_status) + " =  Успешный вызов маршрута.\n")
        print("=============================================")
        print("Маршрут из " + (orig) + " в " + (dest))
        print("Продолжительность поездки: " + (json_data["route"]["formattedTime"]))
        print("Мили: " + str(json_data["route"]["distance"]))
        print("Использованное топливо (Гал.): " + str(json_data["route"]["fuelUsed"]))
        print("=============================================")
```
Сохраните и запустите файл `mapquest_parse-json_5.py`, чтобы увидеть следующий результат.
```shell
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_5.py 
Начальное местоположение: Washington, D.C.
Место назначения: Baltimore, Md
URL: https://www.mapquestapi.com/directions/v2/route?key=DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy&from=Washington%2C+D.C.&to=Baltimore%2C+Md
API Статус: 0 = Успешный вызов маршрута.

=============================================
Маршрут из Washington, D.C. в Baltimore, Md
Продолжительность поездки:   00:49:17
Мили:           38.089
Использованное топливо (Гал.): 1.65
=============================================
Начальное местоположение: q
devasc@labvm:~/labs/devnet-src/mapquest$
```

По умолчанию MapQuest использует Британскую имперскую систему мер, и к сожалению, нет переключателя для изменения данных в метрическую систему. Поэтому, вероятно, нам следует преобразовать приложение для отображения метрических значений, как показано ниже.
```python
print("Километры:      " + str((json_data["route"]["distance"])*1.61))
print("Использованное топливо (Литр.): " + str((json_data["route"]["fuelUsed"])*3.78))
```
Запустите модифицированный сценарий `mapquest_parse-json_5.py`, чтобы увидеть следующий результат:
```shell
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_5.py
Начальное местоположение: Washington, D.C.
Место назначения: Baltimore, Md
URL: https://www.mapquestapi.com/directions/v2/route?key=DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy&from=Washington%2C+D.C.&to=Baltimore%2C+Md
API Статус: 0 = Успешный вызов маршрута.

=============================================
Маршрут из Washington, D.C. в Baltimore, Md
Продолжительность поездки: 00:49:17
Километры:      61.32329
Использованное топливо (Литр.): 6.236999999999999
=============================================
Начальное местоположение: q
devasc@labvm:~/labs/devnet-src/mapquest$
```

Лишние десятичные знаки для Километров и Использованного топлива ненесут особо важной информации. Используйте аргумент `"{:.2f}".format` для форматирования плавающих значений до 2 знаков после запятой перед преобразованием их в строковые значения, как показано ниже. Каждый оператор должен быть на одной строке.

```python    
print("Километры:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
print("Использованное топливо (Литр.): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
```

### Шаг 2: Протестируйте функциональность парсинга и форматирования.
Сохраните и запустите сценарий `mapquest_parse-json_5.py`, чтобы убедиться в его работоспособности. При необходимости устраните неполадки в коде. Убедитесь, что вы правильно расставили все открывающие и закрывающие круглые скобки. Вы должны получить результат, похожий на следующий.
```shell
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_5.py
Начальное местоположение: Washington, D.C.
Место назначения: Baltimore, Md
URL: https://www.mapquestapi.com/directions/v2/route?key=DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy&from=Washington%2C+D.C.&to=Baltimore%2C+Md
API Статус: 0 = Успешный вызов маршрута.

=============================================
Маршрут из Washington, D.C. в Baltimore, Md
Продолжительность поездки: 00:49:17
Километры:      61.32
Использованное топливо (Литр.):  6.24
=============================================
Начальное местоположение: q
devasc@labvm:~/labs/devnet-src/mapquest$
```

### Шаг 3: Просмотрите список маневров в данных JSON.
Теперь мы готовы отобразить пошаговый маршрут от начального места до пункта назначения. Вернитесь в браузер Chromium, где ранее вы просматривали вывод в JSONView. Если вы закрыли браузер, скопируйте URL-адрес с прошлого запуска программы и вставьте его в адресную строку браузера.
Внутри словаря route найдите список "legs". legs включает один большой словарь с большей частью данных JSON. Найдите список маневров maneuvers и сверните каждый из семи словарей внутри него, как показано ниже (нажмите на знак "-" минус, чтобы переключить его на знак "+" плюс). Если вы используете разные места, у вас, вероятно, будет разное количество словарей маневров.
```json
- legs: [
    - {
         hasTollRoad: false,
         hasBridge: true,
         destNarrative: "Proceed to BALTIMORE, MD.",
         distance: 38.089,
         hasTimedRestriction: false,
         hasTunnel: false,
         hasHighway: true,
         index: 0,
         formattedTime: "00:49:29",
         origIndex: -1,
         hasAccessRestriction: false,
         hasSeasonalClosure: false,
         hasCountryCross: false,
       - roadGradeStrategy: [
             [ ]
         ],
         destIndex: 3,
         time: 2969,
               hasUnpaved: false,
         origNarrative: "",
      - maneuvers: [
          + {…},
          + {…},
          + {…},
          + {…},
          + {…},
          + {…},
          + {…}
         ],
         hasFerry: false
     }
        ],
      - options: {
```
Разверните первый словарь в списке maneuvers. Каждый словарь содержит narrative ключ со значением, например, "Начать движение на север...", как показано ниже. Вам нужно разобрать данные JSON, чтобы извлечь значение для narrative ключа для отображения в вашем приложении.
```json
- legs: [
    - {
       hasTollRoad: false,
       hasBridge: true,
       destNarrative: "Proceed to BALTIMORE, MD.",
       distance: 38.089,
       hasTimedRestriction: false,
       hasTunnel: false,
       hasHighway: true,
       index: 0,
       formattedTime: "00:49:29",
       origIndex: -1,
       hasAccessRestriction: false,
       hasSeasonalClosure: false,
       hasCountryCross: false,
     - roadGradeStrategy: [
           [ ]
       ],
       destIndex: 3,
       time: 2969,
             hasUnpaved: false,
       origNarrative: "",
    - maneuvers: [
        - {
             distance: 0.792,
           - streets: [
                 "6th St",
                 "US-50 E",
                 "US-1 N"
             ],
             narrative: "Start out going north on 6th St/US-50E/US-1 N toward Pennsylvania Ave/US-1 Alt N.",
             turnType: 0,
           - startPoint: {
                lng: -77.019913,
                lat: 38.892063
             },
             index: 0,
             formattedTime: "00:02:06",
             directionName: "North",
             maneuverNotes: [ ],
             linkIds: [ ],
           - signs: [
               - {
                     extraText: "",
                     ext: "50",
                     type: 2,
<вывод опущен>
```

> Примечание: Для отображения значения в описании была добавлена обводка слов.

### Шаг 4: Добавьте цикл for для итерации данных JSON маневров.
Выполните следующие шаги, чтобы обновить приложение для отображения значения ключа описания. Для этого необходимо создать цикл for, который будет итерационно просматривать список маневров, отображая значение описательной части для каждого маневра от начального места до пункта назначения.
Сохраните свой сценарий под именем `mapquest_parse-json_6.p`y.
Добавьте цикл for, выделенный ниже, после второго двустрочного оператора печати. Цикл for итерирует каждый список maneuvers и выполняет следующие действия:
Выводит значение narrative.
Конвертирует мили в километры с помощью *1.61
Форматирует значение километража для вывода только двух знаков после запятой с помощью функции "{:.2f}".format.
Добавьте `print()`, который будет отображать двойную строку перед тем, как приложение запросит другое начальное местоположение, как показано ниже.
```python
print("Использованное топливо (Литр.): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
print("=============================================")
for each in json_data["route"]["legs"][0]["maneuvers"]:
    print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " км)"))
print("=============================================\n")
```

### Шаг 5: Активность - тестирование итерации JSON.
Сохраните и запустите сценарий `mapquest_parse-json_6.py`, чтобы убедиться в его работоспособности. При необходимости устраните неполадки в коде. Вы должны получить результат, похожий на следующий:
```shell
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_6.py 
Начальное местоположение: Washington, D.C.
Место назначения: Baltimore, Md
URL: https://www.mapquestapi.com/directions/v2/route?key=DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy&from=Washington%2C+D.C.&to=Baltimore%2C+Md
API Статус: 0 = Успешный вызов маршрута.

=============================================
Маршрут из Washington, D.C. в Baltimore, Md
Продолжительность поездки: 00:49:17
Километры:      61.32
Использованное топливо (Литр.):  6.24
=============================================
Start out going north on 6th St/US-50 E/US-1 N toward Pennsylvania Ave/US-1 Alt N. (1.28 км)
Turn right onto New York Ave/US-50 E. Continue to follow US-50 E (Crossing into Maryland). (7.51 км)
Take the Balt-Wash Parkway exit on the left toward Baltimore. (0.88 км)
Merge onto MD-295 N. (50.38 км)
Turn right onto W Pratt St. (0.86 км)
Turn left onto S Calvert St/MD-2. (0.43 км)
Welcome to BALTIMORE, MD. (0.00 км)
=============================================

Начальное местоположение: q
devasc@labvm:~/labs/devnet-src/mapquest$
```

### Шаг 6: Проверка на недопустимый ввод данных пользователем.
Теперь вы готовы добавить последнюю функцию в ваше приложение, чтобы сообщать об ошибке, когда пользователь вводит недопустимые данные. Вспомните, что перед разбором данных JSON вы запустили цикл if, чтобы убедиться, что возвращаемый код состояния равен 0:
```python
json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Статус: " + str(json_status) + " = Успешный вызов маршрута.\n")
```

Но что произойдет, если код состояния не равен 0? Например, пользователь может ввести недопустимое местоположение или не ввести одно или несколько мест. Если это так, то приложение отображает URL и запрашивает новое начальное местоположение. Пользователь понятия не имеет, что произошло.

Чтобы вызвать отказ приложения без уведомления пользователя, попробуйте использовать в приложении следующие значения. Вы должны увидеть похожие результаты.
```shell
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_6.py 
Место назначения: Washington, D.C.
Продолжительность поездки: Beijing, China
URL: https://www.mapquestapi.com/directions/v2/route?key=DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy%2C+D.C.&to=Beijing%2C+China
Место назначения: Washington, D.C.
Продолжительность поездки: Bal
URL: https://www.mapquestapi.com/directions/v2/route?key=DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy&from=Washington%2C+D.C.&to=Bal
Место назначения: q
devasc@labvm:~/labs/devnet-src/mapquest$ 
```
Скопируйте один из URL-адресов на вкладку браузера Chromium. Обратите внимание, что единственная запись в словаре route - это словарь routeError с errorCode 2. В словаре info statuscode равен 402. Следовательно, ваш цикл if никогда не выполнял код для случая, когда statuscode равен 0.

Сохраните свой сценарий под именем `mapquest_parse-json_7.py`.

Чтобы предоставить информацию об ошибке, когда statuscode равен 402, 611 или другому значению, добавьте два оператора elif и оператор else в цикл if. Операторы elif и else должны быть согласованы с предыдущим оператором if. После последнего двустрочного оператора print в поле if json_status == 0 добавьте следующие операторы elif и else:
```python
    if json_status == 0:
       <объявления опущены>
       for each in json_data["route"]["legs"][0]["maneuvers"]:
           print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " км)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Статус: " + str(json_status) + "; Неверные данные пользователя для одной или обеих локаций.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Статус: " + str(json_status) + "; Отсутствие записи для одного или обоих мест.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("Для статуса: " + str(json_status) + "; Обратитесь:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
```
Первое утверждение elif выводится, если значение statuscode состояния равно 402 для недопустимого местоположения. Второе утверждение elif выводится, если значение statuscode равно 611, потому что пользователь не указал одно или оба местоположения. Оператор else печатается для всех других значений statuscode, например, когда сайт MapQuest выдает ошибку. Оператор else завершает цикл if/else и возвращает приложение к циклу while.

## Часть 6: Тестирование полной функциональности приложения
Запустите сценарий `mapquest_parse-json_7.py` и убедитесь, что он работает. При необходимости устраните неполадки в коде. Протестируйте все функции приложения. Вы должны получить результат, похожий на следующий.
```shell
devasc@labvm:~/labs/devnet-src/mapquest$ python3 mapquest_parse-json_7.py 
Начальное местоположение: Washington, D.C.
Место назначения: Baltimore, Md
URL: https://www.mapquestapi.com/directions/v2/route?key=DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy&from=Washington%2C+D.C.&to=Baltimore%2C+Md
API Статус: 0 = Успешный вызов маршрута.

=============================================
Маршрут из Washington, D.C. в Baltimore, Md
Продолжительность поездки:   00:49:29
Километры:      61.32
Использованное топливо (Литр.): 6.24
=============================================
Start out going north on 6th St/US-50 E/US-1 N toward Pennsylvania Ave/US-1 Alt N. (1.28 км)
Turn right onto New York Ave/US-50 E. Continue to follow US-50 E (Crossing into Maryland). (7.51 км)
Take the Balt-Wash Parkway exit on the left toward Baltimore. (0.88 км)
Merge onto MD-295 N. (50.38 км)
Turn right onto W Pratt St. (0.86 км)
Turn left onto S Calvert St/MD-2. (0.43 км)
Welcome to BALTIMORE, MD. (0.00 км)
=============================================

Начальное местоположение: Moscow, Russia
Место назначения: Beijing, China
URL: https://www.mapquestapi.com/directions/v2/route?key=DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy&from=Moscow%2C+Russia&to=Beijing%2C+China
API Статус: 0 = Успешный вызов маршрута.

=============================================
Маршрут из Moscow, Russia в Beijing, China
Trip Duration:   84:31:10
Километры:      7826.83
Использованное топливо (Литр.): 793.20
=============================================
Start out going west on Кремлёвская набережная/Kremlin Embankment. (0.37 км)
Turn slight right onto ramp. (0.15 км)
Turn slight right onto Боровицкая площадь. (0.23 км)
<вывод опущен>
Turn slight left onto 前门东大街/Qianmen East Street. (0.31 км)
Turn left onto 广场东侧路/E. Guangchang Rd. (0.82 км)
广场东侧路/E. Guangchang Rd becomes 东长安街/E. Chang'an Str. (0.19 км)
Welcome to BEIJING. (0.00 км)
=============================================

Начальное местоположение: Washington, D.C.
Место назначения: Beijing, China
URL: https://www.mapquestapi.com/directions/v2/route?key=DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy&from=Washington%2C+D.C.&to=Beijing%2C+China
**********************************************
Статус: 402; Неверные данные пользователя для одной или обеих локаций.
**********************************************

Начальное местоположение: Washington, D.C.
Место назначения: Bal
URL: https://www.mapquestapi.com/directions/v2/route?key=DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy&from=Washington%2C+D.C.&to=Bal
**********************************************
Статус: 402; Неверные данные пользователя для одной или обеих локаций.
**********************************************

Начальное местоположение: Washington, D.C.
Место назначения: 
URL: https://www.mapquestapi.com/directions/v2/route?key=DptE4HhC9zw3c71LbJHazOH7Q2C2hdRy&from=Washington%2C+D.C.&to=
**********************************************
Статус: 611; Отсутствие записи для одного или обоих мест.
**********************************************

Начальное местоположение: quit
devasc@labvm:~/labs/devnet-src/mapquest$
```