# Сравнение CLI и SDN контроллера 
## Цель лабораторной работы:
- Часть 1: Запуск виртуальной машины DEVASC
- Часть 2: Проверка внешнего подключения к Packet Tracer
- Часть 3: Запрос маркера аутентификации с помощью Postman
- Часть 4: Отправка REST-запросов с помощью Postman
- Часть 5: Отправка REST-запросов с помощью VS Code
- Часть 6: Отправка REST-запросов внутри Packet Tracer

## Необходимые ресурсы:
- 1 ПК
- Virtual Box или VMWare
- DEVASC виртуальная машина

## Таблица адресации
|Устройство|Интерфейс|IP Адрес|
|:---:|:---:|:---:|
|R1	|G0/0/0	|192.168.101.1|
|^^ |S0/1/0	|192.168.1.2|
|R2	|G0/0/0	|192.168.101.2|
|^^ |S0/1/1	|192.168.2.2|
|R3	|G0/0/0	|10.0.1.1|
|^^ |G0/0/1	|10.0.2.1|
|^^ |S0/1/0	|192.168.1.1|
|^^ |S0/1/1	|192.168.2.1|
|SWL1	|VLAN 1	|192.168.101.2|
|SWL2	|VLAN 1	|192.168.102.2|
|SWR1	|VLAN 1	|10.0.1.2|
|SWR2	|VLAN 1	|10.0.1.3|
|SWR3	|VLAN 1	|10.0.1.4|
|SWR4	|VLAN 1	|10.0.1.5|
|Admin	|NIC	|10.0.1.129|
|PC1	|NIC	|10.0.1.130|
|PC2	|NIC	|10.0.2.129|
|PC3	|NIC	|10.0.2.130|
|PC4	|NIC	|192.168.102.3|
|Example Server	|NIC	|192.168.101.100|
|PT-Controlle	|NIC	|192.168.101.254|

## Порядок выполнения работы
## Часть 1: Запуск виртуальной машины DEVASC
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, серьёзно… на последней лабе. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.

## Часть 2: Проверка внешнего подключения к Packet Tracer
> В этой части вы проверите, что Packet Tracer может быть доступен другим приложениям на виртуальной машине DEVASC. Это задание должно быть выполнено полностью в среде виртуальной машины DEVASC.

#### Шаг 1: Если вы ещё не сделали этого, откройте программу Packet Tracer.
В виртуальной машине DEVASC VM откройте учебную программу своего курса в браузере Chromium.
Перейдите на страницу этого задания.
Загрузите и запустите файл Packet Tracer - Implement REST APIs with an SDN Controller.pka, связанный с этими инструкциями.

### Шаг 2: Проверьте настройки Packet Tracer для внешнего доступа.
Нажмите **Options > Preferences > Miscellaneous**. Убедитесь, что в разделе External Access, установлен флажок Enable External Access for Network Controller REST API.

Закройте окно Preferences.
Нажмите **PT-Controller0 > Config**.
Слева в разделе REAL WORLD нажмите Controller.
Установите флажок Access Enabled и обратите внимание на номер порта, который, скорее всего, равен 58000. Это номер порта, который вам понадобится при внешнем доступе к трассировщику пакетов из Chromium, VS Code, и Postman позже в этой работе.

### Шаг 3: Убедитесь, что вы можете получить доступ к Packet Tracer из другой программы на виртуальной машине DEVASC.
Откройте Chromium и перейдите на страницу `http://localhost:58000/api/v1/host`.
Вы получите следующий ответ. Этот шаг проверяет, что вы можете получить внешний доступ к Packet Tracer и PTController0. Обратите внимание, что для авторизации требуется токен. Вы получите его в следующей части.

```json
{
    "response": {
        "detail": "Security Authentication Failure",
        "errorCode": "REST_API_EXTERNAL_ACCESS",
        "message": "Ticket-based authorization: empty ticket."
    },
    "version": "1.0"
}
```

## Часть 3: Запрос маркера аутентификации с помощью Postman
> В этой части вы изучите документацию REST API в Packet Tracer и воспользуетесь Postman для запроса токена аутентификации от PT-Controller0. Вы также можете сделать это в VS Code с помощью Python скрипта.

