# Использование RESTCONF для доступа к устройству IOS XE
## Цель лабораторной работы:
- Часть 1: Создание сети и проверка подключения
- Часть 2: Настройка устройства IOS XE для доступа к RESTCONF
- Часть 3: Запуск и настройка Postman
- Часть 4: Postman для отправки GET-запросов
- Часть 5: Postman для отправки PUT запроса
- Часть 6: Python скрипт для отправки GET-запросов
- Часть 7: Python скрипт для отправки PUT запроса

## Необходимые ресурсы:
- 1 ПК
- Virtual Box или VMWare
- DEVASC виртуальная машина
- CSR1kv виртуальная машина

## Порядок выполнения работы
## Часть 1: Запуск виртуальных машин и проверка подключения
> В этой части вы запустите две виртуальные машины и проверите подключение. Затем вы установите соединение безопасной оболочки (SSH).

### Шаг 1: Запуск виртуальных машин
Если вы еще не выполнили лабораторную работу - Установка лабораторной среды виртуальной машины и лабораторную работу Установка виртуальной машины CSR1kv, сделайте это сейчас. Запустите DEVASC и CSR1000v.

### Шаг 2: Проверьте соединение между виртуальными машинами.
На CSR1kv нажмите Enter, чтобы получить командную строку, а затем используйте show ip interface brief, чтобы проверить, что адрес IPv4 равен 192.168.56.101. Если адрес отличается, запишите его.
Откройте терминал в VS Code в DEVASC.
Выполните Ping CSR1kv для проверки соединения. Вы уже должны были сделать это ранее в лабораторных работах по установке. Если вы не можете выполнить пинг, вернитесь к лабораторным работам, перечисленным выше в части 1a.
```shell
devasc@labvm:~$ ping -c 5 192.168.56.101
PING 192.168.56.101 (192.168.56.101) 56(84) bytes of data.
64 bytes from 192.168.56.101: icmp_seq=1 ttl=254 time=1.37 ms
64 bytes from 192.168.56.101: icmp_seq=2 ttl=254 time=1.15 ms
64 bytes from 192.168.56.101: icmp_seq=3 ttl=254 time=0.981 ms
64 bytes from 192.168.56.101: icmp_seq=4 ttl=254 time=1.01 ms
64 bytes from 192.168.56.101: icmp_seq=5 ttl=254 time=1.14 ms

--- 192.168.56.101 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 0.981/1.130/1.365/0.135 ms
devasc@labvm:~$
```

### Шаг 3: Проверьте подключение SSH к CSR1kv.
В терминале DEVASC выполните SSH к виртуальной машине CSR1kv с помощью следующей команды:
```shell
devasc@labvm:~$ ssh  cisco@192.168.56.101
```

> Примечание: При первом SSH к CSR1kv ваша виртуальная машина DEVASC предупредит вас о подлинности CSR1kv. Поскольку вы доверяете CSR1kv, ответьте "да" на запрос.
```shell
The authenticity of host '192.168.56.101 (192.168.56.101)' can't be established.
RSA key fingerprint is SHA256:HYv9K5Biw7PFiXeoCDO/LTqs3EfZKBuJdiPo34VXDUY.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.56.101' (RSA) to the list of known hosts.
```
Введите `cisco123!` в качестве пароля, и теперь вы должны находиться в привилегированной командной строке EXEC для CSR1kv.
```shell
Password: <cisco123!>

CSR1kv#
```
Оставьте сеанс SSH открытым для следующей части.

## Часть 2: Настройка устройства IOS XE для доступа к RESTCONF
> В этой части вы настроите виртуальную машину CSR1kv на прием сообщений RESTCONF. Вы также запустите службу HTTPS.

> Примечание: Службы, обсуждаемые в этой части, могут быть уже запущены на вашей виртуальной машине. Однако убедитесь, что вы знаете команды для просмотра запущенных служб и их включения.

