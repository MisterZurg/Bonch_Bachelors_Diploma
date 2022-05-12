# Исследование сетевых протоколов
## Цель лабораторной работы:
- Часть 1: Настройка DNS
- Часть 2: Настройка DHCP
- Часть 3: Настройка NTP
- Часть 4: Использование SSH для безопасного доступа к коммутатору
- Часть 5: Изучение идентификаторов объектов SNMP MIB
- Часть 6: Настройка HTTPS
- Часть 7: Настройка EMAIL
- Часть 8: Настройка FTP

## Необходимые ресурсы:
- 1 ПК
- Packet Tracer 7.4.0

## Таблица адресации

|Устройство|Интерфейс|IPv4 Адрес|Маска подсети|Шлюз по умолчанию|
|:---:|:---:|:---:|:---:|:---:|
|R1	|G0/0/0	|209.165.200.225	|255.255.255.248	|нет сведений|
|^^ |G0/0/1	|10.1.1.2	        |255.255.255.252    |^^|
|R3	|G0/0/0	|10.2.2.2	        |255.255.255.252	|нет сведений|
|^^ |G0/0/1	|172.16.3.1	        |255.255.255.0      |^^|
|FIREWALL	|VLAN1	            |192.168.1.1	    |255.255.255.0	|нет сведений|
|^^         |VLAN2	            |209.165.200.226	|255.255.255.248|^^|
|^^         |VLAN3	            |192.168.2.1	    |255.255.255.0 |^^|
|DEVASC Server	|NIC	|Входящий: 192.168.2.3	|255.255.255.0	|192.168.1.1|
|^^             |VLAN1	|Исходящий: 209.165.200.227	|255.255.255.248|	209.165.200.225
|Example Server	|NIC	|64.100.0.10	|255.255.255.0	|64.100.0.1|
|PC-A	        |NIC	|Присвоен DHCP	|255.255.255.0	|192.168.1.1|
|PC-B	        |NIC	|172.16.3.2	    |255.255.255.0	|172.16.3.1|

## Порядок выполнения работы
## Часть 1: Настройка DNS
> Всем узлам в сети присваивается IP-адрес. IP-адрес может быть адресом IPv4 или IPv6. или и то, и другое. Это относится и ко всем узлам в Интернете. Но вы не используете их IP-адреса для общения с ними. Вы используете обычные имена, такие как cisco.com. Система доменных имен (DNS) - это служба, которая автоматически переводит общие, легко запоминающиеся имена в IP-адреса, чтобы связь между устройствами может осуществляться. В этом задании Packet Tracer устройства используют IPv4 адреса.

### Шаг 1: Настройте локальный DNS-сервер.
Щелкните **Corporate server > Services. > DNS**.

Нажмите **On**, чтобы включить службу **DNS**.

Теперь, когда **DNS** включен, вам нужно предоставить информацию для всех хостов в сети (сетях), для которых вы хотите перевести их имена в адреса IPv4.

В поле **Name** введите `www.example.com`.

В поле **Address** введите IPv4-адрес `64.100.0.10`.

Нажмите кнопку **Add**.

Теперь вы увидите запись, которая показывает имя хоста и IPv4-адрес Example Server. Здесь DNS будет искать имя хоста и возвращать IPv4-адрес этого хоста любому устройству, которое его запрашивает.

### Шаг 2: Настройте и протестируйте использование локального DNS-сервера.
Нажмите **PC-A > Config**.

В поле DNS Server введите IPv4-адрес Corporate DNS server: `192.168.1.3`.

Теперь, когда PC-A использует общие имена хостов, он будет посылать DNS-запрос на IPv4-адрес узла с таким именем хоста.

Нажмите **Desktop > Command Prompt**.

Пропингуйте **www.example.com**. 

```shell
C:\> ping www.example.com 
Pinging 64.100.0.10 with 32 bytes of data: 
Request timed out. 
<вывод опущен>

C:\> ping www.example.com 
Pinging 64.100.0.10 with 32 bytes of data: 
Reply from 64.100.0.10: bytes=32 time=3ms TTL=125 
<вывод опущен>
C:\>
```