### Шаг 1: Изучите документацию REST API для сетевого контроллера.
Чтобы просмотреть документацию REST API для PT-Controller0, выполните следующие действия:
Нажмите **Admin > Desktop > Web Browser**.
Введите `192.168.101.254`.
Войдите на **PT-Controller0** под пользователем `cisco` и паролем `cisco123!`
Нажмите на меню и выберите API Docs.

Вы также можете получить доступ к этой же документации из меню Help. (Help > Contents).
В навигационной панели слева прокрутите вниз примерно две трети и выберите Network Controller API. Здесь представлена та же документация, что и для PT-Controller0.
В документации API щелкните addTicket. Вы будете использовать эту документацию в следующем шаге.

> Примечание: Некоторые функции REST API могут быть недоступны в текущей версии Packet Tracer.

### Шаг 2: Создайте новый POST-запрос.
Изучив документацию по методу **addTicket REST API Method**, откройте Postman. В области запуска нажмите на знак плюс, чтобы создать новый Untitled Request.
Нажмите стрелку вниз и измените тип с GET на POST.
Введите URL `http://localhost:58000/api/v1/ticket`.
Ниже поля URL нажмите кнопку Тело. Измените тип на raw.
Нажмите стрелку вниз рядом с Text и измените его на JSON. Это изменение также установит HTTP-заголовок "Content-type" на "application/json", который требуется для этого вызова API.
Вставьте следующий объект JSON в поле Body. Убедитесь, что ваш код правильно отформатирован

```json
{
    "username": "cisco",
    "password": "cisco123!"
}
```

### Шаг 3: Отправьте POST-запрос
Нажмите кнопку **Send**, чтобы отправить POST-запрос на **PT-Controller0**
Вы должны получить ответ, похожий на следующий. Однако `ваш_serviceTicket` будет фактическим значением.

```json
{
    "response": {
        "idleTimeout": 900,
        "serviceTicket": "ваш_serviceTicket",
        "sessionTimeout": 3600
    },
    "version": "1.0"
}
```
Скопируйте значение serviceTicket без кавычек в текстовый файл для последующего использования.

## Часть 4: Отправка REST-запросов с помощью Postman
> В этой части вы будете использовать свой служебный билет для отправки трех REST-запросов на PT-Controller0.

### Шаг 1: Создайте новый GET-запрос для всех сетевых устройств в сети.
В Postman нажмите на знак плюс, чтобы создать новый **Untitled Request**.
Введите URL `http://localhost:58000/api/v1/network-device`.
Ниже поля URL нажмите Headers.
Под последним KEY щелкните поле Key и введите X-Auth-Token.
В поле Value введите значение ваш_serviceTicket.

### Шаг 2: Отправьте GET-запрос.
Нажмите кнопку **Send**, чтобы отправить GET-запрос на **PT-Controller0**.
Вы должны получить ответ со списком данных, которые контроллер имеет для девяти сетевых устройств в сети. Ответ для первого устройства показан здесь.

```json
{
    "response": [
        {
            "collectionStatus": "Managed",
            "connectedInterfaceName": [
                "GigabitEthernet0/0/0",
                "GigabitEthernet0",
                "FastEthernet0"
            ],
            "connectedNetworkDeviceIpAddress": [
                "192.168.101.1",
                "192.168.101.254",
                "192.168.101.100"
            ],
            "connectedNetworkDeviceName": [
                "R1",
                "NetworkController",
                "Example Server"
            ],
            "errorDescription": "",
            "globalCredentialId": "53046ecc-88c3-49f6-9626-ca8ab9db6725",
            "hostname": "SWL1",
            "id": "CAT1010BT47-uuid",
            "interfaceCount": "29",
            "inventoryStatusDetail": "Managed",
            "lastUpdateTime": "6",
            "lastUpdated": "2020-06-11 19:07:29",
            "macAddress": "000C.CF42.2B11",
            "managementIpAddress": "192.168.101.2",
            "platformId": "3650",
            "productId": "3650-24PS",
            "reachabilityFailureReason": "",
            "reachabilityStatus": "Reachable",
            "serialNumber": "CAT1010BT47-",
            "softwareVersion": "16.3.2",
            "type": "MultiLayerSwitch",
            "upTime": "1 hours, 6 minutes, 49 seconds"
        },
<вывод опущен>
    ],
    "version": "1.0"
}
```