### Шаг 1: Убедитесь, что демоны RESTCONF запущены.
RESTCONF уже должен быть запущен. В терминале вы можете использовать команду show platform software yang-management process, чтобы увидеть, запущены ли все демоны, связанные со службой RESTCONF. Демон NETCONF также может быть запущен, но он не будет использоваться в этой лабораторной работе. Если один или несколько необходимых демонов не запущены, перейдите к шагу 2.
```shell
CSR1kv# show platform software yang-management process
confd            : Running 
nesd             : Running 
syncfd           : Running 
ncsshd           : Running 
dmiauthd         : Running 
nginx            : Running 
ndbmand          : Running 
pubd             : Running 

CSR1kv#
```

### Шаг 2: Включите и проверьте службу RESTCONF.
Введите команду глобальной конфигурации restconf, чтобы включить службу RESTCONF на CSR1kv.
```shell
CSR1kv#configure terminal
CSR1kv(config)# restconf
```
Убедитесь, что необходимые демоны RESTCONF запущены. Напомним, что ncsshd — это служба NETCONF, которая может быть запущена на вашем устройстве. Для этой лабораторной работы она нам не нужна. Однако вам нужен nginx, который является HTTPS-сервером. Это позволит выполнять вызовы REST API к службе RESTCONF.
```shell
CSR1kv(config)# exit
CSR1kv# show platform software yang-management process
confd            : Running
nesd             : Running
syncfd           : Running
ncsshd           : Not Running
dmiauthd         : Running
nginx            : Not Running
ndbmand          : Running
pubd             : Running
```

### Шаг 3: Включите и проверьте службу HTTPS.
Введите следующие команды глобальной конфигурации, чтобы включить сервер HTTPS и указать, что аутентификация сервера должна использовать локальную базу данных.
```shell
CSR1kv# configure terminal
CSR1kv(config)# ip http secure-server
CSR1kv(config)# ip http authentication local
```
Убедитесь, что сервер HTTPS (nginx) запущен.
```shell
CSR1kv(config)# exit
CSR1kv# show platform software yang-management process
confd            : Running
nesd             : Running
syncfd           : Running
ncsshd           : Not Running
dmiauthd         : Running
nginx            : Running
ndbmand          : Running
pubd             : Running
```

## Часть 3: Запуск и настройка Postman
> В этой части вы откроете Postman, отключите SSL-сертификаты и изучите пользовательский интерфейс.

### Шаг 1: Откройте Postman.
В виртуальной машине DEVASC откройте приложение Postman.

### Шаг 2: Отключите проверку сертификации SSL.
По умолчанию в Postman включена проверка SSL-сертификатов. Вы не будете использовать SSL сертификаты с CSR1kv, поэтому вам нужно отключить эту функцию.
Нажмите File > Settings.
На вкладке General в поле SSL certificate verification установите значение OFF.
Закройте диалоговое окно Settings.

## Часть 4: Postman для отправки GET-запросов
> В этой части вы будете использовать Postman для отправки GET запроса на CSR1kv, чтобы проверить, что вы можете подключиться к службе RESTCONF.

### Шаг 1: Изучите пользовательский интерфейс Postman.
В центре вы увидите Launchpad. При желании вы можете исследовать эту область.
Щелкните знак плюс (+) рядом с вкладкой Launchpad, чтобы открыть запрос GET Untitled Request. В этом интерфейсе вы будете выполнять всю свою работу в этой лаборатории.

### Шаг 2: Введите URL-адрес для CSR1kv.
Тип запроса уже установлен на GET. Оставьте тип запроса установленным на GET.
В поле "Enter request URL" введите URL, который будет использоваться для доступа к службе RESTCONF, запущенной на CSR1kv:
`https://192.168.56.101/restconf/`

