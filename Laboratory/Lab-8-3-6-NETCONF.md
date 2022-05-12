# Использование NETCONF для доступа к устройству IOS XE
## Цель лабораторной работы:
- Часть 1: Создание сети и проверка подключения
- Часть 2: Использование сеанса NETCONF для сбора информации
- Часть 3: Использование ncclient для подключения к NETCONF
- Часть 4: Использование ncclient для получения конфигурации
- Часть 5: Использование ncclient для настройки устройства
- Часть 6: Задача: Модификация программы, использованной в этой лабораторной работе

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

## Часть 2: Использование сеанса NETCONF для сбора информации
> В этой части вы убедитесь, что NETCONF запущен, включите NETCONF, если он не запущен, и убедитесь, что NETCONF готов к SSH соединению. Затем вы подключитесь к процессу NETCONF, запустите сеанс NETCONF, соберете информацию об интерфейсе и закроете сеанс.

### Шаг 1: Проверьте, запущен ли NETCONF на CSR1kv.
В сеансе SSH с CSR1kv используйте команду `show platform software yang-management process`, чтобы проверить, запущен ли демон NETCONF SSH (ncsshd).
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
Если NETCONF не запущен, как показано в выводе выше, введите команду глобальной конфигурации netconf-yang.
```shell
CSR1kv# config t
CSR1kv (config)# netconf-yang
```
Введите exit, чтобы закрыть сеанс SSH.

### Шаг 2: Получите доступ к процессу NETCONF через терминал SSH.
На этом шаге вы восстановите SSH-сессию с CSR1kv. Но на этот раз вы укажете порт NETCONF 830 и отправите netconf как команду подсистемы.
Примечание: Для получения дополнительной информации об этих опциях изучите страницы руководства по SSH (man ssh).
Введите следующую команду в окне терминала. Вы можете использовать стрелку вверх, чтобы вызвать последнюю команду SSH и просто добавить параметры -p и -s, как показано на рисунке. Затем введите cisco123! в качестве пароля.
```shell
devasc@labvm:~$ ssh cisco@192.168.56.101 -p 830 -s netconf
cisco@192.168.56.101's password: 
```
CSR1kv ответит сообщением hello, содержащим более 400 строк с перечислением всех своих возможностей NETCONF. Конец сообщений NETCONF обозначается `]]>]]>`.
```xml
<?xml version="1.0" encoding="UTF-8"?>
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
<capabilities>
<capability>urn:ietf:params:netconf:base:1.0</capability>
<capability>urn:ietf:params:netconf:base:1.1</capability>
<capability>urn:ietf:params:netconf:capability:writable-running:1.0</capability>
<capability>urn:ietf:params:netconf:capability:xpath:1.0</capability>
<capability>urn:ietf:params:netconf:capability:validate:1.0</capability>
<capability>urn:ietf:params:netconf:capability:validate:1.1</capability>
(вывод опущен)
      </capability>
</capabilities>
<session-id>20</session-id></hello>]]>]]>
```

### Шаг 3: Запустите сеанс NETCONF, отправив сообщение hello с клиента.
Чтобы начать сеанс NETCONF, клиент должен отправить свое собственное сообщение hello. Сообщение hello должно включать версию базовых возможностей NETCONF, которую клиент хочет использовать.
Скопируйте и вставьте следующий XML-код в сеанс SSH. Обратите внимание, что конец сообщения приветствия клиента обозначен символом ]]>]]>.
```xml
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
 <capabilities>
   <capability>urn:ietf:params:netconf:base:1.0</capability>
 </capabilities>
</hello>
]]>]]>
```
Переключитесь на ВМ CSR1kv и используйте команду show netconf-yang sessions, чтобы убедиться, что сеанс NETCONF был запущен. Если экран ВМ CSR1kv темный, нажмите Enter, чтобы разбудить его.
```shell
CSR1kv> en
CSRk1v# show netconf-yang sessions
R: Global-lock on running datastore
C: Global-lock on candidate datastore
S: Global-lock on startup datastore

Number of sessions : 1

session-id  transport    username             source-host           global-lock
-------------------------------------------------------------------------------
20          netconf-ssh  cisco                192.168.56.1          None

CSR1kv# 
```

