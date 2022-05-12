# Создание Python программы для управления Webex Teams
## Цель лабораторной работы:
- Часть 1: Создание сети и проверка подключения
- Часть 2: Получение Access Token для Webex Teams
- Часть 3: Проверка Access Token
- Часть 4: Управление людьми в Webex Teams
- Часть 5: Управление комнатами в Webex Teams
- Часть 6: Управление членством в Webex Teams
- Часть 7: Управление сообщениями в Webex Teams

## Необходимые ресурсы:
- 1 ПК
- Virtual Box или VMWare
- DEVASC виртуальная машина

## Порядок выполнения работы
## Часть 1: Запуск виртуальной машины DEVASC
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.

> Примечание: В рамках лабораторной работы "Установка лабораторной среды виртуальной машины" необходимо установить приложение Webex Teams и добавить в список контактов как минимум еще одного человека. Это необходимо сделать до начала работы над лабораторной работой.

## Часть 2: Получение Access Token для Webex Teams
> В этой части вы зарегистрируетесь или войдете в свою учетную запись Webex, изучите документацию по API, получите свой маркер доступа, а затем протестируете свой маркер доступа, который вы будете использовать в своих вызовах API.

### Шаг 1: Войдите в Webex
Откройте веб-браузер Chromium.
Перейдите на веб-сайт разработчика Webex: `https://developer.webex.com/`.
Войдите в систему, если у вас уже есть учетная запись. Если нет, пройдите процесс регистрации.

### Шаг 2: Изучите документацию по API.
Нажмите Documentation.
Webex имеет множество API, которые вы можете использовать в своих приложениях. Щелкните API, чтобы раскрыть его подменю. 
Изучите все разновидности вызовов API. В этой лабораторной работе мы будем использовать документацию API для People, Rooms, Membership и Message.

### Шаг 3: Получите токен доступа.
Находясь в разделе Documentation, при необходимости прокрутите страницу назад к верху и нажмите Getting Started в разделе REST API. 
В разделе Accounts and Authentication обратите внимание, что Webex поддерживает персональный токен доступа. Токен аутентификации требуется для всех вызовов REST API. Нажмите Copy в разделе Your Personal Access Token. 

> Примечание: Персональный токен доступа предоставляет доступ к вашей учетной записи всем, кто его знает. Обязательно храните его в тайне.

> Примечание: Вы получите сообщение о том, что токен действителен в течение определенного периода времени, который на момент написания данной работы составлял 12 часов. Вам нужно будет получить новый токен и обновить Python скрипт, если вы вернетесь к этой работе после истечения срока действия токена. 

Скопируйте свой личный токен доступа в текстовый файл, чтобы использовать его в дальнейшем в этой лабораторной работе.

## Часть 3: Проверка Access Token
> Вы можете проверить свой токен доступа в документации OpenAPI на сайте разработчика. Однако вы будете использовать свой токен в сценариях Python. Поэтому вам следует проверить, что он работает и в сценарии.

### Шаг 1: Проверьте свой токен доступа на сайте разработчика.
Вы можете проверить свой токен доступа в документации OpenAPI по адресу https://developer.webex.com. 
Вернитесь в браузер и нажмите Documentation, если необходимо. 
В разделе Full API Reference нажмите People, а затем нажмите Get My Own Details.
На панели Try it справа обратите внимание, что ваш токен уже введён.

Вы можете нажать кнопку Try it или Run, чтобы проверить свой доступ. Вы увидите Response с вашей личной информацией. 

Нажмите Request, чтобы увидеть полный URL-адрес, использованный для отправки GET-запроса. Вы будете использовать этот URL на следующем шаге в своем сценарии Python.
В средней секции вы можете просмотреть всю документацию по Response Properties.