### Шаг 3: Введите учетные данные для аутентификации.
Под полем URL находятся вкладки Params, Authorization, Headers, Body, Pre-request Script, Test и Settings. В этой лабораторной работе вы будете использовать авторизацию, заголовки и тело.
Перейдите на вкладку Authorization.
В разделе Type нажмите стрелку вниз рядом с "Inherit auth from parent" и выберите Basic Auth.
В поле Username и Password введите локальные учетные данные аутентификации для CSR1kv:
Имя пользователя: `cisco`
Пароль: `cisco123!`
Щелкните Headers. Затем щелкните 7 hidden. Вы можете проверить, что ключ авторизации имеет значение Basic, которое будет использоваться для аутентификации запроса, когда он будет отправлен на CSR1kv.

### Шаг 4: Установите JSON в качестве типа данных для отправки и получения от CSR1kv.
Вы можете отправлять и получать данные от CSR1kv в формате XML или JSON. Для этой лабораторной работы вы будете использовать JSON.
В области Headers щелкните в первом пустом поле Key и введите Content-Type для типа ключа. В поле Value введите application/yang-data+json. Это указывает Postman на отправку данных JSON на CSR1kv.
Ниже ключа Content-Type добавьте ещё одну пару ключ/значение. Поле Key будет Accept, а поле Value - application/yang-data+json.
> Примечание: При необходимости вы можете изменить application/yang-data+json на application/yang-data+xml для отправки и получения XML-данных вместо JSON-данных.

### Шаг 5: Отправьте запрос API на CSR1kv.
Теперь у Postman есть вся информация, необходимая для отправки GET-запроса. Нажмите кнопку Send. Ниже Temporary Headers вы должны увидеть следующий JSON-ответ от CSR1kv. Если нет, проверьте, что вы выполнили предыдущие шаги в этой части лабораторной работы и правильно настроили RESTCONF и службу HTTPS в части 2.
```json
{
    "ietf-restconf:restconf": {
        "data": {},
        "operations": {},
        "yang-library-version": "2016-06-21"
    }
}
```
Этот ответ JSON подтверждает, что Postman теперь может отправлять другие запросы REST API на CSR1kv.

### Шаг 6: Используйте запрос GET для сбора информации для всех интерфейсов на CSR1kv.
Теперь, когда у вас есть успешный GET-запрос, вы можете использовать его в качестве шаблона для дополнительных запросов. В верхней части Postman, рядом с вкладкой Launchpad, щелкните правой кнопкой мыши вкладку GET, которую вы только что использовали, и выберите Duplicate Tab.
Используйте YANG-модель ietf-interfaces для сбора информации об интерфейсах. Для URL добавьте data/ietf-interfaces:interfaces:
`https://192.168.56.101/restconf/data/ietf-interfaces:interfaces`
Нажмите кнопку Send. Вы должны увидеть ответ JSON от CSR1kv, похожий на показанный ниже. Вывод может отличаться в зависимости от конкретного маршрутизатора.
```json
{
  "ietf-interfaces:interfaces": {
    "interface": [
      {
        "name": "GigabitEthernet1",
        "description": "VBox",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": true,
        "ietf-ip:ipv4": {},
        "ietf-ip:ipv6": {}
      }
    ]
  }
}
```

### Шаг 7: Используйте запрос GET для сбора информации для определенного интерфейса на CSR1kv.
В этой лабораторной настроен только интерфейс GigabitEthernet1. Чтобы указать только этот интерфейс, расширьте URL, чтобы запрашивать информацию только для этого интерфейса.
Продублируйте последний запрос GET.
Добавьте параметр interface= для указания интерфейса и введите имя интерфейса.
`https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1`

> Примечание: Если вы запрашиваете информацию об интерфейсе с другого устройства Cisco с именами, использующими прямые косые черты, например GigabitEthernet0/0/1, используйте HTML-код %2F для прямых косых черт в имени интерфейса. Таким образом, 0/0/1 становится 0%2F0%2F1.