### Шаг 4: Отправьте сообщения RPC на устройство IOS XE.
Во время сеанса SSH клиент NETCONF может использовать сообщения Remote Procedure Call (RPC) для отправки операций NETCONF на устройство IOS XE. В таблице перечислены некоторые из наиболее распространенных операций NETCONF.

|Операция|Описание|
|:------:|:------:|
|`<get>`	|Получение информации о текущей конфигурации и состоянии устройства|
|`<get-config>`	|Извлечение всего или части указанного хранилища данных конфигурации|
|`<edit-config>`	|Загружает всю или часть конфигурации в указанное хранилище данных конфигурации|
|`<copy-config>`	|Замена всего хранилища данных конфигурации на другое|
|`<delete-config>`	|Удаление хранилища данных конфигурации|
|`<commit>`	|Копирование хранилища данных кандидата в действующее хранилище данных|
|`<lock>` / `<unlock>`	|Блокировка или разблокировка всей системы хранения данных конфигурации|
|`<close-session>`	|Graceful завершение сессии NETCONF|
|`<kill-session>`	|Принудительное завершение сеанса NETCONF|

Скопируйте и вставьте следующий XML-код RPC get message в терминальный сеанс SSH для получения информации об интерфейсах на R1.
```xml
<rpc message-id="103" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
 <get>
  <filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
   </filter>
 </get>
</rpc>
]]>]]>
```
Напомним, что XML не требует отступов или пробелов. Поэтому CSR1kv вернет длинную строку данных XML.
```xml
<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="103"><data><interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"><interface><name>GigabitEthernet1</name><description>VBox</description><type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type><enabled>true</enabled><ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"></ipv4><ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"></ipv6></interface></interfaces></data></rpc-reply>]]>]]>
```
Скопируйте XML, который был возвращен, но не включайте заключительные символы "]]>]]>". Эти символы не являются частью XML, возвращаемого маршрутизатором.
Найдите в Интернете запрос "prettify XML". Найдите подходящий сайт и используйте его инструмент для преобразования вашего XML в более читабельный формат, например, следующий:
```xml
<?xml version="1.0"?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="103">
  <data>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
        <name>GigabitEthernet1</name>
        <description>VBox</description>
        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
        <enabled>true</enabled>
        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
        <ipv6 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip"/>
      </interface>
    </interfaces>
  </data>
</rpc-reply>
```

### Шаг 5: Закройте сеанс NETCONF.
Чтобы закрыть сессию NETCONF, клиент должен отправить следующее сообщение RPC:
```xml
<rpc message-id="9999999" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
 <close-session />
</rpc>
```
Через несколько секунд вы вернетесь к приглашению терминала. Вернитесь к приглашению CSR1kv и покажите открытые сессии netconf. Вы увидите, что сессия была закрыта.
```shell
CSR1kv# show netconf-yang sessions
There are no active sessions

CSR1kv#
```

## Часть 3: Использование ncclient для подключения к NETCONF
> Работа с NETCONF не требует работы с необработанными сообщениями NETCONF RPC и XML. В этой части вы узнаете, как использовать модуль ncclient Python для простого взаимодействия с сетевыми устройствами с помощью NETCONF. Кроме того, вы узнаете, как определить, какие модели YANG поддерживаются устройством. Эта информация будет полезна при создании производственной системы автоматизации сети, которая требует, чтобы конкретные модели YANG поддерживались данным сетевым устройством.

### Шаг 1: Убедитесь, что ncclient установлен и готов к работе.
В терминале DEVASC-VM введите команду `pip3 list --format=columns`, чтобы увидеть все установленные в настоящее время модули Python. Отправьте вывод в more. Ваш вывод может отличаться от приведенного ниже. Но вы должны увидеть ncclient в списке, как показано на рисунке. Если это не так, используйте команду pip3 install ncclient для его установки.
```shell
devasc@labvm:~$ pip3 list --format=columns | more
Package                Version    
---------------------- -----------
ansible                2.9.6      
apache-libcloud        2.8.0      
appdirs                1.4.3      
argcomplete            1.8.1      
astroid                2.3.3      
(вывод опущен)
ncclient               0.6.7      
netaddr                0.7.19     
netifaces              0.10.4     
netmiko                3.1.0      
ntlm-auth              1.1.0      
oauthlib               3.1.0
(вывод опущен)
xmltodict              0.12.0     
zipp                   1.0.0      
devasc@labvm:~$
```

