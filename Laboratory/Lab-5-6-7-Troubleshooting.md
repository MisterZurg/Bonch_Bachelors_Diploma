# Инструменты для устранения неполадок в сети
## Цель лабораторной работы:
- Часть 1: Запуск виртуальной машины DEVASC
- Часть 2: Знакомство с инструментом ifconfig
- Часть 3: Знакомство с инструментом ping
- Часть 4: Знакомство с инструментом traceroute
- Часть 5: Знакомство с инструментом nslookup

## Необходимые ресурсы:
- 1 ПК
- Virtual Box или VMWare
- DEVASC виртуальная машина

## Порядок выполнения работы
## Часть 1: Запуск виртуальной машины DEVASC
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.

## Часть 2: Знакомство с инструментом ifconfig
> Утилита ifconfig — это приложение для использования в операционных системах на базе UNIX, таких как Linux. Аналогичная утилита доступна в Windows под названием ipconfig. Эти приложения используются для управления сетевыми интерфейсами из командной строки. С помощью ifconfig можно выполнить следующие действия:
> - Настраивать IP-адреса и маски подсети для интерфейсов.
> - Получать информацию о состоянии сетевых интерфейсов.
> - Включать или отключать сетевые интерфейсы.
> - Изменять MAC-адреса сетевого интерфейса.

### Шаг 1: Просмотрите параметры ifconfig.
Инструмент ifconfig имеет множество различных опций, которые могут быть добавлены к команде для выполнения определенных задач.
Откройте окно терминала либо непосредственно с рабочего стола, либо в VS Code.
Введите ifconfig --help, чтобы увидеть все доступные опции для команды.
```shell
devasc@labvm:~$ ifconfig --help
Usage:
  ifconfig [-a] [-v] [-s] <interface> [[<AF>] <address>]
  [add <address>[/<prefixlen>]]
  [del <address>[/<prefixlen>]]
  [[-]broadcast [<address>]]  [[-]pointopoint [<address>]]
  [netmask <address>]  [dstaddr <address>]  [tunnel <address>]
  [outfill <NN>] [keepalive <NN>]
  [hw <HW> <address>]  [mtu <NN>]
  [[-]trailers]  [[-]arp]  [[-]allmulti]
  [multicast]  [[-]promisc]
  [mem_start <NN>]  [io_addr <NN>]  [irq <NN>]  [media <type>]
  [txqueuelen <NN>]
  [[-]dynamic]
  [up|down] ...
```
Здесь представлен обзор некоторых наиболее широко используемых вариантов:
- add or del — Эта опция позволяет добавлять или удалять IP-адреса и их маску подсети.
- hw ether — Используется для изменения физического MAC-адреса. Это может быть полезно, например, для изменения его на легко узнаваемое имя, чтобы он выделялся в журналах при поиске неисправностей.
- up and down — Эти опции используются для включения и отключения интерфейсов. Убедитесь, какой интерфейс вы отключаете. Если это тот интерфейс, который вы используете для удаленного подключения к устройству, вы будете отключены!

### Шаг 2: Просмотрите состояние всех интерфейсов.
Отобразите состояние всех используемых сетевых интерфейсов, выдав команду ip addr самостоятельно.
```shell
devasc@labvm:~$ ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:e9:3d:e6 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic enp0s3
       valid_lft 85901sec preferred_lft 85901sec
    inet6 fe80::a00:27ff:fee9:3de6/64 scope link 
       valid_lft forever preferred_lft forever
3: dummy0: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN group default qlen 1000
    link/ether e2:2b:24:96:98:b8 brd ff:ff:ff:ff:ff:ff
    inet 192.0.2.1/32 scope global dummy0
       valid_lft forever preferred_lft forever
    inet 192.0.2.2/32 scope global dummy0
       valid_lft forever preferred_lft forever
    inet 192.0.2.3/32 scope global dummy0
       valid_lft forever preferred_lft forever
    inet 192.0.2.4/32 scope global dummy0
       valid_lft forever preferred_lft forever
    inet 192.0.2.5/32 scope global dummy0
       valid_lft forever preferred_lft forever
    inet6 fe80::e02b:24ff:fe96:98b8/64 scope link 
       valid_lft forever preferred_lft forever
devasc@labvm:~$
```
Из этого вывода мы можем многое узнать об интерфейсах виртуальной машины:
- Имеется 3 интерфейса, интерфейс loopback (lo), enp0s3 и dummy0.
- ether показывает MAC-адрес и то, что Ethernet является инкапсуляцией соединения.
- inet — IP-адрес, маска подсети показана в косой черте, а brd — широковещательный адрес.
- UP указывает, что интерфейс включен.
- mtu — это Maximum Transmission Unit, определяющий максимальное количество байт, которое кадр может быть передан на данном носителе до фрагментации.