Нажмите кнопку Send. Вы должны увидеть ответ в формате JSON от CSR1kv, похожий на приведенный ниже. Вывод может отличаться в зависимости от вашего конкретного маршрутизатора. При настройке CSR1kv по умолчанию вы не увидите информацию об IP-адресации.
```json
{
  "ietf-interfaces:interface": {
    "name": "GigabitEthernet1",
    "description": "VBox",
    "type": "iana-if-type:ethernetCsmacd",
    "enabled": true,
    "ietf-ip:ipv4": {},
    "ietf-ip:ipv6": {}
  }
}
```
Этот интерфейс получает адресацию от шаблона Virtual Box. Поэтому IPv4-адрес не отображается в show running-config. Вместо этого вы увидите команду ip address dhcp. Вы можете увидеть это также в кратком выводе show ip interface.
```shell
CSR1kv# show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       192.168.56.101  YES DHCP   up                    up      
CSR1kv#
```
В следующей части вам нужно будет использовать ответ JSON от вручную настроенного интерфейса. Откройте командный терминал с CSR1kv и вручную настройте интерфейс GigabitEthernet1 с тем же адресом IPv4, который в настоящее время назначен ему Virtual Box.
```shell
CSR1kv# conf t
CSR1kv(config)# interface g1
CSR1kv(config-if)# ip address 192.168.56.101 255.255.255.0
CSR1kv(config-if)# end
CSR1kv# show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       192.168.56.101  YES manual up                    up      
CSR1kv#
```
Вернитесь в Postman и снова отправьте GET-запрос. Теперь вы должны увидеть информацию об адресации IPv4 в ответе JSON, как показано ниже. В следующей части вы скопируете этот формат JSON для создания нового интерфейса.
```shell
{
  "ietf-interfaces:interface": {
    "name": "GigabitEthernet1",
    "description": "VBox",
    "type": "iana-if-type:ethernetCsmacd",
    "enabled": true,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "192.168.56.101",
          "netmask": "255.255.255.0"
        }
      ]
    },
    "ietf-ip:ipv6": {}
  }
}
```

## Часть 5: Postman для отправки запроса PUT
> В этой части вы настроите Postman на отправку PUT запроса на CSR1kv для создания нового loopback интерфейса.

### Шаг 1: Повторите и измените последний GET-запрос.
Продублируйте последний GET-запрос.
Для параметра Type запроса нажмите стрелку вниз рядом с GET и выберите PUT.
Для параметра interface= измените его на =Loopback1, чтобы указать новый интерфейс.
`https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback1`

### Шаг 2: Настройте тело запроса, указав информацию для новой петли.
Чтобы отправить запрос PUT, необходимо предоставить информацию для тела запроса. Рядом с вкладкой Heders нажмите кнопку Body. Затем нажмите радиокнопку Raw. В настоящее время поле пустое. Если вы нажмете Send now, вы получите код ошибки 400 Bad Request, поскольку Loopback1 еще не существует, и вы не предоставили достаточно информации для создания интерфейса.
Заполните раздел Body необходимыми данными JSON для создания нового интерфейса Loopback1. Вы можете скопировать раздел Body предыдущего запроса GET и изменить его. Или вы можете скопировать следующее в раздел Body запроса PUT. Обратите внимание, что тип интерфейса должен быть установлен на softwareLoopback.
```json
{
  "ietf-interfaces:interface": {
    "name": "Loopback1",
    "description": "My first RESTCONF loopback",
    "type": "iana-if-type:softwareLoopback",
    "enabled": true,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "10.1.1.1",
          "netmask": "255.255.255.0"
        }
      ]
    },
    "ietf-ip:ipv6": {}
  }
}
```
Нажмите кнопку Send, чтобы отправить запрос PUT на CSR1kv. Ниже раздела Body вы должны увидеть код ответа HTTP Status: 201 Created. Это означает, что ресурс был создан успешно.
Вы можете убедиться, что интерфейс был создан. Вернитесь в сеанс SSH с CSR1kv и введите show ip interface brief. Вы также можете запустить вкладку Postman, содержащую запрос на получение информации об интерфейсах на CSR1kv, который был создан в предыдущей части этой лабораторной работы.
```shell
CSR1kv# show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       192.168.56.101  YES manual up                    up      
Loopback1              10.1.1.1        YES other  up                    up      
CSR1kv#
```