### Шаг 2: Создайте сценарий для использования ncclient для подключения к службе NETCONF.
В VS Code, нажмите File > Open Folder... и перейдите в каталог devnet-src. Нажмите OK.
Откройте окно терминала в VS Code: Terminal > New Terminal.
Создайте подкаталог netconf в каталоге /devnet-src
```shell
devasc@labvm:~/labs/devnet-src$ mkdir netconf
devasc@labvm:~/labs/devnet-src$
```
На панели EXPLORER в разделе DEVNET-SRC щелкните правой кнопкой мыши каталог netconf и выберите New File.
Назовите файл `ncclient-netconf.py`.
В файле сценария импортируйте класс manager из модуля ncclient. Затем создайте переменную m для представления метода connect(). Метод connect() включает всю информацию, необходимую для подключения к службе NETCONF, запущенной на CSR1kv. Обратите внимание, что для NETCONF используется порт 830.
```python
from ncclient import manager

m = manager.connect(
        host="192.168.56.101",
        port=830,
        username="cisco",
        password="cisco123!",
        hostkey_verify=False
    )
```
Если параметр hostkey_verify установлен в True, CSR1kv попросит вас проверить отпечаток SSH. В лабораторных условиях безопасно установить это значение в False, как мы и сделали здесь.
Сохраните и запустите программу, чтобы убедиться в отсутствии ошибок. Пока вы не увидите никакого вывода.
```shell
devasc@labvm:~/labs/devnet-src$ cd netconf/
devasc@labvm:~/labs/devnet-src/netconf$ python3 ncclient-netconf.py 
devasc@labvm:~/labs/devnet-src/netconf$
```
Вы можете проверить, что CSR1kv принял запрос на сеанс NETCONF. Должно появиться сообщение syslog %DMI-5-AUTH_PASSED в ВМ CSR1kv. Если экран черный, нажмите Enter, чтобы разбудить маршрутизатор. Сообщение syslog можно увидеть над баннером.

### Шаг 3: Добавьте функцию печати в сценарий, чтобы перечислить возможности NETCONF для CSR1kv.
Объект m, возвращаемый функцией manager.connect(), представляет собой удаленную сессию NETCONF. Как вы видели ранее, в каждой сессии NETCONF сервер сначала отправляет свои возможности, которые представляют собой список поддерживаемых моделей YANG в формате XML. В модуле ncclient полученный список возможностей хранится в списке m.server_capabilities.
Используйте цикл for и функцию print для отображения возможностей устройства:
```python
print("#Поддерживаемые возможности (YANG модели):")
for capability in m.server_capabilities:
    print(capability) 
```
Сохраните и запустите программу. На выходе вы получите тот же результат, что и при отправке сложного сообщения hello, но без открывающего и закрывающего XML-тега <capability> в каждой строке.
```shell
devasc@labvm:~/labs/devnet-src/netconf$ python3 ncclient-netconf.py 
#Поддерживаемые возможности (YANG модели):
urn:ietf:params:netconf:base:1.0
urn:ietf:params:netconf:base:1.1
urn:ietf:params:netconf:capability:writable-running:1.0
urn:ietf:params:netconf:capability:xpath:1.0
<вывод опущен>
urn:ietf:params:xml:ns:netconf:base:1.0?module=ietf-netconf&revision=2011-06-01
urn:ietf:params:xml:ns:yang:ietf-netconf-with-defaults?module=ietf-netconf-with-defaults&revision=2011-06-01

        urn:ietf:params:netconf:capability:notification:1.1
      
devasc@labvm:~/labs/devnet-src/netconf$
```

## Часть 4: Использование ncclient для получения конфигурации
> В этой части вы будете использовать NETCONF ncclient для получения конфигурации для CSR1kv, использовать модуль xml.dom.minidom для форматирования конфигурации и использовать фильтр с get_config() для получения части работающей конфигурации.