### Шаг 3: Настройте и протестируйте использование удаленного DNS-сервера.
PC-B не имеет локального DNS-сервера. Поэтому в качестве DNS-сервера он будет использовать Example Server.
Нажмите **PC-B > Config**.

В поле DNS Server введите IPv4-адрес корпоративного DNS-сервера: 64.100.0.10.

Нажмите **Desktop > Command Prompt**.

Пропингуйте `www.example.com`.

Пропингуйте `www.devasc-netacad.pka`. 

Закройте окно Command Prompt и нажмите Web Browser.

Введите `www.example.com` в поле URL и нажмите Go. Теперь вы должны увидеть веб-страницу Example.com.

Введите `www.devasc-netacad.pka` в поле URL и нажмите Go. Теперь вы должны увидеть веб-страницу сервера DEVASC.

## Часть 2: Настройка DHCP
> Ручная настройка адресов IPv4 подходит для очень маленьких сетей, но в больших сетях необходимо автоматически предоставлять IPv4-адресацию устройствам при подключении к сети. Dynamic Host Configuration Protocol (DHCP) обеспечивает эту услугу. Это также удобно при перемещении устройств, поскольку при перемещении в другую подсеть, они получат новый адрес и смогут общаться с другими узлами. 
> Еще одна замечательная особенность DHCP заключается в том, что он автоматически устанавливает не только IPv4-адрес для хоста, но и подсеть, шлюз по умолчанию и адрес DNS-сервера. Это позволяет легко настраивать несколько частей информации настраивать на хостах автоматически.

### Шаг 1: Настройте DHCP на Corporate server.
Щелкните **Corporate server > Services > DHCP**

Нажмите кнопку **On**, чтобы включить службу **DHCP**.

Теперь мы определим пул адресов **IPv4**, которые мы желаем назначить хостам. Будете использовать IPv4 адреса в подсети 192.168.1.0. Мы не можем использовать адрес 192.168.1.1, поскольку он уже используется интерфейсом FIREWALL. Мы также не можем использовать адрес Corporate server 192.168.1.3. Кроме того, хорошей практикой является оставление некоторых адресов свободными для статического назначения серверам или другим устройствам, адрес которых должен оставаться неизменным.

В настоящее время имя пула - `serverPool`. Не изменяйте его.

Для параметра Default Gateway введите IPv4-адрес внутреннего интерфейса FIREWALL: 192.168.1.1. Это обеспечит каждому узлу DHCP маршрут в другие сети

Для DNS Server введите IPv4-адрес Corporate server: `192.168.1.3`. Это предоставит каждому узлу DHCP адрес, который будет использоваться для отправки сообщений DNS.

Для начального IP-адреса используйте `192.168.1.10`. Это позволит в будущем создать в сети несколько статически назначенных устройств.

Для маски подсети используйте `255.255.255.0`.

Для параметра `Maximum number of users` введите `245`.

Нажмите **Save**, чтобы перезаписать `serverPool` по умолчанию.

### Шаг 2: Проверьте конфигурацию DHCP.
Нажмите **PC-A > IP Configuration > DCHP**.

Это может занять немного времени, но вы должны получить IPv4-адрес от маршрутизатора за пределами первых 10 адресов. Вы также должны увидеть маску подсети, шлюз по умолчанию и DNS-сервер, которые будут предоставлены для вас автоматически

## Часть 3: Настройка NTP
> Часы на маршрутизаторе или коммутаторе важны для управления, обеспечения безопасности и устранения неполадок в сети. Даже в небольших сетях важно синхронизировать время на всех устройствах. Пытаться сделать это вручную практически невозможно, особенно в больших сетях. Протокол сетевого времени (NTP) можно использовать для синхронизации времени на каждом устройстве, получая его от NTP-сервера, что обеспечивает одинаковое время на всех устройствах.

### Шаг 1: Включите службу NTP.
Щелкните **Corporate server > Services > NTP**.

Нажмите кнопку **On** рядом с пунктом Services.

### Шаг 2: Исследуйте NTP на S2.
**S2** уже настроен на использование корпоративного сервера в качестве NTP-сервера.

Нажмите **S2 > CLI**.