## Часть 3: Знакомство с инструментом ping
> Инструмент ping — это приложение, которое используется для тестирования сетевого соединения между устройствами. ping использует протокол Internet Control Message Protocol (ICMP) для отправки пакетов на устройство в сети и ожидает ответа устройства. ping сообщает о сетевых ошибках, потере пакетов и времени жизни (TTL), среди прочей статистики.

### Шаг 1: Просмотрите параметры пинга.
Ping доступен только в окне терминала или командной строки.
Введите ping -help, чтобы увидеть все доступные параметры команды.
```shell
devasc@labvm:~$ ping -help

Usage
  ping [options] <destination>

Options:
  <destination>      dns name or ip address
  -a                 use audible ping
  -A                 use adaptive ping
  -B                 sticky source address
  -c <count>         stop after <count> replies
  -D                 print timestamps
  -d                 use SO_DEBUG socket option
  -f                 flood ping
  -h                 print help and exit
  -I <interface>     either interface name or address
  -i <interval>      seconds between sending each packet
  -L                 suppress loopback of multicast packets
  -l <preload>       send <preload> number of packages while waiting replies
  -m <mark>          tag the packets going out
  -M <pmtud opt>     define mtu discovery, can be one of <do|dont|want>
  -n                 no dns name resolution
  -O                 report outstanding replies
  -p <pattern>       contents of padding byte
  -q                 quiet output
  -Q <tclass>        use quality of service <tclass> bits
  -s <size>          use <size> as number of data bytes to be sent
  -S <size>          use <size> as SO_SNDBUF socket option value
  -t <ttl>           define time to live
  -U                 print user-to-user latency
  -v                 verbose output
  -V                 print version and exit
  -w <deadline>      reply wait <deadline> in seconds
  -W <timeout>       time to wait for response

IPv4 options:
  -4                 use IPv4
  -b                 allow pinging broadcast
  -R                 record route
  -T <timestamp>     define timestamp, can be one of <tsonly|tsandaddr|tsprespec>

IPv6 options:
  -6                 use IPv6
  -F <flowlabel>     define flow label, default is random
  -N <nodeinfo opt>  use icmp6 node info query, try <help> as argument

For more details see ping(8).
devasc@labvm:~$
```

### Шаг 2: Выполните Ping хоста.
Инструмент ping имеет множество различных опций, которые можно выбрать для настройки того, как будет происходить взаимодействие. Некоторые из опций, которые можно указать, включают:
- Сколько эхо-запросов ICMP нужно отправить.
- IP-адрес источника, если на устройстве имеется несколько интерфейсов.
- Время ожидания ответа.
- Размер пакета, если вы хотите отправлять пакеты большего размера, чем 64 байта по умолчанию. Это поможет определить, каков максимальный блок передачи (MTU).
Пропингуем `www.yandex.ru`, чтобы проверить, доступен ли он.
```shell
devasc@labvm:~$ ping -c 5 www.yandex.ru
PING www.yandex.ru (5.255.255.80) 56(84) bytes of data.
64 bytes from yandex.ru (5.255.255.80): icmp_seq=1 ttl=53 time=49.2 ms
64 bytes from yandex.ru (5.255.255.80): icmp_seq=2 ttl=53 time=18.9 ms
64 bytes from yandex.ru (5.255.255.80): icmp_seq=3 ttl=53 time=19.8 ms
64 bytes from yandex.ru (5.255.255.80): icmp_seq=4 ttl=53 time=15.9 ms
64 bytes from yandex.ru (5.255.255.80): icmp_seq=5 ttl=53 time=33.4 ms

--- www.yandex.ru ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4007ms
rtt min/avg/max/mdev = 15.879/27.426/49.212/12.445 ms
devasc@labvm:~$
```
Этот пинг задал счетчик из 5 пакетов.
Инструмент ping автоматически выполняет разрешение DNS, возвращая 5.255.255.80 (ваш возвращенный IP-адрес может быть другим). Также отображается время жизни (TTL) для полученных эхо-ответов и время прохождения в оба конца. Итоговая статистика подтверждает, что было передано 5 пакетов ICMP эхо-запроса и получено 5 пакетов ICMP эхо-ответа, что составляет 0% потери пакетов. Также отображаются статистические данные о минимальном, среднем, максимальном и стандартном отклонении времени, которое потребовалось пакетам, чтобы добраться до места назначения и обратно.
Если вы не получаете никаких ответов от адресата, это не обязательно означает, что хост находится в автономном режиме или недоступен. Это может означать, что ICMP-пакеты блокируются брандмауэром. Лучшей практикой является предоставление только тех услуг, которые должны быть доступны на узлах сети.
Для IPv6 существует аналогичная утилита, которая называется ping6 и также доступна в большинстве операционных систем.