### Шаг 1: Используйте функцию get_config() для получения текущей конфигурации для R1.
Если вы хотите пропустить вывод возможностей (400+ строк), закомментируйте блок операторов, которые выводят возможности, как показано ниже:
```python
'''
print("#Поддерживаемые возможности (YANG модели):")
for capability in m.server_capabilities:
    print(capability)
'''
```
Вы можете использовать метод `get_config()` объекта сессии m NETCONF для получения конфигурации для CSR1kv. Метод get_config() ожидает строкового параметра source, который указывает исходное хранилище данных NETCONF. Для отображения результатов используйте функцию print. Единственным хранилищем данных NETCONF на CSR1kv в настоящее время является работающее хранилище данных. Вы можете проверить это с помощью команды show netconf-yang datastores.
```python
netconf_reply = m.get_config(source="running")
print(netconf_reply)
```
Сохраните и запустите свою программу. Вывод будет содержать более 100 строк, поэтому IDLE может сжать их. Дважды щелкните на текстовом сообщении Squeezed в окне оболочки IDLE, чтобы развернуть вывод.
```shell
devasc@labvm:~/labs/devnet-src/netconf$ python3 ncclient-netconf.py 
```
```xml
<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:3f31bedc-5671-47ca-9781-4d3d7aadae24" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><data><native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"><version>16.9</version><boot-start-marker/><boot-end-marker/><banner><motd><banner>
(вывод опущен)
```
```shell
devasc@labvm:~/labs/devnet-src/netconf$
```
Обратите внимание, что возвращаемый XML не отформатирован. Вы можете скопировать его на тот же сайт, который вы нашли ранее, чтобы отформатировать XML.
```xml
<?xml version="1.0" encoding="UTF-8"?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:3f31bedc-5671-47ca-9781-4d3d7aadae24">
  <data>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
      <version>16.9</version>
      <boot-start-marker/>
      <boot-end-marker/>
      <banner>
        <motd>
          <banner>^C</banner>
        </motd>
      </banner>
      <service>
        <timestamps>
          <debug>
            <datetime>
              <msec/>
            </datetime>
          </debug>
          <log>
            <datetime>
              <msec/>
            </datetime>
          </log>
        </timestamps>
      </service>
      <platform>
        <console xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-platform">
          <output>virtual</output>
        </console>
      </platform>
      <hostname>CSR1kv</hostname>
(вывод опущен)
```

### Шаг 2: Используйте Python для улучшения XML.
Python имеет встроенную поддержку для работы с XML-файлами. Модуль xml.dom.minidom можно использовать для украшения вывода с помощью функции toprettyxml().
В начале сценария добавьте утверждение для импорта модуля xml.dom.minidom.
```python
import xml.dom.minidom
```
Замените простую функцию печати `print(netconf_reply)` версией, которая печатает оптимизированный вывод XML.
```python
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
```
Сохраните и запустите свою программу. XML отображается в более читабельном формате.
```shell
devasc@labvm:~/labs/devnet-src/netconf$ python3 ncclient-netconf.py 
```
```xml
<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:3a5f6abc-76b4-436d-9e9a-7758091c28b7">
        <data>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                        <version>16.9</version>
                        <boot-start-marker/>
                        <boot-end-marker/>
                        <banner>
                                <motd>
                                        <banner>^C</banner>
                                </motd>
                        </banner>
(вывод опущен)
        </data>
</rpc-reply>
```
```shell
devasc@labvm:~/labs/devnet-src/netconf$
```

### Шаг 3: Используйте фильтр с get_config(), чтобы получить только определенную модель YANG.
Администратор сети может захотеть получить только часть текущей конфигурации устройства. NETCONF поддерживает возврат только тех данных, которые определены в параметре фильтра функции get_conf().
Создайте переменную под названием netconf_filter, которая извлекает только данные, определенные моделью Cisco IOS XE Native YANG.
```python
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
netconf_reply = m.get_config(source="running", filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
```
Сохраните и запустите свою программу. Начало вывода будет таким же, как показано ниже. Однако на этот раз отображается только элемент <native> XML. Ранее отображались все модели YANG, доступные на CSR1kv. Фильтрация полученных данных для отображения только родного модуля YANG значительно уменьшает результат. Это происходит потому, что родной модуль YANG включает только подмножество всех моделей Cisco IOX XE YANG.
```shell
devasc@labvm:~/labs/devnet-src/netconf$ python3 ncclient-netconf.py 
```
```xml
<?xml version="1.0" ?> 
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:4da5b736-1d33-47c3-8e3c-349414be0958">
        <data>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                        <version>16.9</version>
                        <boot-start-marker/>
                        <boot-end-marker/>
                        <banner>
                                <motd>
                                        <banner>^C</banner>
                                </motd>
                        </banner>
                        <service>
                                <timestamps>
                                        <debug>
                                                <datetime>
                                                        <msec/>
                                                </datetime>
                                        </debug>
                                        <log>
                                                <datetime>
                                                        <msec/>
                                                </datetime>
                                        </log>
                                </timestamps>
                        </service>
                        <platform>
                                <console xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-platform">
                                        <output>virtual</output>
                                </console>
                        </platform>
                        <hostname>CSR1kv</hostname>
(вывод опущен)
                </native>
        </data>
</rpc-reply>
```
```shell
devasc@labvm:~/labs/devnet-src/netconf$
```

