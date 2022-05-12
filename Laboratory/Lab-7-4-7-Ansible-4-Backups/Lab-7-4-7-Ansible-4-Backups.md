# Использование Ansible для резервного копирования и настройки устройства
## Цель лабораторной работы:
- Часть 1: Запуск виртуальных машин DEVASC и CSR1000v
- Часть 2: Настройка Ansible
- Часть 3: Ansible для резервного копирования конфигурации
- Часть 4: Ansible для настройки устройства

## Необходимые ресурсы:
- ПК с не менее чем 4 ГБ оперативной памяти 
- Virtual Box или VMWare
- DEVASC виртуальная машина
- CSR1000v виртуальная машина

## Порядок выполнения работы:
## Часть 1: Запуск виртуальных машин DEVASC и CSR1000v
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.
>
> Если вы еще не завершили лабораторную работу - Установка виртуальной машины CSR1000v, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину CSR1000v.

## Часть 2: Настройка Ansible
> В этой части мы настроим Ansible на запуск из определенного каталога.

### Шаг 1: Откройте каталог Ansible в VS Code.
Откройте VS Code
Нажмите File > Open Folder... и перейдите в папку /labs/devnet-src/ansible.
Нажмите OK
Два подкаталога для лабораторных работ Ansible теперь отображаются слева на панели EXPLORER для вашего удобства. Сейчас мы будем работать с каталогом ansible-csr1000v.

### Шаг 2: Отредактируйте файл Ansible inventory.
Ansible использует inventory файл под названием hosts, который содержит информацию об устройствах, используемых в сценариях Ansible. По умолчанию файл “инвентаризации” Ansible располагается в каталоге /etc/ansible/hosts, как указано в стандартном файле ansible.cfg в том же каталоге /etc/ansible. Эти файлы по умолчанию используются при глобальном запуске Ansible. Однако в этой лабораторной работе вы будете запускать Ansible из каталога ansible-csr1000v. Поэтому для каждой лаборатории вам понадобятся отдельные файлы hosts и ansible.cfg.

> Примечание: Термины hosts файл и inventory файл являются синонимами и будут использоваться как взаимозаменяемые.

Ansible inventory файл определяет устройства и группы устройств, которые используются программой воспроизведения Ansible. Файл может быть в одном из многих форматов, включая YAML и INI, в зависимости от вашей среды Ansible. Inventory файл может содержать список устройств по IP-адресу или полному доменному имени (FQDN), а также включать параметры, специфичные для конкретного хоста.