### Шаг 3: Дублируйте GET-запрос и измените его для всех хостов в сети.
В Postman щелкните правой кнопкой мыши вкладку GET-запроса хоста и выберите Duplicate Tab.
Вся информация в тикете будет одинаковой, за исключением URL. Просто измените network-device на host:`http://localhost:58000/api/v1/host`.

### Шаг 4: Отправьте GET-запрос.
Нажмите кнопку **Send**, чтобы отправить запрос GET на PT-Controller0.
Вы должны получить ответ со списком данных, которые контроллер имеет для шести хост-устройств в сети.
Ответ для первого устройства показан здесь.

```json
{
    "response": [
        {
              "connectedAPMacAddress": "",
              "connectedAPName": "",
              "connectedInterfaceName": "GigabitEthernet1/0/24",
              "connectedNetworkDeviceIpAddress": "192.168.102.2",
              "connectedNetworkDeviceName": "SWL2",
              "hostIp": "192.168.102.3",
              "hostMac": "00E0.F96C.155B",
              "hostName": "PC4",
              "hostType": "Pc",
              "id": "PTT08108MO8-uuid",
              "lastUpdated": "2020-06-11 13:00:56",
              "pingStatus": "SUCCESS"
        },
<вывод опущен>
    ],
    "version": "1.0"
}
```

### Шаг 5: Закройте Postman, чтобы освободить память в виртуальной машине DEVASC.

## Часть 5: Отправка REST-запросов с помощью VS Code
> В этой части вы будете использовать сценарий Python в VS Code для отправки тех же запросов API, которые вы отправляли в Postman.
> Однако вы также будете использовать циклы Python for для разбора JSON и отображения только определенных пар ключ-значение.

### Шаг 1: Используйте скрипт для запроса заявки на обслуживание.
Откройте VS Code.
Нажмите **File > Open Folder...** и перейдите в каталог **devnet-src/ptna**.
Нажмите OK.
Обратите внимание, что в панели EXPLORE слева отображаются три скрипта: `01_get-ticket.py`, `02_get-networkdevice.py` и `03_get-host.py`. Просмотрите код каждого из них. Обратите внимание, что программы для сетевых устройств и хостов требуют, чтобы вы заменили значение ваш_serviceTicket на значение, которое Packet Tracer дал вам, когда вы сделали его запрос. Запросите новый тикет на обслуживание, чтобы увидеть работу скрипта 01_get-ticket.py.
```shell
devasc@labvm:~/labs/devnet-src/ptna$ python3 01_get-ticket.py 
Ticket request status: 201
The service ticket number is: your_serviceTicket
devasc@labvm:~/labs/devnet-src/ptna$
```
Замените значение `your_serviceTicket` в файлах `02_get-network-device.py` и `03_get-host.py` на значение которое дал вам Packet Tracer.

### Шаг 2: Используйте сценарий для запроса списка сетевых устройств.
Ранее в Postman вызов API сетевого устройства возвращал список всех девяти сетевых устройств и всю информацию, доступную для каждого устройства. Однако скрипт 02_get-network-device.py печатает только значения ключей, которые интересуют программиста: имя хоста, platformId и managementIpAddress.
В окне терминала запустите сценарий `02_get-network-device.py`.

```shell
devasc@labvm:~/labs/devnet-src/ptna$ python3 02_get-network-device.py
Request status: 200
SWL1 3650 192.168.101.2
R1 ISR4300 192.168.1.2
R3 ISR4300 192.168.2.1
SWR1 3650 10.0.1.2
SWR2 3650 10.0.1.3
R2 ISR4300 192.168.2.2
SWL2 3650 192.168.102.2
SWR4 3650 10.0.1.5
SWR3 3650 10.0.1.4
devasc@labvm:~/labs/devnet-src/ptna$
```

