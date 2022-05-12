# Использование Ansible для автоматизации установки веб-сервера
## Цель лабораторной работы:
- Часть 1: Запуск виртуальной машины DEVASC
- Часть 2: Настройка Ansible
- Часть 3: Проверка связи с локальным веб-сервером
- Часть 4: Ansible Playbooks для автоматизации установки веб-сервера
- Часть 5: Добавление опций в Ansible Playbook для Apache Web Servers

## Необходимые ресурсы:
- ПК с не менее чем 4 ГБ оперативной памяти 
- Virtual Box или VMWare
- DEVASC виртуальная машина

## Порядок выполнения работы:
## Часть 1: Запуск виртуальных машин DEVASC
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.

## Часть 2: Настройка Ansible
> В виртуальной машине DEVASC предустановленны фиктивные IPv4 адреса, которые можно использовать для различных ситуаций и моделирования. В этой части мы настроим Ansible на использование одного из фиктивных IPv4-адресов для локального веб-сервера.

### Шаг 1: Откройте терминал в DEVASC-LABVM.
Сервер SSH отключен в DEVASC-LABVM, наряду с другими службами, которые обычно не требуются. Запустите его с помощью следующей команды.
```shell
devasc@labvm:~$ sudo systemctl start ssh
devasc@labvm:~$
```
Примечание: Сервер SSH и утилита sshpass уже установлены на виртуальной машине. Для справки, они устанавливаются с помощью следующих команд:

**Установка SSH**
```shell
devasc@labvm:~$ sudo apt-get install openssh-server
```
**Установка sshpass**
```shell
devasc@labvm:~$ sudo apt-get install sshpass
```

### Шаг 3: Откройте каталог ansible в VS Code.
Откройте VS Code.
Нажмите File > Open Folder… и перейдите в каталог /labs/devnet-src/ansible.
Нажмите OK.
Два подкаталога для лабораторных работ Ansible теперь отображаются слева на панели EXPLORER для вашего удобства. Сейчас мы будем работать с каталогом ansible-apache.

### Шаг 4: Отредактируйте файл инвентаризации Ansible
Откройте файл hosts в каталоге ansible-apache.
Добавьте следующие строки в файл hosts и сохраните.
```shell
[webservers]
192.0.2.3 ansible_ssh_user=devasc ansible_ssh_pass=Cisco123!
devasc и Cisco123! являются учетными данными администратора для виртуальной машины DEVASC. IPv4-адрес, который вы будете использовать для этой лабораторной работы, - 192.0.2.3. Это статический IPv4-адрес на ВМ под интерфейсом dummy0, как показано в выводе команды ip addr.
devasc@labvm:~/labs/devnet-src/ansible$ ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:97:ae:11 brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic enp0s3
       valid_lft 45882sec preferred_lft 45882sec
    inet6 fe80::a00:27ff:fe97:ae11/64 scope link 
       valid_lft forever preferred_lft forever
3: dummy0: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN group default qlen 1000
    link/ether a6:44:a7:e8:6a:9e brd ff:ff:ff:ff:ff:ff
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
    inet6 fe80::a444:a7ff:fee8:6a9e/64 scope link 
       valid_lft forever preferred_lft forever
devasc@labvm:~/labs/devnet-src/ansible$
```

### Шаг 5: Отредактируйте файл ansible.cfg.
Вы можете удалить комментарий. Добавьте в файл следующие строки и сохраните его. Файл ansible.cfg указывает Ansible, где найти файл инвентаризации, и устанавливает некоторые параметры по умолчанию.
```shell
# Файл конфигурации для ansible-apache
[defaults]
# Использовать локальный файл hosts в этой папке
inventory=./hosts 
# Не беспокойтесь о RSA Fingerprints
host_key_checking = False 
# Не создавать retry файлы
retry_files_enabled = False 
```