## Часть 5: Использование ncclient для настройки устройства
> В этой части вы будете использовать ncclient для настройки CSR1kv с помощью метода edit_config() модуля manager.

### Шаг 1: Используйте ncclient для редактирования имени хоста для CSR1kv.
Чтобы обновить существующий параметр в конфигурации для CSR1kv, вы можете извлечь местоположение параметра из полученной ранее конфигурации. Для этого шага вы установите переменную для изменения значения <hostname>.
```shell
devasc@labvm:~/labs/devnet-src/netconf$ python3 ncclient-netconf.py 
```
```xml
<?xml version="1.0" ?> 
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:4da5b736-1d33-47c3-8e3c-349414be0958">
        <data>
                <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
(вывод опущен)
                        <hostname>CSR1kv</hostname>
(вывод опущен)
```
Ранее вы определили переменную `<filter>`. Чтобы изменить конфигурацию устройства, вы определите переменную <config>. Добавьте следующую переменную в сценарий ncclient_netconf.py. Вы можете использовать NEWHOSTNAME или любое другое имя хоста по вашему желанию.
```python
netconf_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>NEWHOSTNAME</hostname>
  </native>
</config>
"""
```
Используйте функцию `edit_config()` объекта сессии m NETCONF для отправки конфигурации и сохранения результатов в переменной netconf_reply, чтобы их можно было распечатать. Параметры для функции edit_config() следующие:
- target — целевое хранилище данных NETCONF, которое должно быть обновлено
- config — модификация конфигурации, которая должна быть отправлена
```python
netconf_reply = m.edit_config(target="running", config=netconf_hostname)
```
Функция `edit_config()` возвращает ответное сообщение XML RPC с <ok/>, указывающее на то, что изменение было успешно применено. Повторите предыдущий оператор печати для отображения результатов.
```python
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
```
Сохраните и запустите свою программу. Вы должны получить результат, аналогичный показанному ниже. Вы также можете проверить, что имя хоста изменилось, переключившись на виртуальную машину CSR1kv.
```shell
devasc@labvm:~/labs/devnet-src/netconf$ python3 ncclient-netconf.py 
```
```xml
(вывод опущен)
<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:e304b225-7951-4029-afd5-59e8e7edbaa0">
        <ok/>
</rpc-reply>
```
```shell
devasc@labvm:~/labs/devnet-src/netconf$
```
Отредактируйте свой сценарий, чтобы изменить имя хоста на CSR1kv. Сохраните и запустите свою программу. Вы также можете просто закомментировать код из предыдущего шага, если хотите избежать повторного изменения имени хоста.