### Шаг 3: Используйте сценарий для запроса списка хост-устройств.
Аналогично, разработчик решил перечислить конкретную информацию для каждого из шести хост-устройств, подключенных к сети.
В окне терминала запустите скрипт `03_get-host.py`.
```shell
devasc@labvm:~/labs/devnet-src/ptna$ python3 03_get-host.py
Request status: 200
PC4 192.168.102.3 00E0.F96C.155B GigabitEthernet1/0/24
PC3 10.0.2.129 0004.9A42.C245 GigabitEthernet1/0/24
PC1 10.0.1.129 00E0.A330.3359 GigabitEthernet1/0/22
PC2 10.0.2.130 0060.47C1.A4DB GigabitEthernet1/0/23
Admin 10.0.1.130 0050.0FCE.B095 GigabitEthernet1/0/21
Example Server 192.168.101.100 000A.413D.D793 GigabitEthernet1/0/3
devasc@labvm:~/labs/devnet-src/ptna$
```

## Часть 6: Отправка REST-запросов внутри Packet Tracer
> В этой части вы будете использовать те же сценарии с одной небольшой правкой для отправки тех же API-запросов внутри Packet Tracer, которые вы отправляли из VS Code.

### Шаг 1: Создание проекта в Packet Tracer
В программе Packet Tracer щелкните Admin PC.
Перейдите на вкладку Programming.
В настоящее время проекта нет. Нажмите кнопку New.
Введите REST APIs в качестве имени и выберите Empty - Python в качестве шаблона.
Нажмите кнопку Create.
Теперь проект REST APIs (Python) создан с пустым сценарием main.py.

### Шаг 2: Измените скрипт для запуска внутри Packet Tracer.
Доступ от одного приложения к другому на одной и той же хост-машине требует, чтобы номер порта был указан в URL-адресе. Однако Packet Tracer имитирует реальную сеть. В реальном мире вы обычно не указывать номер порта при выполнении запросов API. Кроме того, вы будете использовать доменное имя или IP-адрес в URL.
В VS Code скопируйте код для файла 03_get-host.py
На вкладке **Admin > Programming** дважды щелкните по `main.py`, чтобы открыть его.
Вставьте код в скрипт main.py.
Измените `api_url`. Замените `localhost:58000/api/v1/host` на `192.168.101.254/api/v1/host`.
Изменения автоматически сохраняются. Нажмите кнопку Выполнить. Вывод Packet Tracer не совсем точно имитирует то, что вы видите в командной строке Linux. Однако вы должны увидеть похожие результаты, как показано ниже
```shell
Starting REST APIs (Python)...
('Request status: ', 200)
('PC4', '\t', '192.168.102.3', '\t', '00E0.F96C.155B', '\t', 'GigabitEthernet1/0/24')
('PC3', '\t', '10.0.2.129', '\t', '0004.9A42.C245', '\t', 'GigabitEthernet1/0/24')
('PC1', '\t', '10.0.1.129', '\t', '00E0.A330.3359', '\t', 'GigabitEthernet1/0/22')
('PC2', '\t', '10.0.2.130', '\t', '0060.47C1.A4DB', '\t', 'GigabitEthernet1/0/23')
('Admin', '\t', '10.0.1.130', '\t', '0050.0FCE.B095', '\t', 'GigabitEthernet1/0/21')
('Example Server', '\t', '192.168.101.100', '\t', '000A.413D.D793', '\t', 'GigabitEthernet1/0/3')
REST APIs (Python) finished running.
```
Скопируйте и вставьте `02_get-network-device.py` в файл `main.py`. Измените URL и запустите его.
```shell
REST APIs (Python) finished running.
Starting REST APIs (Python)...
('Request status: ', 200)
('SWL1', '\t', '3650', '\t', '192.168.101.2')
('R1', '\t', 'ISR4300', '\t', '192.168.1.2')
('R3', '\t', 'ISR4300', '\t', '192.168.2.1')
('SWR1', '\t', '3650', '\t', '10.0.1.2')
('SWR2', '\t', '3650', '\t', '10.0.1.3')
('R2', '\t', 'ISR4300', '\t', '192.168.2.2')
('SWL2', '\t', '3650', '\t', '192.168.102.2')
('SWR4', '\t', '3650', '\t', '10.0.1.5')
('SWR3', '\t', '3650', '\t', '10.0.1.4')
REST APIs (Python) finished running
```