## Часть 3: Проверка связи с локальным веб-сервером
> В этой части мы проверим, что Ansible может отправлять команды на локальный веб-сервер.

### Шаг 1: Используйте модуль ping, чтобы проверить, что Ansible может выполнить ping веб-сервера.
Используйте модуль Ansible ping для проверки связи с устройствами, перечисленными в группе webservers вашего файла инвентаризации hosts.
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$ ansible webservers -m ping
192.0.2.3 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    },
    "changed": false,
    "ping": "pong"
}
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$
```

### Шаг 2: Используйте командный модуль для проверки того, что Ansible может взаимодействовать с веб-сервером.
Используйте командный модуль Ansible для проверки связи с устройствами, перечисленными в группе webservers инвентарного файла hosts. В этом примере мы отправим аргумент -a "/bin/echo hello world", чтобы попросить локальный веб-сервер ответить "hello world".
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$ ansible webservers -m command -a "/bin/echo hello world"
192.0.2.3 | CHANGED | rc=0 >>
hello world
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$
```

## Часть 4: Создание Ansible Playbooks для автоматизации установки веб-сервера
> В этой части мы создадим два Ansible плейбука. Первый плейбук будет автоматизировать эхо-тест, который мы проводили в предыдущей части. Представьте, что вы подключаете сотню вебсерверов. Группа [webserver] в файле hosts будет содержать всю необходимую информацию для каждого веб-сервера. Затем вы можете использовать простую программу для проверки связи со всеми этими серверами с помощью одной команды. Во втором плейбуке мы создадим и автоматизируем установку программного обеспечения веб-сервера Apache.

### Шаг 1: Создайте Ansible плейбук для тестирования группы веб-серверов.
В этом шаге вы создадите плейбук для выполнения той же команды echo.
В VS Code создайте новый файл в каталоге ansible-apache со следующим именем: test_apache_playbook.yaml
Добавьте в файл следующую информацию. Убедитесь, что используете правильный отступ в YAML. Каждый пробел и тире имеют значение. При копировании и вставке вы можете потерять часть форматирования.
```yaml
---
- hosts: webservers
  tasks:
    - name: run echo command
      command: /bin/echo hello world
```

### Шаг 2: Запустите Ansible playbook для тестирования группы веб-серверов.
Запустите игровой учебник Ansible с помощью команды ansible-playbook, используя опцию -v verbose. Вы должны увидеть вывод, похожий на следующий.
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$ ansible-playbook -v test_apache_playbook.yaml
Using /home/devasc/labs/ansible/ansible-apache/ansible.cfg as config file

PLAY [webservers] **************************************************************

TASK [Gathering Facts] *********************************************************
ok: [192.0.2.3]

TASK [run echo command] ********************************************************
changed: [192.0.2.3] => {"changed": true, "cmd": ["/bin/echo", "hello", "world"], "delta": "0:00:00.002062", "end": "2022-05-10 17:31:36.832442", "rc": 0, "start": "2022-05-10 17:31:36.82839", "stderr": "", "stderr_lines": [], "stdout": "hello world", "stdout_lines": ["hello world"]}

PLAY RECAP *********************************************************************
192.0.2.3                  : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$ 
```

### Шаг 3: Создайте Ansible playbook для установки Apache.
В VS Code создайте новый файл в каталоге ansible-apache со следующим именем: install_apache_playbook.yaml
Добавьте в файл следующую информацию. Убедитесь, что вы используете правильный отступ в YAML. Каждый пробел и тире имеют значение. При копировании и вставке вы можете потерять некоторые форматирования. 
```yaml
---
- hosts: webservers
  become: yes
  tasks:
    - name: INSTALL APACHE2
      apt: name=apache2 update_cache=yes state=latest
 
    - name: ENABLED MOD_REWRITE
      apache2_module: name=rewrite state=present
      notify:
        - RESTART APACHE2
 
  handlers:
    - name: RESTART APACHE2
      service: name=apache2 state=restarted 