Войдите в привилегированный режим **EXEC** с помощью команды `enable`. Используйте cisco в качестве пароля.
```shell
S2> enable 
Password: 
S2#
```

Отобразите текущее время и дату с помощью команды show clock detail. Обратите внимание, что время устанавливается оборудованием и не является точным
```shell
S2# show clock detail 
*0:3:44.318 UTC Mon Mar 1 1993
Time source is hardware calendar
S2#
```
Вы можете вручную настроить время с помощью команды `clock`. Однако лучше использовать NTP-сервер. Войдите в режим глобальной конфигурации с помощью команды configure terminal.
```shell
S2# configure terminal
Enter configuration commands, one per line. End with CNTL/Z. 
S2(config)#
```

Настройте **S2** на использование Corporate server в качестве **NTP-сервера**. Выйдите из режима глобальной конфигурации и убедитесь, что S2 теперь использует NTP. Теперь время и дата должны быть точными.
```shell
S2(config)# ntp server 192.168.1.3 
S2(config)# exit 
S2# show clock detail
14:1:26.216 UTC Thu May 21 2020
Time source is NTP
S2#
```

## Часть 4: Использование SSH для безопасного доступа к коммутатору
> Secure Shell (SSH) — это протокол, который используется для шифрования связи между клиентом и хостом. SSH является предпочтительным типом соединения, поскольку он безопасен по сравнению с Telnet. SSH уже был настроен на S2.

Щелкните **PC-A > Desktop > Command Prompt**.

Попытайтесь установить небезопасный сеанс **Telnet** на **S2**.
```shell
C:\> telnet 192.168.1.4
Trying 192.168.1.4 ...Open
[Connection to 192.168.1.4 closed by foreign host]
```
**S2** отклоняет ваш запрос, поскольку он настроен только для доступа по SSH. 

Попытайтесь установить SSH-соединение с S2. Пароль - **cisco**.
```shell
C:\> ssh -l administrator 192.168.1.4
Password: 
S2>
```
Теперь мы можем безопасно настроить **S2**

Мы получаем доступ к командной строке для **S2** через защищенное соединение. Войдите в режим глобальной конфигурации с командой enable, чтобы убедиться, что вы можете настроить коммутатор удаленно. Используйте cisco в качестве пароль. Затем введите exit, чтобы завершить сеанс SSH.
```shell
S2> enable
Password: 
S2# exit 
[Connection to 192.168.1.4 closed by foreign host]
C:\>
```

## Часть 5: Изучение идентификаторов объектов SNMP MIB
> Simple Network Management Protocol (SNMP) можно использовать для получения и установки переменных, связанных с состоянием и конфигурацией сетевых узлов, таких как маршрутизаторы и коммутаторы, а также сетевых клиентских компьютеров.

Нажмите **PC-B > MIB Browser**.

Введите адрес R3 в поле Address: `172.16.3.1`.

Нажмите **Advanced**.

Введите `read` в поле для **Read Community**.

Введите `write` в поле **Write Community**.

Измените **SNMP Version** на **v3**.

Нажмите **OK**.

Нажмите стрелку рядом с `MIB Tree`, чтобы развернуть дерево.

Щелкните стрелку рядом с `MIBs router_std`.

Продолжайте расширять дерево, пока не дойдете до `.mgmt`.

Разверните `.mgmt`.

Продолжайте расширять дерево, пока не достигнете `.system`.

Разверните `.system`. 

Щелкните `.sysName`.

Нажмите кнопку **GO**.

Теперь вы увидите, что значение объекта R3.

Разверните дерево **.interfaces > .ifTable > .ifEntry > .ifOperStatus** и нажмите GO.

Вы увидите, что два из трех интерфейсов работают. Теперь вы можете легко запросить любую информацию о маршрутизаторе.