### Шаг 2: Используйте Python скрипт для проверки токена доступа.
Откройте VS code. Затем нажмите File > Open Folder... и перейдите в каталог devnet-src/webex-teams. Нажмите OK.
На панели EXPLORER теперь должны быть видны все файлы placeholder.py, которые вы будете использовать в этой лабораторной работе. Щелкните файл authentciation.py.
Поместите в файл следующий код. Не забудьте заменить your_token_here на ваш персональный токен доступа, который вы скопировали в предыдущем шаге.
```python
import requests
import json

access_token = 'your_token_here'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
```
Сохраните и запустите файл. Вы должны получить тот же результат, который вы видели в документации OpenAPI.

> Примечание: Значения некоторых ключей были сокращены в приведенном ниже выводе.
```shell
devasc@labvm:~/labs/devnet-src/webex-teams$ python3 authentication.py 
{
    "id": "Y2lz...c5NGE",
    "emails": [
        "ваша-почта@example.com"
    ],
    "phoneNumbers": [],
    "displayName": "Ваше-Имя Ваша-Фамилия",
    "nickName": "Ваше-Имя-Пользователя",
    "firstName": "Ваше-Имя",
    "lastName": "Ваша-Фамилия",
    "avatar": "https://9643-417f-9974...6baa4~1600",
    "orgId": "Y2lzY2...E1YjQ",
    "created": "2022-05-09T09:24:46.392Z",
    "lastActivity": "2022-05-10T21:46:03.765Z",
    "status": "active",
    "type": "person"
}
devasc@labvm:~/labs/devnet-src/webex-teams$
```

## Часть 4: Управление людьми в Webex Teams
> В Webex Teams люди — это зарегистрированные пользователи. С помощью API можно получить список людей, создать человека, получить данные об отдельном человеке, обновить человека и удалить его.

## Шаг 1: Найдите в документации API сведения о зарегистрированном пользователе Webex Teams.
Вернитесь на веб-сайт developer.webex.com. В разделе API Reference > People щелкните Method for List People.
В разделе Query Parameters, найдите параметр электронной почты. Это параметр, который вы будете использовать для поиска конкретного пользователя в вашей организации. В качестве альтернативы можно использовать параметр displayName, если вы знаете точное имя. Вы можете использовать функцию Try it.