```

### Шаг 4: Изучите свой Ansible playbook.
Ниже приводится объяснение некоторых важных строк в плейбуке:
- `hosts: webservers` — ссылка на группу устройств webservers в файле инвентаризации hosts. Эта программа будет запущена для всех устройств с этой группой.
- `become: yes` — ключевое слово become активирует выполнение команд sudo, что позволит выполнять такие задачи, как установка приложений.
- `apt:` — модуль apt используется для управления пакетами и установкой приложений в Linux.
- `handlers:` — обработчики похожи на задачи, но не выполняются автоматически. Они вызываются задачей. Обратите внимание, что задача ENABLED MOD_REWRITE вызывает обработчик RESTART APACHE2.

### Шаг 5: Запустите резервное копирование Ansible для установки Apache.
Запустите Ansible playbook с помощью, как это ни странно, команды ansible-playbook с опцией -v verbose. При первой установке Apache на вашей виртуальной машине задача INSTALL APACHE2 займет от 30 секунд до нескольких минут в зависимости от скорости вашего интернета.
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$ ansible-playbook -v install_apache_playbook.yaml
Using /home/devasc/labs/ansible/ansible-apache/ansible.cfg as config file

PLAY [webservers] **************************************************************

TASK [Gathering Facts] *********************************************************
ok: [192.0.2.3]

TASK [INSTALL APACHE2] *********************************************************
ok: [192.0.2.3] => {"cache_update_time": 1590010855, "cache_updated": true, "changed": false}

TASK [ENABLED MOD_REWRITE] *****************************************************
ok: [192.0.2.3] => {"changed": false, "result": "Module rewrite enabled"}

PLAY RECAP *********************************************************************
192.0.2.3   : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
=
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$
```
В PLAY RECAP должно отобразиться ok и failed=0, что свидетельствует об успешном выполнении плейбука. 