## Часть 6: Python скрипт для отправки GET-запросов
> В этой части вы создадите сценарий Python для отправки GET-запросов на CSR1kv.

### Шаг 1: Создайте каталог RESTCONF и запустите сценарий.
Откройте VS Code. Затем нажмите File > Open Folder... и перейдите в каталог devnet-src. Нажмите OK.
Откройте окно терминала в VS Code: Terminal > New Terminal.
Создайте подкаталог restconf в каталоге /devnet-src.
```shell
devasc@labvm:~/labs/devnet-src$ mkdir restconf
devasc@labvm:~/labs/devnet-src$
```
В панели EXPLORER в разделе DEVNET-SRC щелкните правой кнопкой мыши каталог restconf и выберите New File.
Назовите файл `restconf-get.py`.
Введите следующие команды, чтобы импортировать необходимые модули и отключить предупреждения о сертификатах SSL:
```python
import json
import requests
requests.packages.urllib3.disable_warnings()
```
Модуль json включает методы для преобразования данных JSON в объекты Python и наоборот. Модуль requests содержит методы, позволяющие отправлять REST-запросы на URL.

### Шаг 2: Создайте переменные, которые будут компонентами запроса.
Создайте переменную api_url и присвойте ей URL, по которому будет осуществляться доступ к информации об интерфейсе на CSR1kv.
```python
api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces"
```
Создайте словарь headers, содержащий ключи Accept и Content-type, и присвойте ключам значение application/yang-data+json.
```python
headers = {
    "Accept": "application/yang-data+json", 
    "Content-type":"application/yang-data+json"
}
```
Создайте кортежную переменную Python с именем basicauth, которая содержит два ключа, необходимых для аутентификации, имя пользователя и пароль.

### Шаг 3: Создайте переменную для отправки запроса и хранения ответа в формате JSON.
Используйте переменные, созданные на предыдущем шаге, в качестве параметров для метода requests.get(). Этот метод отправляет запрос HTTP GET к API RESTCONF на CSR1kv. Присвойте результат запроса переменной с именем resp. Эта переменная будет содержать JSON-ответ от API. Если запрос прошел успешно, JSON будет содержать возвращенную модель данных YANG.
Введите следующее утверждение:
```python
resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)
```
В таблице ниже перечислены различные элементы этого заявления:

|Элемент|Описание|
|:---:|:---:|
|`resp`|	Переменная для хранения ответа от API|
|`requests.get()`|	Метод, который фактически выполняет GET-запрос|
|`api_url`|	Переменная, в которой хранится строка адреса URL|
|`auth`|	Кортежная переменная, созданная для хранения информации об аутентификации|
|`headers=headers`|	Параметр, которому присваивается переменная headers|
|`verify=False`|	Отключает проверку SSL-сертификата при выполнении запроса|

Чтобы увидеть код ответа HTTP, добавьте `print()`.
```python
print(resp)
```
Сохраните и запустите свой скрипт. Вы должны получить результат, показанный ниже. Если нет, проверьте все предыдущие шаги в этой части, а также конфигурацию SSH и RESTCONF для CSR1kv.
```shell
devasc@labvm:~/labs/devnet-src$ cd restconf/
devasc@labvm:~/labs/devnet-src/restconf$ python3 restconf-get.py 
<Response [200]>
devasc@labvm:~/labs/devnet-src/restconf$
```