## Часть 6: Настройка HTTPS
> Когда вы подключаетесь к серверу с помощью HTTP, вы предполагаете, что это правильный сервер. Данные передаваемые между вами и сервером, отправляются в виде открытого текста, поэтому если кто-то перехватит эти данные, он сможет их прочесть и манипулировать ими. Обычно это не является проблемой, если вы просто просматриваете Интернет. Но если вы создаете учетную запись, получаете доступ к ней или предоставите какую-либо личную информацию, она может быть перехвачена и использована кем-то другим. Secure HTTP (HTTPS) добавляет уровень безопасности, шифруя соединение между вами и сервером. Сайт должен иметь сертификат безопасности из надежного источника, чтобы убедиться в его легитимности. Ваш браузер проверяет, что сертификат действителен и получен из надежного источника, прежде чем соединить вас с сайтом.

### Шаг 1: Откройте веб-страницу с компьютера.
Нажмите **PC-B > Desktop > Web Browser**.

Введите `www.devasc-netacad.pka` в поле URL и нажмите **Go**. Обратите внимание, что протокол - HTTP (http://).

### Шаг 2: Изучите межсетевой экран.
Нажмите `FIREWALL > CLI`.

Пароль отсутствует, поэтому нажмите **Enter**.

Введите `show run` и нажмите **Enter**.

Используйте пробел для прокрутки конфигурации брандмауэра.

Обратите внимание на следующие две конфигурации в списке доступа OUTSIDE-DMZ:
```shell
<вывод опущен>
access-list OUTSIDE-DMZ extended permit icmp any host 192.168.2.3 
access-list OUTSIDE-DMZ extended permit tcp any host 192.168.2.3 eq www 
access-list OUTSIDE-DMZ extended permit tcp any host 192.168.2.3 eq 443
<вывод опущен>
```
Строка с www разрешает порт 80, который является незащищенным HTTP-трафиком. Строка с портом 443 разрешает порт 443, который является защищенным HTTP (HTTPS) трафиком.
Удалите access-list, разрешающий незащищенный HTTP-трафик на порту 80
```shell
FIREWALL# configure terminal
FIREWALL(config)# no access-list OUTSIDE-DMZ extended permit tcp any host 192.168.2.3 eq www 
FIREWALL(config)#
```

### Шаг 3: Настройте HTTPS.
Щелкните **DEVASC Server > Services > HTTP**.

Обратите внимание, что для **HTTP** установлено значение **On**, а для **HTTPS** - **Off**.

Выключите **HTTP** и включите **HTTPS**. Даже если **FIREWALL** больше не будет разрешать доступ по **HTTP**, лучше всего настроить сервер так, чтобы он разрешал только **HTTPS**.

Нажмите кнопку **On** для HTTPS.

### Шаг 4: Проверьте конфигурацию HTTPS.
Нажмите **PC-B > Web Browser**.

Убедитесь, что **PC-B** больше не может получить доступ к `www.devasc-netacad.pka` с помощью **HTTP**. Через несколько секунд вы должны получить сообщение **Request Timeout**. Нажмите **Fast Forward Time**, чтобы ускорить процесс.

Измените `http` на `https` и нажмите **Go**. Теперь вы должны увидеть веб-страницу `https://www.devasc-netacad.pka`

## Часть 7: Настройка EMAIL
> Клиенты электронной почты используют Simple Mail Transfer Protocol (SMTP), порт 25, для отправки электронной почты на сервер. SMTP также используется для отправки электронной почты между серверами. Клиент электронной почты использует протокол Post Office Protocol 3 (POP3), порт 110, для получения почты с сервера.

### Шаг 1: Настройте сервер EMAIL.
Щелкните **Example Server > Services > EMAIL**.

Включите службы **SMTP** и **POP3**.

Введите `www.example.com` в поле **Domain Name box**.

Нажмите **Set**.

### Шаг 2: Создание пользователей.
В поле `User` введите **Student1**.

Введите `class` в качестве пароля.

Нажмите на плюс (+), чтобы добавить пользователя.

Повторите этот шаг, чтобы добавить пользователя под именем Student2 с тем же паролем.

### Шаг 3: Конфигурирование клиентов.
Щелкните **PC-A > Desktop > Email**.

Введите следующую информацию:
- Ваше имя: `Student1` 
- Адрес электронной почты: `Student1@www.example.com` 
- Сервер входящих сообщений: `64.100.0.10` 
- Сервер исходящих сообщений: `64.100.0.10` 
- Имя пользователя: `Student1` 
- Пароль: `class`
Нажмите кнопку **Save**.

Повторите настройку на **PC-B**, заменив `Student1` на `Student2`.

### Шаг 4: Отправка и получение электронной почты
На PC-B откройте программу Email, если она не открыта.

Нажмите кнопку Compose.

Заполните следующую информацию:
- Кому: `Student1@www.example.com`
- Тема: `Электронная почта`

В поле сообщения введите сообщение для `Student1`, например, `"Сколько тебе лет?"`.

Нажмите **Send**.

На **PC-A** откройте **Email**, если он не открыт.

Нажмите Receive. Это может занять некоторое время и несколько попыток.

Дважды щелкните сообщение, когда оно придет, чтобы прочитать его.

Нажмите **Reply**.

Введите ответ на сообщение электронной почты, например, "Мне 5, мне 5 лет!"и нажмите Send.

Вернитесь в **PC-B**, нажмите **Receive**, чтобы прочитать ответ.

## Часть 8: Настройка FTP
> File Transfer Protocol (FTP) — это широко используемое приложение для передачи файлов между клиентами и серверами в сети. Сервер настраивается для запуска службы, где клиенты подключаются, входят в систему и передают файлы. FTP использует порт 21 в качестве командного порта сервера для создания соединения. Затем FTP использует порт 20 для передачи данных.

### Шаг 1: Настройка сервера.
Нажмите **Corporate server > Services > FTP**.

Нажмите кнопку **On**, чтобы включить службу FTP.

В поле `Username` введите `Student`.

В поле `Password` введите `class`.

Установите все флажки под этими полями, чтобы разрешить пользователю запись, чтение, удаление, переименование.

Нажмите кнопку **Add**.

### Шаг 2: Используйте службу FTP
Нажмите **PC-A > Desktop > Command Prompt**.

Введите `dir`, чтобы увидеть файлы на компьютере.
```shell
C:\> dir
Volume in drive C has no label.
Volume Serial Number is 5E12-4AF3
Directory of C:\ 

2/6/2106 23:28 PM 26 sampleFile.txt 
26 bytes 1 File(s) 
C:\>

FTP on Corporate server IPv4-адрес
C:\> ftp 192.168.1.3 
Trying to connect...192.168.1.3
Connected to 192.168.1.3 
220- Welcome to PT Ftp server 
Username:
```
Введите имя пользователя и пароль, которые вы настроили ранее для получения доступа.

Введите `dir`, чтобы увидеть файлы, доступные на сервере.
```shell
ftp> dir 

Listing /ftp directory from 192.168.1.3: 
0 : asa842-k8.bin 5571584 
1 : asa923-k8.bin 30468096 
2 : c1841-advipservicesk9-mz.124-15.T1.bin 33591768 
3 : c1841-ipbase-mz.123-14.T7.bin 13832032
<вывод опущен>
```
Введите `put sampleFile.txt`, чтобы отправить файл на сервер
```shell
ftp> put sampleFile.txt 

Writing file sampleFile.txt to 192.168.1.3: 
File transfer in progress... 

[Transfer complete - 26 bytes] 

26 bytes copied in 0.08 secs (325 bytes/sec) 
ftp>
```
Снова используйте команду `dir`, чтобы снова перечислить содержимое FTP-сервера и увидеть файл.

Введите `get asa842-k8.bin`, чтобы получить файл с сервера. Это может занять 30 секунд или более поскольку файл очень большой.
```shell
ftp> get asa842-k8.bin 

Reading file asa842-k8.bin from 192.168.1.3: 
File transfer in progress... 

[Transfer complete - 5571584 bytes]

5571584 bytes copied in 46.893 secs (42706 bytes/sec) 
ftp>
```
Введите `delete sampleFile.txt`, чтобы удалить файл с сервера.
```shell
ftp> delete sampleFile.txt

Deleting file sampleFile.txt from 192.168.1.3: ftp> 
[Deleted file sampleFile.txt successfully ] 
ftp>
```
Введите `quit`, чтобы выйти из FTP-клиента.
Снова отобразите содержимое каталога на ПК, чтобы увидеть файл изображения с FTP-сервера