### Шаг 6: Убедитесь, что Apache был установлен.
Используйте следующую команду, чтобы проверить, что Apache теперь установлен. Нажмите "q", чтобы выйти из системы.
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$ sudo systemctl status apache2
● apache2.service - The Apache HTTP Server
     Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor prese>
     Active: active (running) since Tue 2022-05-10 17:35:51 UTC; 4min 1s ago
       Docs: https://httpd.apache.org/docs/2.4/
    Process: 5343 ExecStart=/usr/sbin/apachectl start (code=exited, status=0/SU>
   Main PID: 5368 (apache2)
      Tasks: 55 (limit: 4628)
     Memory: 5.3M
     CGroup: /system.slice/apache2.service
             ├─5368 /usr/sbin/apache2 -k start
             ├─5369 /usr/sbin/apache2 -k start
             └─5370 /usr/sbin/apache2 -k start
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$
```
Откройте веб-браузер Chromium и введите IPv4-адрес вашего нового сервера, 192.0.2.3, чтобы увидеть веб-страницу Apache2 по умолчанию.

## Часть 5: Добавление опций в Ansible Playbook для веб-серверов Apache
> В продакшене стандартная установка Apache2 обычно настраивается с учетом специфических функций, необходимых организации. Ansible playbook может помочь автоматизировать и эти задачи по настройке. В этой части вы настроите плейбук, указав, что сервер Apache должен использовать другой номер порта.

### Шаг 1: Создайте Ansible Playbook для добавления опций Apache.
В VS Code создайте новый файл в каталоге ansible-apache со следующим именем: install_apache_options_playbook.yaml
Добавьте в файл следующую информацию. Убедитесь, что вы используете правильный отступ в YAML. Каждый пробел и тире имеют значение. При копировании и вставке вы можете потерять часть форматирования.
```yaml
---
- hosts: webservers
  become: yes
  tasks:
   - name: INSTALL APACHE2
     apt: name=apache2 update_cache=yes state=latest
 
   - name: ENABLED MOD_REWRITE
     apache2_module: name=rewrite state=present
     notify:
       - RESTART APACHE2
 
   - name: APACHE2 LISTEN ON PORT 8081
     lineinfile: dest=/etc/apache2/ports.conf regexp="^Listen 80" line="Listen 8081" state=present
     notify:
       - RESTART APACHE2
 
   - name: APACHE2 VIRTUALHOST ON PORT 8081
     lineinfile: dest=/etc/apache2/sites-available/000-default.conf regexp="^<VirtualHost \*:80>" line="<VirtualHost *:8081>" state=present
     notify:
       - RESTART APACHE2
 
  handlers:
   - name: RESTART APACHE2
     service: name=apache2 state=restarted
```
Этот плейлист очень похож на предыдущий с добавлением двух заданий, которые заставляют веб-серверы слушать порт 8081 вместо порта 80. 
Модуль lineinfile используется для замены существующих строк в файлах /etc/apache2/ports.conf и /etc/apache2/sites-available/000-default.conf. Дополнительную информацию о модуле lineinfile можно найти в документации Ansible.

### Шаг 2: Изучите два файла, которые будут изменены плейбуком.
Просмотрите файлы /etc/apache2/ports.conf и /etc/apache2/sites-available/000-default.conf. Обратите внимание, что веб-сервер в настоящее время прослушивает порт 80.
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$ cat /etc/apache2/ports.conf
# If you just change the port or add more ports here, you will likely also
# have to change the VirtualHost statement in
# /etc/apache2/sites-enabled/000-default.conf

Listen 80

<IfModule ssl_module>
        Listen 443
<вывод опущен>

devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$ cat /etc/apache2/sites-available/000-default.conf
<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
<вывод опущен>
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$
```

### Шаг 3: Запустите Ansible Playbook.
Запустите Ansible playbook с помощью команды ansible-playbook.
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$ ansible-playbook install_apache_options_playbook.yaml

PLAY [webservers] **************************************************************

TASK [Gathering Facts] *********************************************************
ok: [192.0.2.3]

TASK [INSTALL APACHE2] *********************************************************
ok: [192.0.2.3]

TASK [ENABLED MOD_REWRITE] *****************************************************
ok: [192.0.2.3]

TASK [APACHE2 LISTEN ON PORT 8081] *********************************************
ok: [192.0.2.3]

TASK [APACHE2 VIRTUALHOST ON PORT 8081] ****************************************
ok: [192.0.2.3]

PLAY RECAP *********************************************************************
192.0.2.3                  : ok=6    changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$ 
```

### Шаг 4: Убедитесь, что Apache был установлен.
Просмотрите файлы /etc/apache2/ports.conf и /etc/apache2/sites-available/000-default.conf еще раз. Заметьте, что плейбук изменил эти файлы, чтобы прослушивать порт 8081.
```shell
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$ cat /etc/apache2/ports.conf
# If you just change the port or add more ports here, you will likely also
# have to change the VirtualHost statement in
# /etc/apache2/sites-enabled/000-default.conf

Listen 8081

<IfModule ssl_module>
        Listen 443
</IfModule>

<IfModule mod_gnutls.c>
        Listen 443
</IfModule>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$ 

devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$ cat /etc/apache2/sites-available/000-default.conf
<VirtualHost *:8081>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
<вывод опущен>
devasc@labvm:~/labs/devnet-src/ansible/ansible-apache$
```
Откройте веб-браузер Chromium и введите IPv4-адрес вашего нового сервера. Но на этот раз укажите 8081 в качестве номера порта, 192.0.2.3:8081, чтобы увидеть веб-страницу Apache2 по умолчанию.
> Примечание: Хотя в файле ports.conf видно, что Apache2 также прослушивает порт 443, он предназначен для HTTPS, конечно же её можно добавить в плейбук, однако в данной лабораторной это будет избыточным.