## Часть 4: Знакомство с инструментом traceroute
> Инструмент traceroute отображает маршрут, по которому пакеты идут к месту назначения. Альтернатива для Windows называется tracert. Наблюдение за тем, какой путь проходит сетевой трафик от источника к месту назначения, важно для устранения неполадок, поскольку можно обнаружить и устранить петли маршрутизации и неоптимальные пути.
traceroute использует ICMP-пакеты для определения пути к месту назначения. Поле Time to Live (TTL) в заголовке IP-пакета используется для предотвращения бесконечных петель в сети. Для каждого хопа или маршрутизатора, через который проходит IP-пакет, поле TTL уменьшается на единицу. Когда значение поля TTL достигает 0, пакет отбрасывается, что позволяет избежать бесконечных циклов. Обычно поле TTL устанавливается на максимальное значение, 255, в источнике трафика, поскольку хост пытается максимально увеличить шансы того, что пакет попадет в пункт назначения. traceroute изменяет эту логику и постепенно увеличивает значение TTL, начиная с 1, и продолжает добавлять 1 к полю TTL в следующем пакете и так далее. Установка значения TTL равного 1 для первого пакета означает, что пакет будет отброшен на первом маршрутизаторе. По умолчанию большинство маршрутизаторов отправляют обратно источнику трафика пакет ICMP Time Exceeded, информирующий его о том, что пакет достиг значения TTL 0 и должен быть отброшен. traceroute использует информацию, полученную от маршрутизатора, для определения его IP-адреса и имени хоста, а также времени прохождения маршрута.
Для IPv6 существует альтернатива под названием traceroute6 для операционных систем на базе UNIX и tracert6 для операционных систем на базе Microsoft Windows.

### Шаг 1: Просмотрите параметры traceroute.
Введите traceroute --help, чтобы увидеть все доступные параметры команды.
```shell
devasc@labvm:~$ traceroute --help
Usage: traceroute [OPTION...] HOST
Print the route packets trace to network host.

  -f, --first-hop=NUM        set initial hop distance, i.e., time-to-live
  -g, --gateways=GATES       list of gateways for loose source routing
  -I, --icmp                 use ICMP ECHO as probe
  -m, --max-hop=NUM          set maximal hop count (default: 64)
  -M, --type=METHOD          use METHOD (`icmp' or `udp') for traceroute
                             operations, defaulting to `udp'
  -p, --port=PORT            use destination PORT port (default: 33434)
  -q, --tries=NUM            send NUM probe packets per hop (default: 3)
      --resolve-hostnames    resolve hostnames
  -t, --tos=NUM              set type of service (TOS) to NUM
  -w, --wait=NUM             wait NUM seconds for response (default: 3)
  -?, --help                 give this help list
      --usage                give a short usage message
  -V, --version              print program version

Mandatory or optional arguments to long options are also mandatory or optional
for any corresponding short options.

Report bugs to <bug-inetutils@gnu.org>.
devasc@labvm:~$
```

В traceroute также доступны несколько опций, включая:
- Значение TTL первого отправленного пакета, по умолчанию 1.
- Максимальное значение TTL. По умолчанию он будет увеличивать значение TTL до 64 или пока не будет достигнут пункт назначения.
- Адрес источника в случае наличия нескольких интерфейсов на устройстве.
- Значение Quality of Service (QoS) в IP-заголовке.
- Длину пакета.