### Шаг 4: Форматирование и отображение данных JSON, полученных от CSR1kv.
Теперь вы можете извлечь значения ответа модели YANG из JSON ответа.
JSON ответа не совместим с объектами словаря и списка Python, поэтому его необходимо преобразовать в формат Python. Создайте новую переменную с именем response_json и присвойте ей переменную resp. Добавьте метод json() для преобразования JSON. Утверждение выглядит следующим образом:
```python
response_json = resp.json()
```
Добавьте print() для отображения данных JSON.
```python
print(response_json)
```
Сохраните и запустите свой сценарий. Вы должны получить результат, подобный следующему:
```shell
devasc@labvm:~/labs/devnet-src/restconf$ python3 restconf-get.py 
<Response [200]>
{'ietf-interfaces:interfaces': {'interface': [{'name': 'GigabitEthernet1', 'description': 'VBox', 'type': 'iana-if-type:ethernetCsmacd', 'enabled': True, 'ietf-ip:ipv4': {'address': [{'ip': '192.168.56.101', 'netmask': '255.255.255.0'}]}, 'ietf-ip:ipv6': {}}, {'name': 'Loopback1', 'description': 'My first RESTCONF loopback', 'type': 'iana-if-type:softwareLoopback', 'enabled': True, 'ietf-ip:ipv4': {'address': [{'ip': '10.1.1.1', 'netmask': '255.255.255.0'}]}, 'ietf-ip:ipv6': {}}]}}
devasc@labvm:~/labs/devnet-src/restconf$
```
Чтобы сделать вывод более красивым, измените оператор print, чтобы использовать функцию json.dumps() с параметром "indent":
```python
print(json.dumps(response_json, indent=4))
```
Сохраните и запустите свой скрипт. Вы должны получить результат, показанный ниже. Этот результат практически идентичен результату вашего первого GET-запроса Postman.
```shell
devasc@labvm:~/labs/devnet-src/restconf$ python3 restconf-get.py 
<Response [200]>
{
    "ietf-interfaces:interfaces": {
        "interface": [
            {
                "name": "GigabitEthernet1",
                "description": "VBox",
                "type": "iana-if-type:ethernetCsmacd",
                "enabled": true,
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": "192.168.56.101",
                            "netmask": "255.255.255.0"
                        }
                    ]
                },
                "ietf-ip:ipv6": {}
            },
            {
                "name": "Loopback1",
                "description": "My first RESTCONF loopback",
                "type": "iana-if-type:softwareLoopback",
                "enabled": true,
                "ietf-ip:ipv4": {
                    "address": [
                        {
                            "ip": "10.1.1.1",
                            "netmask": "255.255.255.0"
                        }
                    ]
                },
                "ietf-ip:ipv6": {}
            }
        ]
    }
}
devasc@labvm:~/labs/devnet-src/restconf$
```

## Часть 7: Python скрипт для отправки запроса PUT
> В этой части вы создадите Python скрипт для отправки запроса PUT на CSR1kv. Как и в Postman, вы создадите новый loopback интерфейс.

### Шаг 1: Импортируйте модули и отключите предупреждения SSL.
На панели EXPLORER в разделе DEVNET-SRC щелкните правой кнопкой мыши каталог restconf и выберите New File.
Назовите файл `restconf-put.py`.
Введите следующие команды, чтобы импортировать необходимые модули и отключить предупреждения о сертификатах SSL:
```python
import json
import requests
requests.packages.urllib3.disable_warnings()
```

### Шаг 2: Создайте переменные, которые будут компонентами запроса.
Создайте переменную api_url и присвойте ей URL, нацеленный на новый интерфейс Loopback2.

> Примечание: Эта спецификация переменной должна находиться на одной строке в вашем сценарии.