### Шаг 2: Используйте ncclient для создания нового интерфейса loopback на R1.
Создайте новую переменную `<config>` для хранения конфигурации нового интерфейса loopback. Добавьте следующее в сценарий ncclient_netconf.py.
> Примечание: Вы можете использовать любое описание по своему усмотрению. Однако используйте только буквенно-цифровые символы, иначе их придется экранировать с помощью обратной косой черты ( \ ).
```python
netconf_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>1</name>
    <description>My first NETCONF loopback</description>
    <ip>
     <address>
      <primary>
       <address>10.1.1.1</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""
```
Добавьте следующую функцию `edit_config()` в файл ncclient_netconf.py, чтобы отправить новую конфигурацию loopback на R1 и затем распечатать результаты.
```python
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
```
Сохраните и запустите свою программу. Вы должны получить результат, похожий на следующий:
```shell
devasc@labvm:~/labs/devnet-src/netconf$ python3 ncclient-netconf.py 
```
(вывод опущен)
```xml
<?xml version="1.0" ?>
<rpc-reply xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="urn:uuid:98437f47-7a93-4cac-9b9e-9bc8afc9dfa1">
        <ok/>
</rpc-reply>
```
```shell
devasc@labvm:~/labs/devnet-src/netconf$
```
На CSR1kv проверьте, что новый интерфейс loopback был создан.
```shell
CSR1kv>en
CSR1kv# show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       192.168.56.101  YES DHCP   up                    up      
Loopback1              10.1.1.1        YES other  up                    up      
CSR1kv# show run | section interface Loopback1
interface Loopback1
 description My first NETCONF loopback
 ip address 10.1.1.1 255.255.255.0
CSR1kv#
```

### Шаг 3: Попытайтесь создать новый интерфейс loopback с тем же адресом IPv4.
Создайте новую переменную `netconf_newloop`. Она будет содержать конфигурацию, создающую новый интерфейс loopback 2, но с тем же IPv4-адресом, что и на loopback 1: 10.1.1.1 /24. В CLI маршрутизатора это приведет к ошибке из-за попытки присвоить дублирующий IP-адрес интерфейсу.
```python
netconf_newloop = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>2</name>
    <description>My second NETCONF loopback</description>
    <ip>
     <address>
      <primary>
       <address>10.1.1.1</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""
```
Добавьте следующую функцию `edit_config()` в файл ncclient_netconf.py для отправки новой конфигурации loopback на CSR1kv. Оператор print для этого шага не нужен.
netconf_reply = m.edit_config(target="running", config=netconf_newloop)
Сохраните и запустите программу. Вы должны получить вывод об ошибке, подобный следующему, с сообщением RPCError Device refused one or more commands.
```shell
devasc@labvm:~/labs/devnet-src/netconf$ python3 ncclient-netconf.py
Traceback (most recent call last):
  File "ncclient-netconf.py", line 80, in <module>
    netconf_reply = m.edit_config(target="running", config=netconf_newloop)
  File "/home/devasc/.local/lib/python3.8/site-packages/ncclient/manager.py", line 231, in execute
    return cls(self._session,
  File "/home/devasc/.local/lib/python3.8/site-packages/ncclient/operations/edit.py", line 69, in request
    return self._request(node)
  File "/home/devasc/.local/lib/python3.8/site-packages/ncclient/operations/rpc.py", line 348, in _request
    raise self._reply.error
ncclient.operations.rpc.RPCError: inconsistent value: Device refused one or more commands
devasc@labvm:~/labs/devnet-src/netconf$
```
NETCONF не применит ни одну из отправленных конфигураций, если одна или несколько команд будут отклонены. Чтобы проверить это, введите команду show ip interface brief на R1. Обратите внимание, что ваш новый интерфейс не был создан.
```shell
CSR1kv# show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       192.168.56.101  YES DHCP   up                    up      
Loopback1              10.1.1.1        YES other  up                    up      
```

## Часть 6: Челлендж: Измените программу, использованную в этой лаборатории
Ниже приведена полная программа, созданная в этой лаборатории, без единого комментария кода, чтобы вы могли запустить сценарий без ошибок. Ваш сценарий может выглядеть иначе. Практикуйте свои навыки работы с Python, изменяя программу для отправки различных команд проверки и конфигурации.
```python
from ncclient import manager
import xml.dom.minidom

m = manager.connect(
        host="192.168.56.101",
        port=830,
        username="cisco",
        password="cisco123!",
        hostkey_verify=False
    )

print("#Supported Capabilities (YANG models):")

for capability in m.server_capabilities:
    print(capability) 

netconf_reply = m.get_config(source="running")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""

netconf_reply = m.get_config(source="running", filter=netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>CSR1kv</hostname>
  </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>1</name>
    <description>My NETCONF loopback</description>
    <ip>
     <address>
      <primary>
       <address>10.1.1.1</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_newloop = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>2</name>
    <description>My second NETCONF loopback</description>
    <ip>
     <address>
      <primary>
       <address>10.1.1.1</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_newloop)
```