### Шаг 2: Используйте traceroute, чтобы найти путь к веб-серверу.
Из-за того, как Virtual Box реализует NAT-сеть, вы не можете отслеживать за пределами своей виртуальной машины. Вам нужно будет переключить свою виртуальную машину в режим Bridged. Поэтому мы рекомендуем оставить вашу ВМ в режиме NAT. 
Однако вы должны иметь возможность использовать команду traceroute на локальном хосте. Для компьютеров Mac и Linux используйте команду traceroute. Для хостов Windows используйте команду tracert, как показано ниже. Откройте командную строку на локальном узле и проследите маршрут до cloud.yandex.ru, чтобы узнать, сколько переходов и сколько времени требуется для достижения маршрута. Ваши результаты будут отличаться.
```shell
C:\> tracert cloud.yandex.ru

Трассировка маршрута к cloud.yandex.ru [87.250.250.108]
с максимальным числом прыжков 30:

  1     1 ms     2 ms    <1 мс  192.168.0.1
  2     4 ms     2 ms     3 ms  bras240-lo0.spb.corbina.net [85.21.129.73]
  3     *        *        *     Превышен интервал ожидания для запроса.
  4    14 ms    12 ms    47 ms  bmor19-bb-tengige0-3-0-3.spb.corbina.net [85.21.225.198]
  5    20 ms   149 ms    10 ms  ko-crs-be5.corbina.net [195.14.54.184]
  6    47 ms   132 ms    52 ms  corbina-gw.dante.yandex.net [83.102.145.178]
  7    16 ms    49 ms    17 ms  vla-32z5-ae1-1.yndx.net [93.158.172.25]
  8     *        *        *     Превышен интервал ожидания для запроса.
  9   124 ms    25 ms    13 ms  cloud.yandex.ru [87.250.250.108]

Трассировка завершена.

C:\>
```
Результат показывает, что на пути имеется 5 переходов, а также отображается время пути туда и обратно.

## Часть 5: Знакомство с инструментом nslookup
> Инструмент nslookup используется для запроса системы доменных имен (DNS) с целью получения сопоставления доменных имен с IP-адресами. Этот инструмент полезен для определения того, разрешает ли DNS-сервер, настроенный на определенном хосте, имена хостов в IP-адреса.

## Шаг 1: Запрос домена.
Чтобы использовать nslookup, необходимо ввести имя хоста, которое вы пытаетесь преобразовать в IP-адрес. Для поиска IP-адреса будет использован настроенный DNS-сервер. Вы также можете указать DNS-сервер для использования.
Использование: `nslookup [HOST] [SERVER]`

Введите nslookup practicum.yandex.ru, чтобы определить IP-адрес домена.
```shell
devasc@labvm:~$ nslookup practicum.yandex.ru
Server:         127.0.0.53
Address:        127.0.0.53#53

Non-authoritative answer:
Name:   practicum.yandex.ru
Address: 87.250.250.5
Name:   practicum.yandex.ru
Address: 2a02:6b8::313

devasc@labvm:~$
```

Команда возвращает неавторитетный ответ, а также имя и адрес IPv4 и IPv6. Неавторитетный ответ означает, что сервер не содержит оригинальных записей зоны домена, а создан на основе предыдущих поисков DNS.

### Шаг 2: Запрос IP-адреса.
Вы также можете просмотреть IP-адреса, чтобы узнать связанный с ним домен.
Запросите у DNS-сервера IP-адрес 8.8.8.8.
```shell
devasc@labvm:~$ nslookup 8.8.8.8
8.8.8.8.in-addr.arpa name = dns.google.

Authoritative answers can be found from:

devasc@labvm:~$
```

### Шаг 3: Запросите домен, используя определенный DNS-сервер.
Введите `nslookup www.sut.ru 8.8.8.8`, чтобы определить IP-адрес домена в соответствии с DNS Google.
```shell
devasc@labvm:~$ nslookup www.sut.ru 8.8.8.8
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
Name:   www.sut.ru
Address: 195.208.187.23

devasc@labvm:~$

devasc@labvm:~$ nslookup practicum.yandex.ru 8.8.8.8
Server:         8.8.8.8
Address:        8.8.8.8#53

Non-authoritative answer:
Name:   practicum.yandex.ru
Address: 87.250.250.5
Name:   practicum.yandex.ru
Address: 2a02:6b8::313

devasc@labvm:~$
```

Обратите внимание, что при использовании этого метода сервер разрешил адрес на два разных IP-адреса, причем все они отличаются от предыдущего DNS-запроса. Эти серверы имеют разный кэш DNS-запросов practicum.yandex.ru.