```python
api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback2"
```
Создайте словарную переменную headers, содержащую ключи Accept и Content-type, и присвойте ключам значение application/yang-data+json.
```python
headers = { 
    "Accept": "application/yang-data+json", 
    "Content-type":"application/yang-data+json"
}
```
Создайте кортежную переменную Python с именем basicauth, которая содержит два значения, необходимые для аутентификации, - имя пользователя и пароль.
```python
basicauth = ("cisco", "cisco123!")
```
Создайте в Python словарную переменную yangConfig, которая будет содержать данные YANG, необходимые для создания нового интерфейса Loopback2. Вы можете использовать тот же словарь, который ранее использовали в Postman. Однако измените номер и адрес интерфейса. Также помните, что в Python булевы значения должны быть написаны с заглавной буквы. Поэтому убедитесь, что в паре ключ/значение для "enabled" буква T написана с заглавной буквы: True.
```python
yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback2",
        "description": "My second RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.2.1.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}
```

### Шаг 3: Создайте переменную для отправки запроса и хранения ответа в формате JSON.
Используйте переменные, созданные на предыдущем шаге, в качестве параметров метода requests.put(). Этот метод отправляет запрос HTTP PUT в API RESTCONF. Присвойте результат запроса переменной с именем resp. Эта переменная будет содержать JSON-ответ от API. Если запрос прошел успешно, JSON будет содержать возвращенную модель данных YANG.
Прежде чем вводить утверждения, обратите внимание, что эта спецификация переменной должна находиться только в одной строке вашего сценария. Введите следующие утверждения:

> Примечание: Эта спецификация переменной должна находиться на одной строке в вашем сценарии.

```python
resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)
```

Введите приведенный ниже код для обработки ответа. Если ответ является одним из сообщений об успехе HTTP, будет выведено первое сообщение. Любое другое значение кода считается ошибкой. В случае обнаружения ошибки будет выведен код ответа и сообщение об ошибке.
```python
if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))
```
В таблице ниже перечислены различные элементы этих заявлений:

|Элемент|	Описание|
|:---:|:---:|
|`resp`|	Переменная для хранения ответа от API|
|`requests.put()`|	Метод, который фактически выполняет PUT-запрос|
|`api_url`|	Переменная, в которой хранится строка адреса URL|
|`data`|	Данные для отправки в конечную точку API, которые форматируются как JSON.|
|`auth`|	Переменная кортежа, созданная для хранения информации об аутентификации.|
|`headers=headers`|	Параметр, которому присваивается переменная headers.|
|`verify=False`|	Параметр, отключающий проверку SSL-сертификата при выполнении запроса.|
|`resp.status_code`|	Код состояния HTTP в ответе на запрос API PUT.|

Сохраните и запустите сценарий для отправки запроса PUT на CSR1kv. Вы должны получить сообщение 201 Status Created. Если нет, проверьте свой код и конфигурацию CSR1kv.
Вы можете проверить, что интерфейс был создан, введя show ip interface brief на CSR1kv.
```shell
CSR1kv# show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       192.168.56.101  YES manual up                    up      
Loopback1              10.1.1.1        YES other  up                    up      
Loopback2              10.2.1.1        YES other  up                    up      
CSR1kv#
```
Программы, используемые в данной лабораторной
В этой лабое использовались следующие программы Python:
```python
#===================================================================
#resconf-get.py
import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces"

headers = { 
            "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
          }

basicauth = ("cisco", "cisco123!")

resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)

print(resp)

response_json = resp.json()
print(json.dumps(response_json, indent=4))

#end of file

#===================================================================
#resconf-put.py
import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback2"

headers = {
            "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
          }

basicauth = ("cisco", "cisco123!")

yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback2",
        "description": "My second RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "10.2.1.1",
                    "netmask": "255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

resp = requests.put(api_url, data=json.dumps(yangConfig), auth=basicauth, headers=headers, verify=False)

if(resp.status_code >= 200 and resp.status_code <= 299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Status Code: {} \nError message: {}'.format(resp.status_code,resp.json()))
```