## Шаг 2: Используйте Python скрипт для получения списка сведений о зарегистрированном пользователе Webex Teams.
В VS Code щелкните файл list-people.py
Поместите в файл следующий код. Обязательно замените your_token_here на ваш личный токен, а user@example.com — на реального пользователя Webex Team в вашей организации.
```python
import requests
import json

access_token = 'your_token_here'
url = 'https://webexapis.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    'email': 'user@example.com'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))
```
Сохраните и запустите скрипт. Вы должны получить вывод, аналогичный приведенному ниже. Если вы получите сообщение вида {'message': 'Invalid email address.'..., это означает, что вы не заменили пустой параметр email на легитимный адрес электронной почты зарегистрированного пользователя Webex Teams. Значение для ключа id будет использовано в следующем вызове API

> Примечание: Значения некоторых ключей были усечены в приведенном ниже выводе.
```shell
devasc@labvm:~/labs/devnet-src/webex-teams$ python3 list-people.py 
{
    "notFoundIds": null,
    "items": [
        {
            "id": "Y2l...2I", # Вы будете использовать это значение в следующем шаге
            "emails": [
                "user@example.com"
            ],
            "phoneNumbers": [
                {
                    "type": "mobile",
                    "value": "+1234567690"
                }
            ],
            "displayName": "displayName",
            "nickName": "nickName",
            "firstName": "firstName",
            "lastName": "lastName",
            "avatar": "https://9643-417f-9974...6baa4~1600",
            "orgId": "Y2lzY...UxMGY",
            "created": "2012-06-15T20:39:19.726Z",
            "lastActivity": "2022-05-10T21:46:03.765Z",
            "status": "active",
            "type": "person"
        }
    ]
}
devasc@labvm:~/labs/devnet-src/webex-teams$
```

### Шаг 3: Перечислите дополнительные административные данные человека.
Если вы являетесь администратором Webex Teams, вы можете получить дополнительные сведения о человеке, используя значение ключа person id в вызове API. Добавьте следующий код в сценарий list-people.py. Замените previous_id_here на значение id из предыдущего вызова API.
```python
person_id = 'previous_id_here'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
```
Сохраните файл и запустите его. Как человек, не являющийся администратором, вы получите информацию, очень похожую на предыдущий шаг.
```shell
devasc@labvm:~/labs/devnet-src/webex-teams$ python3 list-people.py 
{
    <вывод первого вызова API опущен>
}
{
    "id": "Y2l...2I",
    "emails": [
        "user@example.com"
    ],
    "phoneNumbers": [
        {
            "type": "mobile",
            "value": "+1234567890"
        }
    ],
    "displayName": "displayName",
    "nickName": "nickName",
    "firstName": "firstName",
    "lastName": "lastName",
    "avatar": "https://9643-417f-9974...6baa4~1600",
    "orgId": "Y2l...MGY",
    "created": "2012-06-15T20:39:19.726Z",
    "lastActivity": "2022-05-10T21:50:03.765Z",
    "status": "active",
    "type": "person"
}
devasc@labvm:~/labs/devnet-src/webex-teams$
```

## Часть 5: Управление комнатами в Webex Teams
> Комнаты, также называемые пространствами в пользовательском интерфейсе, позволяют людям отправлять сообщения и файлы для виртуального сотрудничества в местах коллективных встреч. В этой части вы увидите список комнат, создадите комнату и получите сведения о комнате.

### Шаг 1: Найдите и изучите документацию API для комнат.
Вернитесь на developer.webex.com. В разделе API Reference нажмите Rooms.
Изучите различные вызовы API, которые можно выполнить с помощью API Rooms.
Щелкните GET-запрос для List Rooms и изучите параметры запроса.

### Шаг 2: Используйте Python скрипт для составления списка всех комнат для аутентифицированного пользователя.
Для этого шага вам нужно быть участником хотя бы одной комнаты. Разговор с одним собеседником считается комнатой в Webex Teams.
В VS Code щелкните файл list-rooms.py.
Поместите в файл следующий код. Обязательно замените your_token_here на ваш личный маркер доступа.
```python
import requests

access_token = 'your_token_here'  
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(res.json())
```
Сохраните и запустите файл. Ваш результат будет отличаться от приведенного ниже. Здесь указана только одна комната. Значения идентификаторов были усечены.
```shell
devasc@labvm:~/labs/devnet-src/webex-teams$ python3 list-rooms.py 
{'items': [{'id': 'Y2l...ZTE0', 'title': 'User Name', 'type': 'direct', 'isLocked': False, 'lastActivity': '2022-05-10T22:14:27.361Z', 'creatorId': 'Y2lz...yM2U', 'created': '2022-05-10T22:14:27.361Z', 'ownerId': 'Y2lz...xMGY'}
# additional rooms displayed up to 'max' value.
]}
devasc@labvm:~/labs/devnet-src/webex-teams$
```

### Шаг 3: Найдите и изучите документацию по API для отправки сообщений в API Rooms.
Вернитесь на веб-сайт developer.webex.com. В разделе API Reference нажмите Rooms, если необходимо.
API Rooms имеет один метод POST для создания комнаты. Нажмите на ссылку посмотреть доступные Query Parameters. В своей программе вы будете использовать необходимый параметр title.

### Шаг 4: Используйте Python скрипт для создания комнаты.
В VS Code щелкните файл create-rooms.py.
Поместите в файл следующий код. Обязательно замените your_token_here на ваш личный маркер доступа. Обратите внимание, что это POST-запрос и в нем используется параметр title.
```python
import requests

access_token = 'your_token_here'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'Подготовка к собесу ASMR!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
```
Сохраните и запустите файл. Вы должны получить ответ, подобный следующему. Значения идентификаторов были усечены. Идентификатор и название комнаты выделены. Скопируйте идентификатор комнаты и сохраните его в текстовом файле для использования в дальнейшей работе.
```shell
devasc@labvm:~/labs/devnet-src/webex-teams$ python3 create-rooms.py 
{'id': 'Y2l...jEy', 'title': 'Подготовка к собесу ASMR!', 'type': 'group', 'isLocked': False, 'lastActivity': '2022-05-10T22:14:27.361Z', 'creatorId': 'Y2l...NGE', 'created': '2022-05-10T22:14:27.361Z', 'ownerId': 'Y2l...YjQY'}
devasc@labvm:~/labs/devnet-src/webex-teams$
```
В приложении Webex Teams проверьте, что теперь вы видите комнату DevNet Associate Training! В настоящее время вы являетесь единственным участником.

### Шаг 5: Используйте Python скрипт для получения информации о номере.
Что если вы хотите начать собрание в новой комнате? Вы можете сделать еще один вызов GET, чтобы получить адрес протокола инициирования сеанса (SIP), URL собрания и номера телефонов для набора.
В VS Code щелкните файл `get-room-details.py`.
Поместите в файл следующий код. Замените your_token_here на ваш персональный токен доступа. Замените your_room_id на значение, полученное в предыдущем шаге.
```python
import requests

access_token = 'your_token_here'
room_id = 'your_room_id'
url = 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(res.json())
```
Сохраните и запустите файл. Вы должны получить ответ, подобный следующему. Значения были усечены.
```shell
devasc@labvm:~/labs/devnet-src/webex-teams$ python3 get-room-details.py 
{'roomId': 'Y2l...jEy', 'meetingLink': 'https://cisco.webex.com/m/804...4fa2', 'sipAddress': '274...198@cisco.webex.com', 'meetingNumber': '274...7979', 'callInTollFreeNumber': '+8-800-...-3535', 'callInTollNumber': '+8-800-...-3535'}
devasc@labvm:~/labs/devnet-src/webex-teams$
```

## Часть 6: Управление членством в Webex Teams
> В этой части вы будете использовать API Membership, чтобы добавить кого-либо в свою комнату.

### Шаг 1: Найдите и изучите документацию API для членства.
Вернитесь на веб-сайт developer.webex.com. В разделе API Reference нажмите Memberships.
Изучите различные вызовы API, которые можно выполнить с помощью API Memberships.
Выберите GET-запрос для List Memberships и изучите параметры запроса.

### Шаг 2: Используйте Python скрипт для составления списка членов комнаты.
В VS Code щелкните файл list-memberships.py.
Поместите в файл следующий код. Замените your_token_here на ваш персональный токен доступа. Замените your_room_id на значение, полученное в предыдущей части.
```shell
import requests

access_token = 'your_token_here'
room_id = 'your_room_id'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id}
res = requests.get(url, headers=headers, params=params)
print(res.json())
```
Сохраните и запустите файл. Вы должны получить ответ, похожий на следующий. Вы должны быть единственным участником, если только вы не добавили кого-либо в приложение Webex Teams. Значения идентификаторов были усечены.
```shell
devasc@labvm:~/labs/devnet-src/webex-teams$ python3 list-memberships.py 
{'items': [{'id': 'Y2l...RjZg', 'roomId': 'Y2l...GNm', 'personId': 'Y2l...M2U', 'personEmail': 'user@example.com', 'personDisplayName': 'personDisplayName', 'personOrgId': 'Y2l...MGY', 'isModerator': False, 'isMonitor': False, 'created': '2022-05-10T22:16:27.361Z'}]}
devasc@labvm:~/labs/devnet-src/webex-teams$
```

### Шаг 3: Найдите и изучите документацию по API для отправки сообщений в Memberships API.
Вернитесь на веб-сайт developer.webex.com. В разделе API Reference нажмите Memberships, если необходимо.
API Memberships имеет один метод POST для Create a Membership. Нажмите на ссылку посмотреть доступные Query Parameters. В своем сценарии вы будете использовать необходимые параметры roomID и personEmail.

### Шаг 4: С помощью Python скрипта создайте членство, добавив кого-либо в комнату.
Для этого шага вам понадобится электронная почта другого человека, который является зарегистрированным пользователем Webex Teams в вашей организации. Вы можете использовать ту же электронную почту, которую вы использовали ранее для перечисления сведений о человеке.
В VS Code щелкните файл create-membership.py.
Поместите в файл следующий код. Замените `your_token_here` на ваш персональный токен доступа. Замените your_room_id на значение, полученное в предыдущей части. Замените new-user@example.com на email человека, которого вы хотите добавить в комнату.
```python
import requests

access_token = 'your_token_here'
room_id = 'your_room_id'
person_email = 'new-user@example.com'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())
```
Сохраните и запустите файл. Вы должны получить ответ, похожий на следующий. Вы должны быть единственным участником, если только вы не добавили кого-либо в приложение Webex Teams. Значения идентификаторов были усечены.
```shell
devasc@labvm:~/labs/devnet-src/webex-teams$ python3 list-memberships.py 
{'items': [{'id': 'Y2l...RjZg', 'roomId': 'Y2l...GNm', 'personId': 'Y2l...M2U', 'personEmail': 'user@example.com', 'personDisplayName': 'personDisplayName', 'personOrgId': 'Y2l...MGY', 'isModerator': False, 'isMonitor': False, 'created': '2022-05-10T22:16:27.361Z'}]}
devasc@labvm:~/labs/devnet-src/webex-teams$
```

## Часть 7: Управление сообщениями в Webex Teams
> В Webex Teams сообщение может содержать обычный текст, Markdown или вложение файла. Каждое сообщение отображается в отдельной строке вместе с меткой времени и информацией об отправителе. Вы можете использовать этот API Messages для списка, создания и удаления сообщений. В этой части вы отправите сообщение в комнату, которую вы создали в этой лабораторной работе.

### Шаг 1: Найдите и изучите документацию API для сообщений.
Вернитесь на веб-сайт developer.webex.com. В разделе Справочник API нажмите Сообщения.
Изучите различные вызовы API, которые можно выполнить с помощью API Messages.
Щелкните POST-запрос для Create a Message и изучите Query Parameters. Обратите внимание, что для простого текстового сообщения можно использовать параметр text или markdown. В этом шаге вы зададите сообщение с форматированием в формате Markdown. Поищите в Интернете, чтобы узнать больше о Markdown.

### Шаг 2: Используйте Python скрипт для отправки сообщения в комнату Webex.
В VS Code щелкните файл create-markdown-message.py.
Поместите в файл следующий код. Замените your_token_here на ваш персональный токен доступа. Замените your_room_id на значение, полученное в предыдущей части.
```python
import requests

access_token = 'your_token_here'
room_id = 'your_room_id'
message = 'Here in my garage, just bought this new Lamborghini here.'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
```
Сохраните и запустите файл. Вы должны получить ответ, похожий на следующий. Обратите внимание, что Markdown был преобразован в HTML. Значения идентификаторов были усечены.
```shell
devasc@labvm:~/labs/devnet-src/webex-teams$ python3 create-markdown-message.py 
{'id': 'Y2l...RjZg', 'roomId': 'Y2l...GNm', 'roomType': 'group', 'text': 'Here in my garage, just bought this new Lamborghini here.', 'personId': 'Y2l...NGE', 'personEmail': 'user@example.com', 'markdown': 'Here in my garage, just bought this new Lamborghini here.', 'html': '<p>Here in my garage, just bought this new Lamborghini here.</p>', 'created': '2022-05-10T22:27:41.505Z'}
devasc@labvm:~/labs/devnet-src/webex-teams$
```