Откройте файл hosts в каталоге ansible-csr1000v.
Добавьте следующие строки в файл hosts и сохраните.
```shell
# Введите хосты или устройства для Ansible плейбуков
CSR1kv ansible_user=cisco ansible_password=cisco123! ansible_host=192.168.56.101
```
После комментария (#) файл hosts начинается с алиаса CSR1kv. Алиаса используется в плейбуке Ansible для ссылки на устройство. После алиаса в файле hosts указываются три переменные, которые будут использоваться плейбуком для доступа к устройству. Это учетные данные SSH, которые нужны Ansible для безопасного доступа к виртуальной машине CSR1000v.
- `ansible_user` - переменная, содержащая имя пользователя, используемое для подключения к удаленному устройству. Без этого будет использоваться пользователь, запускающий ansible-playbook.
- `ansible_password` - переменная, содержащая соответствующий пароль для ansible_user. Если не указано, будет использоваться SSH-ключ. 
- `ansible_host` - переменная, содержащая IP-адрес или FQDN устройства.

### Шаг 3: Отобразите версию Ansible и расположение ansible.cfg по умолчанию.
Чтобы увидеть, где Ansible хранит файл по умолчанию `ansible.cfg`, откройте окно терминала и перейдите на один каталог вверх к родительскому каталогу ansible.
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$ cd ..
devasc@labvm:~/labs/devnet-src/ansible$
Введите ansible, чтобы получить список команд ansible. Обратите внимание на опцию --version.
devasc@labvm:~/labs/devnet-src/ansible$ ansible
usage: ansible [-h] [--version] [-v] [-b] [--become-method BECOME_METHOD]
               [--become-user BECOME_USER] [-K] [-i INVENTORY] [--list-hosts]
               [-l SUBSET] [-P POLL_INTERVAL] [-B SECONDS] [-o] [-t TREE] [-k]
               [--private-key PRIVATE_KEY_FILE] [-u REMOTE_USER]
               [-c CONNECTION] [-T TIMEOUT]
               [--ssh-common-args SSH_COMMON_ARGS]
<вывод опущен>
devasc@labvm:~/labs/devnet-src/ansible$
```
Используйте команду `ansible --version` для отображения информации о версии.
```shell
devasc@labvm:~/labs/devnet-src/ansible$ ansible --version
ansible 2.9.9
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/devasc/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3/dist-packages/ansible
  executable location = /usr/bin/ansible
  python version = 3.8.2 (default, Apr 27 2020, 15:53:34) [GCC 9.3.0]
devasc@labvm:~/labs/devnet-src/ansible$
```

### Шаг 4: Отобразите файл по умолчанию ansible.cfg.
Файл `ansible.cfg` используется Ansible для установки определенных значений по умолчанию. Эти значения могут быть изменены. 
Используя путь по умолчанию, указанный в команде ansible --version, отобразите файл конфигурации по умолчанию. Обратите внимание, что это очень длинный файл, можно направить вывод команды cat в more, чтобы он отображал по одной странице за раз. Выделены записи, которые будут в вашем файле ansible.cfg для этой лабораторной работы.
```shell
devasc@labvm:~/labs/devnet-src/ansible$ cat /etc/ansible/ansible.cfg | more
# config file for ansible -- https://ansible.com/
# ===============================================

# nearly all parameters can be overridden in ansible-playbook
# or with command line flags. ansible will read ANSIBLE_CONFIG,
# ansible.cfg in the current working directory, .ansible.cfg in
# the home directory or /etc/ansible/ansible.cfg, whichever it
# finds first

[defaults]

# some basic default values...

#inventory      = /etc/ansible/hosts
<вывод опущен>

# uncomment this to disable SSH key host checking
#host_key_checking = False
<вывод опущен>

# retry files
# When a playbook fails a .retry file can be created that will be placed in ~/
# You can enable this feature by setting retry_files_enabled to True
# and you can change the location of the files by setting retry_files_save_path

#retry_files_enabled = False
<вывод опущен>
```
Обратите внимание, что Ansible показывает, что файл “инвентаризации” hosts, который он будет использовать по умолчанию, это /etc/ansible/hosts. В предыдущем шаге вы отредактировали файл инвентаризации hosts в каталоге ansible-csr1000v. На следующем шаге вы отредактируете новый файл ansible.cfg, который будет использовать созданный вами файл инвентаризации hosts.

### Шаг 5: Измените расположение файла ansible.cfg.
Ansible будет использовать файл конфигурации, расположенный в /etc/ansible/ansible.cfg, если в текущем каталоге нет файла ansible.cfg. Перейдите обратно в каталог ansible-csr1000v. В этой директории уже есть файл-плейсхолдер ansible.cfg. Выясните текущее местоположение файла ansible.cfg с помощью команды ansible --version.
```shell
devasc@labvm:~/labs/devnet-src/ansible$ cd ansible-csr1000v/
devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$ ansible --version
ansible 2.9.9
  config file = /home/devasc/labs/devnet-src/ansible/ansible-csr1000v/ansible.cfg
<вывод опущен>
devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$
```
Отобразите файл и увидите, что он пуст, за исключением комментария. Вы будете редактировать этот файл на следующем этапе.
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$ cat ansible.cfg 
# Add to this file for the Ansible lab
devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$
```

### Шаг 6: Отредактируйте файл ansible.cfg.
Теперь вам нужно отредактировать файл /ansible-csr1000v/ansible.cfg, указав в нем расположение файла инвентаризации hosts. Помните, что файл конфигурации по умолчанию в /etc/ansible/ansible.cfg использует файл инвентаризации в /etc/ansible/hosts.
Откройте файл /ansible-csr1000v/ansible.cfg в VS Code.
Вы можете удалить комментарий. Добавьте в файл следующие строки и сохраните его.
```shell
# Файл конфигурации для ansible-csr1000v 
[defaults]
# Использовать локальный файл hosts в этой папке
inventory=./hosts 
host_key_checking = False # Не беспокойтесь о RSA Fingerprints
retry_files_enabled = False # Не создавать retry файлы
deprecation_warnings = False # Не показывать предупреждения
```
Как и в Python, символ # используется для комментариев в файле ansible.cfg. Если запись ссылается на имя файла, например inventory=./hosts, комментарий не может идти после записи. Ansible рассматривает # и следующий за ним комментарий как часть имени файла. Поэтому в таких случаях комментарий # должен быть на отдельной строке. Однако переменные могут иметь комментарий в той же строке, как показано для host_key_checking и retry_files_enabled.

ansible.cfg указывает Ansible, где найти файл “инвентаризации”, и устанавливает определенные параметры по умолчанию. Информация, которую вы ввели в файл ansible.cfg, следующая:
- `inventory=./hosts` — Ваш файл инвентаризации; файл hosts в текущем каталоге.
- `host_key_checking = False` — В локальной среде разработки не установлены ключи SSH. Вы установили параметр host_key_checking в False, что является значением по умолчанию. В производственной сети значение параметра host_key_checking должно быть равно True.
- `retry_files_enabled = False` — Когда у Ansible возникают проблемы с запуском плейбуков для хоста, он выводит имя хоста в файл в текущем каталоге, заканчивающийся .retry. Чтобы избежать беспорядка, обычно этот параметр отключают.
- `deprecation_warnings = False` — Предупреждения об износе указывают на использование устаревших функций, которые планируется удалить в будущем выпуске Ansible. Вы отключили это предупреждение.

### Шаг 7: Резюме: Ваши файлы конфигурации Ansible.
В этой части мы настроили Ansible на запуск в каталоге ansible-csr1000v. По умолчанию Ansible использует файлы в каталоге /etc/ansible. Файл /etc/ansible/ansible.cfg по умолчанию указывает, что файл инвентаризации по умолчанию - /etc/ansible/hosts.
Однако в этой лабе нам понадобится файл hosts и ansible.cfg в каталоге ansible-csr1000v.
- Мы отредактировали файл hosts, чтобы он содержал информацию о логине и IP-адресе для маршрутизатора CSR1000v.
- Мы также отредактировали файл ansible.cfg, чтобы использовать локальный файл hosts в качестве файла инвентаризации (inventory=./hosts).
В следующей части мы создадим playbook, чтобы указать Ansible, что делать.

## Часть 3: Ansible для резервного копирования конфигурации
> В этой части мы создадим playbook Ansible, который автоматизирует процесс резервного копирования конфигурации CSR1000v. Плейбуки находятся в центре Ansible. Если вы хотите, чтобы Ansible получил информацию или выполнил действие на устройстве или группе устройств, вы запускаете playbook для выполнения работы.
> Плейбук Ansible — это YAML-файл, содержащий один или несколько plays.
> Playbook — термин, взятый из футбола. Обозначает книгу тренера, который там что-то записывает и задаёт сценарий игре. Плейбук — это оно и есть, список сценариев для запуска Ansible  
> Каждый play представляет собой набор задач.
> - play — это соответствующий набор задач для устройства или группы устройств. 
> - task (задача) — это одно действие, которое ссылается на модуль для запуска вместе с любыми входными аргументами и действиями. Эти задачи могут быть простыми или сложными в зависимости от необходимости разрешений, порядка выполнения задач и так далее.
>
> Playbook может также содержать роли. Роль — это механизм, позволяющий разбить учебник на несколько компонентов или файлов, что упрощает playbook и делает его более удобным для повторного использования. Например, общая роль используется для хранения задач, которые можно использовать во всех ваших плейбуках.
> 
> Ansible YAML Playbook включает в себя объекты, списки и модули.
> -	Объект YAML — одна или несколько пар ключ-значение. Пары разделяются двоеточием без использования кавычек, например, hosts: CSR1kv. 
> -	Объект может содержать другие объекты, например, список. В YAML используются списки или массивы. Для каждого элемента в списке используется знак "-". 
> -	Ansible поставляется с рядом модулей (называемых библиотекой модулей), которые могут быть выполнены непосредственно на удаленных хостах или через плейбуки. Примером может служить модуль ios_command, используемый для отправки команд на устройство IOS и возврата результатов. Каждая задача обычно состоит из одного или нескольких модулей Ansible.
>
> Вы запускаете Ansible playbook с помощью команды `ansible-playbook`, например:
> `ansible-playbook backup_zss_router_playbook.yaml -i hosts`
>
> Команда ansible-playbook использует следующие параметры:
> - Playbook, который вы хотите запустить (`backup_zss_router_playbook.yaml`) 
> - Файл инвентаризации и его расположение (-i hosts).

### Шаг 1: Создайте Ansible Playbook.
Ansible Playbook представляет собой YAML. Убедитесь, что вы используете правильный отступ в YAML. Каждый пробел и тире имеют значение. При копировании и вставке кода из этой лабораторной работы вы можете потерять форматирование.
В VS Code создайте новый файл в каталоге ansible-csr1000v со следующим именем: backup_cisco_router_playbook.yaml
Добавьте в файл следующую информацию.
```yaml
---
- name: AUTOMATIC BACKUP OF RUNNING-CONFIG
  hosts: CSR1kv
  gather_facts: false
  connection: local
 
  tasks:
   - name: DISPLAYING THE RUNNING-CONFIG
     ios_command:
       commands:
         - show running-config  
     register: config
 
   - name: SAVE OUTPUT TO ./backups/
     copy:
       content: "{{ config.stdout[0] }}"
       dest: "backups/show_run_{{ inventory_hostname }}.txt"
```

### Шаг 2: Изучите свой Ansible playbook.
Созданный вами playbook содержит один play с двумя задачами.  Ниже приводится пояснение к нему:
-	`---` находится в начале каждого файла YAML, что указывает YAML на то, что это отдельный документ. Каждый файл может содержать несколько документов, разделенных символом `---`.
-	`name: AUTOMATIC BACKUP OF RUNNING-CONFIG` — название play.
-	`hosts: CSR1kv` — алиас ранее настроенного файла hosts. Ссылаясь на него в вашем плейбуке, плейбук может использовать все параметры, связанные с этой записью файла инвентаризации, которая включает имя пользователя, пароль и IP-адрес устройства. 
-	`gather_facts: false` — Ansible изначально был разработан для работы с серверами Linux, копируя модули Python на серверы для автоматизации задач. Это не обязательно при работе с сетевыми устройствами.
-	`connection: local` — Указывает, что вы не используете SSH, поэтому соединение является локальным.
-	`tasks:` — Это ключевое слово указывает на одну или несколько задач, которые необходимо выполнить.

Первая задача — отобразить running-config.
-	`- name: DISPLAYING THE RUNNING-CONFIG` — имя задачи.
-	`ios_command:` — модуль Ansible, который используется для отправки команд на устройство IOS и возврата результатов, считанных с устройства. Однако он не поддерживает команды конфигурации. Для этой цели используется модуль ios_config, как вы увидите в следующей части этой лабораторной работы.

> Примечание: В терминале Linux вы можете использовать команду ansible-doc имя_модуля для просмотра страниц руководства для любого модуля и параметров, связанных с этим модулем. (например, ansible-doc ios_command)

-	`commands:` — параметр связан с модулем ios_command. Он используется для перечисления команд IOS в плейбуке, которые должны быть отправлены на удаленное устройство IOS. Возвращается результирующий вывод команды. 
-	`- show running-config` — команда Cisco IOS, отправленная с помощью модуля ios_command.
-	`register: config` — Ansible включает регистры, используемые для фиксации вывода задачи в переменную. Эта запись указывает, что вывод предыдущей команды show running-config будет сохранен в переменной config.

Вторая задача - сохранить вывод:
- `name: SAVE OUTPUT TO ./backups/` — имя задачи.
- `copy:` - Это модуль Ansible, используемый для копирования файлов в удаленное место. С этим модулем связаны два параметра:
  - `content: "{{ config.stdout[0] }}"` — Указанное значение для этого параметра — это данные, хранящиеся в переменной config, переменной регистра Ansible, использованной в предыдущей задаче. Стандартный вывод (stdout) — это дескриптор файла по умолчанию, куда процесс может записывать вывод, используемый в Unix-подобных операционных системах, таких как Linux и Mac OS X.
  - `dest: "backups/show_run_{{ inventory_hostname }}.txt"` — Это путь и имя файла, куда должен быть скопирован файл. Переменная inventory_hostname — это "магическая переменная" Ansible, которая автоматически получает имя хоста, настроенное в файле hosts. В вашем случае, напомню, это CSR1kv. Этот параметр приводит к созданию файла show_run_CSR1kv.txt, хранящегося в каталоге backups. Этот файл будет содержать вывод команды show running-config. Вы создадите каталог backups на следующем шаге.

### Шаг 3: Запустите Ansible backup Playbook.
В Части 1 вы запустили виртуальную машину CSR1000v. Выполните Ping, чтобы убедиться, что вы можете получить к ней доступ. Введите Ctrl+ C, чтобы прервать пинг.
```shell
devasc@labvm:~/labs/devnet-src/ansible$ ping 192.168.56.101
PING 192.168.56.101 (192.168.56.101) 56(84) bytes of data.
64 bytes from 192.168.56.101: icmp_seq=1 ttl=63 time=0.913 ms
64 bytes from 192.168.56.101: icmp_seq=2 ttl=63 time=0.875 ms
^C
--- 192.168.56.101 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.875/0.894/0.913/0.019 ms
devasc@labvm:~/labs/devnet-src/ansible$ 
```
Создайте каталог backups. Как указано в последней строке вашего плейбука, это каталог, в котором будет храниться резервный файл конфигурации.
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$ mkdir backups
```
Теперь вы можете запустить Ansible playbook с помощью команды ansible-playbook:
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$ ansible-playbook backup_cisco_router_playbook.yaml

PLAY [AUTOMATIC BACKUP OF RUNNING CONFIG] *****************************************

TASK [DISPLAYING THE RUNNING-CONFIG] **********************************************
ok: [CSR1kv]

TASK [SAVE OUTPUT TO ./backups/] **************************************************
changed: [CSR1kv]

PLAY RECAP ************************************************************************
CSR1kv : ok=2  changed=1  unreachable=0  failed=0 skipped=0 rescued=0  ignored=0 

devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$
```
> Примечание: Во многих примерах вы увидите запуск плейбука с использованием опции -i inventory-filename. Например:
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$ ansible-playbook backup_cisco_router_playbook.yaml -i hosts
```
Этот параметр указывает Ansible местоположение и имя файла инвентаризации, список устройств, которые будет использовать плейбук. Этот параметр не нужен, поскольку вы настроили имя и расположение файла инвентаризации в локальном файле ansible.cfg: inventory=./hosts. Вы можете использовать опцию -i inventory-filename, чтобы переопределить информацию в файле ansible.cfg.

В PLAY RECAP должно появиться сообщение ok=2 changed=1, указывающее на успешное выполнение игровой книги.
Если ваш Ansible playbook не работает, вот некоторые вещи, которые следует проверить:
- Убедитесь, что ваши файлы hosts и ansible.cfg корректны.
- Убедитесь в правильности отступов в YAML.
- Убедитесь в правильности команды IOS.
- Проверьте весь синтаксис книги воспроизведения Ansible.
- Убедитесь, что вы можете пинговать CSR1000v.

Если проблемы всё ещё есть:
- Попробуйте вводить по одной строке за раз и каждый раз запускать playbook.
- Сравните ваш файл с playbook в каталоге ansible_solutions

### Шаг 4: Убедитесь, что файл резервной копии создан.
В VS Code откройте папку backups и откройте файл show_run_CSR1kv.txt. Вы также можете использовать окно терминала, чтобы открыть файл с помощью cat backups/show_run_CSR1kv.txt. Теперь у вас есть резервная копия конфигурации CSR1000v.
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$ cat backups/show_run_CSR1kv.txt
Building configuration...

Current configuration : 3915 bytes
!
! Last configuration change at 20:54:52 UTC Mon May 9 2022
!
version 16.9
service timestamps debug datetime msec
service timestamps log datetime msec
platform qfp utilization monitor load 80
no platform punt-keepalive disable-kernel-core
platform console virtual
!
hostname CSR1kv
!
<вывод опущен>
```

## Часть 4: Использование Ansible для настройки устройства
В этой части вы создадите ещё один Ansible playbook для настройки IPv6 адресации на маршрутизаторе CSR1000v.

### Шаг 1: Просмотрите файл инвентаризации хостов.
Пересмотрите файл инвентаризации хостов. Напоминаю, что этот файл содержит псевдоним CSR1kv и три инвентаризационные переменные для имени пользователя, пароля и IP-адреса хоста. Руководство по выполнению этой части также будет использовать этот файл и файл ansible.cfg, который вы создали в начале лабораторной работы.
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$ cat hosts
# Введите хосты или устройства для Ansible плейбуков
CSR1kv ansible_user=cisco ansible_password=cisco123! ansible_host=192.168.56.101
devasc@labvm:~/labs/devnet-src/ansible$
```

### Шаг 2: Создайте новый playbook.
В VS Code создайте новый файл в каталоге ansible-csr1000v со следующим именем: cisco_router_ipv6_config_playbook.yaml
Добавьте в файл следующую информацию. Убедитесь, что вы используете правильный отступ в YAML. Каждый пробел и тире имеют значение. При копировании и вставке вы можете потерять часть форматирования.
```yaml
---
- name: CONFIGURE IPv6 ADDRESSING
  hosts: CSR1kv
  gather_facts: false
  connection: local

  tasks:
   - name: SET IPv6 ADDRESS 
     ios_config:
       parents: "interface GigabitEthernet1"
       lines:
         - description IPv6 ADDRESS 
         - ipv6 address 2001:db8:acad:1::1/64
         - ipv6 address fe80::1:1 link-local

   - name: SHOW IPv6 INTERFACE BRIEF 
     ios_command:
       commands:
         - show ipv6 interface brief
     register: output

   - name: SAVE OUTPUT ./ios_configurations/
     copy: 
       content: "{{ output.stdout[0] }}"
       dest: "ios_configurations/IPv6_output_{{ inventory_hostname }}.txt"
```

### Шаг 3: Изучите Ansible playbook.
Многое в этом плейбуке похоже на тот, что мы создали в предыдущей части. Основным отличием является первая задача SET IPv6 ADDRESS.
Ниже приводится краткое описание элементов задания:
- `ios_config:` — модуль Ansible, используемый для конфигурирования устройства IOS. Вы можете использовать команду ansible-doc ios_config для просмотра подробной информации о родительских параметрах и параметрах линий, используемых в этом плейбуке.
- `parents: "interface GigabitEthernet1"` — параметр указывает на режим конфигурации интерфейса IOS.
- `lines:` — В этом разделе настраивается упорядоченный набор команд IOS, определяющий информацию об адресации IPv6 для интерфейса GigabitEthernet1.

Остальная часть плейбука аналогична задачам из предыдущей части. Вторая задача использует модуль ios_command и команду show ipv6 interface brief для отображения вывода и отправки его в регистр вывода.

Последняя задача сохраняет информацию в выводе регистра в файл IPv6_output_CSR1kv.txt в подкаталоге ios_configurations.

### Шаг 4: Запустите Ansible playbook для настройки IPv6 адресации на виртуальной машине CSR1000v.
В Части 1 вы запустили виртуальную машину CSR1000v. Выполните Ping, чтобы убедиться, что вы можете получить к ней доступ. Введите Ctrl+ C, чтобы прервать пинг.
```shell
devasc@labvm:~/labs/devnet-src/ansible$ ping 192.168.56.101
PING 192.168.56.101 (192.168.56.101) 56(84) bytes of data.
64 bytes from 192.168.56.101: icmp_seq=1 ttl=63 time=0.913 ms
64 bytes from 192.168.56.101: icmp_seq=2 ttl=63 time=0.875 ms
^C
--- 192.168.56.101 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.875/0.894/0.913/0.019 ms
devasc@labvm:~/labs/devnet-src/ansible$ 
```

Создайте каталог ios_configurations. Как указано в последней строке вашего плейбука, это каталог, в котором будет храниться вывод команды show ipv6 interface brief.
```shell
devasc@labvm:~/labs/devnet-src/ansible$ mkdir ios_configurations
```
Теперь вы можете запустить Ansible playbook с помощью команды ansible-playbook. Опцию -v verbose можно использовать для отображения задач, выполняемых в плейбуке.
```shell
devasc@labvm:~/labs/devnet-src/ansible$ ansible-playbook -v cisco_router_ipv6_config_playbook.yaml
Using /home/devasc/labs/ansible-csr1000v/ansible.cfg as config file

PLAY [CONFIGURE IPv6 ADDRESSING] ***********************************************

TASK [SET IPv6 ADDRESS] ********************************************************
changed: [CSR1kv] => {"ansible_facts": {"discovered_interpreter_python": "/usr/bin/python3"}, "banners": {}, "changed": true, "commands": ["interface GigabitEthernet1", "description IPv6 ADDRESS", "ipv6 address 2001:db8:acad:1::1/64", "ipv6 address fe80::1:1 link-local"], "updates": ["interface GigabitEthernet1", "description IPv6 ADDRESS", "ipv6 address 2001:db8:acad:1::1/64", "ipv6 address fe80::1:1 link-local"]}

TASK [SHOW IPv6 INTERFACE BRIEF] ***********************************************
ok: [CSR1kv] => {"changed": false, "stdout": ["GigabitEthernet1       [up/up]\n    FE80::1:1\n    2001:DB8:ACAD:1::1"], "stdout_lines": [["GigabitEthernet1       [up/up]", "    FE80::1:1", "    2001:DB8:ACAD:1::1"]]}

TASK [SAVE OUTPUT ./ios_configurations/] ***************************************
ok: [CSR1kv] => {"changed": false, "checksum": "60784fbaae4bd825b7d4f121c450effe529b553c", "dest": "ios_configurations/IPv6_output_CSR1kv.txt", "gid": 900, "group": "devasc", "mode": "0664", "owner": "devasc", "path": "ios_configurations/IPv6_output_CSR1kv.txt", "size": 67, "state": "file", "uid": 900}

PLAY RECAP *********************************************************************
CSR1kv                     : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
devasc@labvm:~/labs/devnet-src/ansible$ 
```
При первом запуске учебника в PLAY RECAP должно отобразиться ok=3 changed=2 и failed=0, что указывает на успешное выполнение. Эти значения могут отличаться, если вы запустите учебник снова.

### Шаг 5: Убедитесь, что файл вывода создан.
В VS Code откройте папку ios_configurations и щелкните файл IPv6_output_CSR1kv.txt. Вы также можете использовать окно терминала для просмотра файла с помощью команды cat ios_configurations/IPv6_output_CSR1kv.txt. Теперь у вас есть резервная копия конфигурации CSR1000v.
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-csr1000v$ cat ios_configurations/IPv6_output_CSR1kv.txt 
GigabitEthernet1       [up/up]
    FE80::1:1
    2001:DB8:ACAD:1::1
devasc@labvm:~/labs/ansible-csr1000v/ios_configurations$
```