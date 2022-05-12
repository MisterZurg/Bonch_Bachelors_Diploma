# Знакомство c Linux
![Иллюстрация к работе](../Resourses/README-LR-1-2-2.png)
## Цель лабораторной работы:
- Часть 1: Запуск виртуальной машины DEVASC
- Часть 2: Обзор навигации по синтаксису команд
- Часть 3: Обзор управления файлами
- Часть 4: Обзор регулярных выражений
- Часть 5: Обзор системного администрирования
 
## Необходимые ресурсы
- 1 ПК
- Virtual Box или VMWare
- DEVASC виртуальная машина

## Порядок выполнения работы
## Часть 1: Запуск DEVASC VM
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.

## Часть 2: Обзор навигации по синтаксису команд
> В этой части вы будете использовать команды ls, pwd, cd и sudo для изучения базового синтаксиса команд.

### Шаг 1: Откройте терминал в DEVASC-LABVM
Дважды щелкните значок эмулятора терминала на рабочем столе, чтобы открыть окно терминала.

### Шаг 2: Навигация по директориям
Используйте команду ls для отображения файлов в текущем каталоге. Помните, что команды чувствительны к регистру
```shell
devasc@labvm:~$ ls
Desktop    Downloads  Music     Public  Templates
Documents  labs       Pictures  snap    Videos
devasc@labvm:~$
```
Используйте команду ls с аргументом labs, чтобы отобразить содержимое папки labs.
```shell
devasc@labvm:~$ ls labs
devnet-src
devasc@labvm:~$
```

Используйте команду ls с опцией -l для отображения "длинном формате" содержимого текущего каталога.
```shell
devasc@labvm:~$ ls -l
total 40
drwxr-xr-x 2 devasc devasc 4096 Mar 30 21:25 Desktop
drwxr-xr-x 2 devasc devasc 4096 Apr 15 19:09 Documents
drwxr-xr-x 2 devasc devasc 4096 Apr 15 19:09 Downloads
drwxr-xr-x 5 devasc devasc 4096 Mar 30 21:21 labs
drwxr-xr-x 2 devasc devasc 4096 Apr 15 19:09 Music
drwxr-xr-x 2 devasc devasc 4096 Apr 15 19:09 Pictures
drwxr-xr-x 2 devasc devasc 4096 Apr 15 19:09 Public
drwxr-xr-x 5 devasc devasc 4096 Mar 30 21:24 snap
drwxr-xr-x 2 devasc devasc 4096 Apr 15 19:09 Templates
drwxr-xr-x 2 devasc devasc 4096 Apr 15 19:09 Videos
devasc@labvm:~$
```
Используйте команду ls с опцией -r для отображения содержимого текущего каталога в обратном алфавитном порядке.
```shell
devasc@labvm:~$ ls -r
Videos     snap    Pictures  labs       Documents
Templates  Public  Music     Downloads  Desktop
devasc@labvm:~$
```
Одновременно можно использовать несколько опций. Используйте команду ls с опциями -l и -r для отображения содержимого текущего каталога как в прямом, так и в обратном порядке.
```shell
devasc@labvm:~$ ls -lr
total 40
drwxr-xr-x 2 devasc devasc 4096 Apr 15 19:09 Videos
drwxr-xr-x 2 devasc devasc 4096 Apr 15 19:09 Templates
drwxr-xr-x 5 devasc devasc 4096 Mar 30 21:24 snap
drwxr-xr-x 2 devasc devasc 4096 Apr 15 19:09 Public
drwxr-xr-x 2 devasc devasc 4096 Apr 15 19:09 Pictures
drwxr-xr-x 2 devasc devasc 4096 Apr 15 19:09 Music
drwxr-xr-x 5 devasc devasc 4096 Mar 30 21:21 labs
drwxr-xr-x 2 devasc devasc 4096 Apr 15 19:09 Downloads
drwxr-xr-x 2 devasc devasc 4096 Apr 15 19:09 Documents
drwxr-xr-x 2 devasc devasc 4096 Mar 30 21:25 Desktop
devasc@labvm:~$
```
Существует множество других опций, которые можно использовать с командой ls. Используйте команду man с аргументом ls, чтобы посмотреть на все возможности в руководстве. Команду man можно использовать для поиска любой команды в системе. Для перехода к последующим экранам используйте пробел. Нажмите q, чтобы выйти из системы.
```shell
devasc@labvm:~$ man ls
(The command line disappears and the manual page for ls opens.)
LS(1)                            User Commands                           LS(1)

NAME
       ls - list directory contents
SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List  information  about  the FILEs (the current directory by default).
       Sort entries alphabetically if none of -cftuvSUX nor --sort  is  speci‐
       fied.

       Mandatory  arguments  to  long  options are mandatory for short options
       too.

       -a, --all
              do not ignore entries starting with .

       -A, --almost-all
              do not list implied . and ..

       --author
 Manual page ls(1) line 1 (press h for help or q to quit)
```
Вы также можете использовать аргумент --help после большинства команд, чтобы увидеть краткое описание всех доступных опций команды.
```shell
devasc@labvm:~$ ls --help
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options too.
  -a, --all                  do not ignore entries starting with .
  -A, --almost-all           do not list implied . and ..
 (полный вывод опущен)
devasc@labvm:~$
```
Используйте команду pwd для отображения текущей рабочей директории
```shell
devasc@labvm:~$ pwd
/home/devasc
devasc@labvm:~$
```
С помощью команды cd измените каталог на /home/devasc/Documents. 
```shell
devasc@labvm:~$ cd Documents
devasc@labvm:~/Documents$
```
Используйте команду cd с символом / для смены каталога на корневой каталог. Снова используйте команду pwd, чтобы убедиться, что вы теперь находитесь в корневом каталоге.
```shell
devasc@labvm:~/Documents$ cd /
devasc@labvm:/$ pwd
/
devasc@labvm:/$
```
Вернитесь в каталог /home/devasc/Documents

_Совет: Вы можете перемещатьcя по одному каталогу за раз или по всему пути до пункта назначения. Чтобы быстро ввести команду, наберите первые несколько букв имени каталога и нажмите Tab, чтобы система автоматически ввела остальную часть имени. Помните, что имена чувствительны к регистру._
```shell
devasc@labvm:/$ cd /home/devasc/Documents/
devasc@labvm:~/Documents$
```
Используйте символы .. для перемещения вверх на один каталог. Снова используйте pwd, чтобы убедиться, что вы вернулись в домашний каталог пользователя.
```shell
devasc@labvm:~/Documents$ cd ..
devasc@labvm:~$ pwd
/home/devasc
devasc@labvm:~$
```
### Шаг 3: Используйте команды суперпользователя для административного доступа.
Используйте команду sudo, чтобы выполнить одну команду от имени пользователя root. При этом новый терминал не будет создан. Используйте команду sudo apt-get update для обновления списка доступных пакетов, установленных на ВМ. Эта команда не будет работать без использования команды sudo.
> Примечание: Ваш output, скорее всего, будет отличаться.
```shell
devasc@labvm:~$ sudo apt-get update
Get:1 http://security.ubuntu.com/ubuntu focal-security InRelease [97.9 kB]
Get:2 http://us.archive.ubuntu.com/ubuntu focal InRelease [265 kB]
Get:3 http://us.archive.ubuntu.com/ubuntu focal-updates InRelease [89.1 kB]    
Get:4 http://us.archive.ubuntu.com/ubuntu focal-backports InRelease [89.2 kB]  
Get:5 http://us.archive.ubuntu.com/ubuntu focal/main i386 Packages [723 kB]    
Get:6 http://us.archive.ubuntu.com/ubuntu focal/main amd64 Packages [981 kB]   
(полный вывод опущен)
Fetched 677 kB in 2s (346 kB/s)                              
Reading package lists... Done
devasc@labvm:~$
```
## Часть 3: Обзор навигации по синтаксису команд
> В этой части вы рассмотрите права доступа файлов, изменение прав и прав владельца, перемещение файлов, копирование файлов, удаление файлов и просмотр файлов

### Шаг 1: Проверьте права файлов.
Используйте команду ls Desktop -l для отображения содержимого папки "Рабочий стол".
```shell
devasc@labvm:~$ ls Desktop -l
total 28
-rwxr-xr-x 1 devasc devasc 1095 Mar 30 21:24 chromium_chromium.desktop
-rwxr-xr-x 1 devasc devasc  401 Mar 30 21:25 cisco-packet-tracer_cisco-pacet-tracer.desktop
-rwxr-xr-x 1 devasc devasc  776 Mar 30 21:23 code.desktop
-rwxr-xr-x 1 devasc devasc  373 Mar 30 21:25 drawio_drawio.desktop
-rwxr-xr-x 1 devasc devasc  250 Mar 30 21:21 exo-terminal-emulator.desktop
-rwxr-xr-x 1 devasc devasc   99 Mar 30 21:21 labs.desktop
-rwxr-xr-x 1 devasc devasc  334 Mar 30 21:24 postman_postman.desktop
devasc@labvm:~$
```

#### Ответьте на следующие вопросы относительно приведенного выше вывода. Если необходимо, найдите в Интернете информацию о разрешении файлов Linux, показанном в выводе команды ls.
* Что означает начальное тире в информации о правах файлов?
* Что будет стоять на месте тире, если речь идет о каталоге?
* Что означают следующие три буквы или тире в информации о правах файлов?
* Что означают три средние буквы или тире в информации о разрешении?
* Что означают последние три буквы или тире в информации о разрешении?
* На что указывает первое слово "devasc" в информации о правах доступа?
* На что указывает второй экземпляр "devasc" в информации о разрешении?
* Что означает тип разрешения "r"?
* Что означает тип разрешения "w"?
* Что означает тип разрешения "x"?

### Шаг 2: Изменение прав доступа и владельца файла.
С помощью команды cd перейдите в каталог Документы.
```shell
devasc@labvm:~$ cd Documents/
devasc@labvm:~/Documents$
```
С помощью команды echo создайте файл сценария оболочки, внутри которого будет команда ls ../Desktop. Помните, что символ больше чем (>) перенаправляет вывод команды в файл.
```shell
devasc@labvm:~/Documents$ echo "ls ../Desktop" > myfile.sh
devasc@labvm:~/Documents$
```
Сценарий `myfile.sh` хранится в каталоге /Documents. Используйте команду cat для просмотра единственной команды в сценарии. Этот файл будет использоваться в качестве примера для изменения прав доступа и собственности
```shell
devasc@labvm:~/Documents$ cat myfile.sh 
ls ../Desktop
devasc@labvm:~/Documents$
```
Используйте команду ./myfile.sh для запуска сценария.
```shell
devasc@labvm:~/Documents$ ./myfile.sh
bash: ./myfile.sh: Permission denied
```
Доступ запрещен, так как для файла необходимо установить разрешение executable. Используйте команду ls -l myfile.sh для просмотра текущих разрешений файлов.
```shell
devasc@labvm:~/Documents$ ls -l myfile.sh
-rw-rw-r-- 1 devasc devasc 14 Apr 16 12:46 myfile.sh
```
Используйте команду `chmod +x myfile.sh`, чтобы разрешить выполнение файла.
```shell
devasc@labvm:~/Documents$ chmod +x myfile.sh
devasc@labvm:~/Documents$
```
Снова попробуйте запустить скрипт ./myfile.sh
```shell
devasc@labvm:~/Documents$ ./myfile.sh
chromium_chromium.desktop   exo-terminal-emulator.desktop
cisco-packet-tracer_cisco-pacet-tracer.desktop labs.desktop
code.desktop     postman_postman.desktop
drawio_drawio.desktop
devasc@labvm:~/Documents$
```
Отобразите разрешения файла myfile.sh.
```shell
devasc@labvm:~/Documents$ ls -l
total 4
-rwxrwxr-x 1 root devasc 14 Apr 16 21:28 myfile.sh
devasc@labvm:~/Documents$
```

### Шаг 3: Использование команды перемещения файлов.
С помощью команды mv переместите файл myfile.sh на рабочий стол.
```shell
devasc@labvm:~/Documents$ mv myfile.sh /home/devasc/Desktop/
devasc@labvm:~/Documents$
```
Отобразите содержимое папки "Рабочий стол"
```shell
devasc@labvm:~/Documents$ ls ../Desktop/
chromium_chromium.desktop                       exo-terminal-emulator.desktop
cisco-packet-tracer_cisco-pacet-tracer.desktop  labs.desktop
code.desktop                                    myfile.sh
drawio_drawio.desktop                           postman_postman.desktop
devasc@labvm:~/Documents$
```
Верните файл в папку Документы.
```shell
devasc@labvm:~/Documents$ mv ../Desktop/myfile.sh myfile.sh
devasc@labvm:~/Documents$
```
С помощью команды mv переименуйте myfile.sh в myfile_renamed.sh.
```shell
devasc@labvm:~/Documents$ mv myfile.sh myfile_renamed.sh
devasc@labvm:~/Documents$ ls
myfile_renamed.sh
devasc@labvm:~/Documents$
```

### Шаг 4: Использование команды копирования файлов.
С помощью команды cp создайте копию файла myfile_renamed.sh.
```shell
devasc@labvm:~/Documents$ cp myfile_renamed.sh myfile_renamed_and_copied.sh
devasc@labvm:~/Documents$ ls
myfile_renamed_and_copied.sh  myfile_renamed.sh
devasc@labvm:~/Documents$
```

### Шаг 5: Использование команду удаления файлов.
Используйте команду rm для удаления файла myfile_renamed_and_copied.sh.
```shell
devasc@labvm:~/Documents$ rm myfile_renamed_and_copied.sh 
devasc@labvm:~/Documents$ ls
mbr.img  myfile_renamed.sh
devasc@labvm:~/Documents$
```

### Шаг 6: Перенаправление стандартного потока вывода.
С помощью оператора перенаправления (>) поместите текст в новый файл с именем linux.txt.
```shell
devasc@labvm:~$ echo "Я съел деда!" > linux.txt
devasc@labvm:~$
```
С помощью команды cat перенаправьте содержимое файла linux.txt в другой файл.
```shell
devasc@labvm:~$ cat linux.txt > linux2.txt
devasc@labvm:~$
```
С помощью команды cat просмотрите содержимое файла linux2.txt.
```shell
devasc@labvm:~$ cat linux2.txt
Я съел деда!
devasc@labvm:~$
```
Используйте команду echo для добавления текста в файл linux2.txt.
```shell
devasc@labvm:~$ echo "I LOVE Linux!" >> linux2.txt
devasc@labvm:~$
```
Используйте команду cat для просмотра содержимого файла linux2.txt.
```shell
devasc@labvm:~$ cat linux2.txt
Я съел деда!
I LOVE Linux!
devasc@labvm:~$
```
Используйте команду echo для перезаписи содержимого файла с помощью одинарной угловой скобки.
```shell
devasc@labvm:~$ echo "Linux is POWERFUL!" > linux.txt
devasc@labvm:~$
```
Используйте команду cat для просмотра содержимого файла linux.txt. 
Обратите внимание, что предыдущее состояние "Я съел деда!" было перезаписано.
```shell
devasc@labvm:~$ cat linux.txt
Linux is POWERFUL!
devasc@labvm:~$
```

### Шаг 7: Используйте текстовый редактор vi.
Используйте следующую команду для запуска текстового редактора vi и открытия текстового файла.
```shell
devasc@labvm:~$ vi linux2.txt
```
В окне редактора отображается следующее содержимое:
```shell
Linux is AWESOME!
I LOVE Linux!
```
С помощью текстового редактора измените содержимое на следующее
```shell
Linux is Linux
I am AWESOME!
```
Клавиша `a` позволит вам войти в режим редактирования, добавляя текст после позиции курсора, а клавиша `i` позволит вам войти в режим редактирования, вставляя текст в позицию курсора. Чтобы перейти в командный режим, вам понадобится клавиша `Esc`. Помните, что `d` удалит (вырежет), `y` выдернет (скопирует), а `p` вставит (вставит) текущую строку с курсором.

Сохраните текст в новом файле с именем "linux3.txt". Помните, что вам нужно будет находиться в командном режиме и набрать двоеточие ( : ) для входа в режим ex, чтобы вы могли записать (сохранить) документ ( :w linux3.txt). Затем вы можете использовать команду quit (выход) ( :q) для выхода из редактора vi. Также можно сэкономить на спичках используя команду `:wq`

Используйте команду cat для просмотра содержимого файла linux3.txt.
```shell
devasc@labvm:~$ cat linux3.txt
Linux is Linux
I am AWESOME!
devasc@labvm:~$
```

## Часть 4: Обзор регулярных выражений
> В этой части вы используете команду grep, чтобы рассмотреть, как можно использовать регулярные выражения для фильтрации.
>
> **Примечание:** Ваши результаты могут отличаться от показанных ниже, поскольку состояние виртуальной машины основано на последней загруженной вами итерации, а также на любых изменениях, которые вы могли внести. Тем не менее, вы должны получить некоторые результаты из файла passwd, но ваш выделенный результат будет отличаться.

Используйте команду grep для фильтрации содержимого файла passwd, чтобы отобразить строку из файла passwd, содержащую devasc. Обратите внимание, что два экземпляра devasc выделены. Также обратите внимание, что команда grep чувствительна к регистру. Экземпляр DEVASC не выделяется.
```shell
devasc@labvm:~$ grep devasc /etc/passwd
devasc:x:900:900:DEVASC,,,:/home/devasc:/bin/bash
devasc@labvm:~$
```
Используйте команду grep, чтобы показать, сколько раз root встречается в файле passwd. Обратите внимание, что все три экземпляра root выделены.
```shell
devasc@labvm:~$ grep root /etc/passwd
root:x:0:0:root:/root:/bin/bash
devasc@labvm:~$
```
Используйте команду grep с символом якоря (циркумфлекс) ^, чтобы найти слово, но только в начале строки. Обратите внимание, что выделено только слово в начале строки.
```shell
devasc@labvm:~$ grep '^root' /etc/passwd
root:x:0:0:root:/root:/bin/bash
devasc@labvm:~$
```
Используйте команду grep с символом якоря (доллара) $, чтобы найти слово в конце строки.
```shell
devasc@labvm:~$ grep 'false$' /etc/passwd
tss:x:106:114:TPM software stack,,,:/var/lib/tpm:/bin/false
lightdm:x:107:117:Light Display Manager:/var/lib/lightdm:/bin/false
hplip:x:115:7:HPLIP system user,,,:/run/hplip:/bin/false
devasc@labvm:~$
```
Используйте команду grep с символом якоря (точка) . для поиска слов определенной длины с разными буквами в них. Обратите внимание, что выделен не только daem, но и dnsm.
```shell
devasc@labvm:~$ grep 'd..m' /etc/passwd
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
avahi-autoipd:x:110:121:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/usr/sbin/nologin
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
avahi:x:113:122:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
colord:x:116:125:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
pulse:x:117:126:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
devasc@labvm:~$
```
Используйте команду grep для поиска строк, в которых присутствуют только числа 8 или 9. Обратите внимание, что возвращаются только строки, содержащие 8, 9 или оба числа.
```shell
devasc@labvm:~$ grep '[8-9]' /etc/passwd
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
uuidd:x:103:109::/run/uuidd:/usr/sbin/nologin
devasc:x:900:900:DEVASC,,,:/home/devasc:/bin/bash
systemd-network:x:999:999:systemd Network Management:/:/usr/sbin/nologin
systemd-resolve:x:998:998:systemd Resolver:/:/usr/sbin/nologin
systemd-timesync:x:997:997:systemd Time Synchronization:/:/usr/sbin/nologin
systemd-coredump:x:996:996:systemd Core Dumper:/:/usr/sbin/nologin
rtkit:x:108:119:RealtimeKit,,,:/proc:/usr/sbin/nologin
dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
devasc@labvm:~$
```
Используйте команду grep для поиска литеральных символов. Обратите внимание, что возвращаются только строки, содержащие запятую.
```shell
devasc@labvm:~$ grep '[,]' /etc/passwd
devasc:x:900:900:DEVASC,,,:/home/devasc:/bin/bash
tss:x:106:114:TPM software stack,,,:/var/lib/tpm:/bin/false
rtkit:x:108:119:RealtimeKit,,,:/proc:/usr/sbin/nologin
dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
avahi-autoipd:x:110:121:Avahi autoip daemon,,,:/var/lib/avahi-autoipd:/usr/sbin/nologin
usbmux:x:111:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
kernoops:x:112:65534:Kernel Oops Tracking Daemon,,,:/:/usr/sbin/nologin
avahi:x:113:122:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
hplip:x:115:7:HPLIP system user,,,:/run/hplip:/bin/false
colord:x:116:125:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
pulse:x:117:126:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
devasc@labvm:~$
```
Используйте команду grep для поиска вхождений нулевого или более шаблона, предшествующего ему. Обратите внимание, что возвращаются только строки с new и ne.
```shell
devasc@labvm:~$ grep 'new*' /etc/passwd
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
messagebus:x:100:103::/nonexistent:/usr/sbin/nologin
_apt:x:102:65534::/nonexistent:/usr/sbin/nologin
tcpdump:x:104:110::/nonexistent:/usr/sbin/nologin
systemd-network:x:999:999:systemd Network Management:/:/usr/sbin/nologin
kernoops:x:112:65534:Kernel Oops Tracking Daemon,,,:/:/usr/sbin/nologin
saned:x:114:124::/var/lib/saned:/usr/sbin/nologin
devasc@labvm:~$
```

## Часть 5: Обзор Системного Администрирования
> В этой части вы рассмотрите основные задачи системного администрирования Linux, включая выключение компьютера, просмотр и тестирование конфигурации сети, просмотр процессов, управление установочными пакетами, обновление паролей пользователей, добавление содержимого в файлы и использование текстовых редакторов.

### Шаг 1: Выключение компьютера.
Используйте команду shutdown now, чтобы инициировать немедленное завершение работы ОС (и ВМ). Вам не нужно выполнять это действие, так как ВМ выключится, и вам нужно будет перезапустить ее вручную. Форматом аргумента time может быть слово now, время суток в формате hh:mm или количество минут задержки в формате +minutes.
```shell
devasc@labvm:~$ shutdown now
```
Используйте команду date для проверки даты установки ОС.
```shell
devasc@labvm:~$ date
Fri 4 Feb 2022 08:53:20 PM UTC
devasc@labvm:~$
```
Используйте команду shutdown +1 "Come back soon!", чтобы выключить ОС через 1 минуту и вывести сообщение "Come back soon!". Не забудьте отменить команду, иначе ваша ВМ выключится.
```shell
devasc@labvm:~$ shutdown +1 "Come back soon!"
Shutdown scheduled for Fri 2022-02-04 20:57:13 UTC, use 'shutdown -c' to cancel.
devasc@labvm:~$ shutdown -c 
devasc@labvm:~$
```
## Шаг 2: Просмотр и тестирование конфигурации сети.
Используйте команду ip address для отображения конфигурации сети. Вывод будет немного более подробным. Например, обратите внимание, что для интерфейса dummy0 показаны пять адресов IPv4.
```shell
devasc@labvm:~$ ip address
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:ce:2b:8b brd ff:ff:ff:ff:ff:ff
    inet 10.0.2.15/24 brd 10.0.2.255 scope global dynamic enp0s3
       valid_lft 75746sec preferred_lft 75746sec
    inet6 fe80::a00:27ff:fece:2b8b/64 scope link 
       valid_lft forever preferred_lft forever
3: dummy0: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue state UNKNOWN group default qlen 1000
    link/ether 46:8b:41:b5:de:aa brd ff:ff:ff:ff:ff:ff
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
    inet6 fe80::448b:41ff:feb5:deaa/64 scope link 
       valid_lft forever preferred_lft forever
devasc@labvm:~$ 
```
Используйте команду ping с параметрами -c 4, чтобы четыре раза пропинговать компьютер в локальной сети. Вы должны использовать действительный IP-адрес устройства в вашей локальной сети. В следующем примере используется 192.168.1.1, но в вашей сети, скорее всего, будут другие IPv4-адреса.
```shell
devasc@labvm:~$ ping -c 4 192.168.1.1
PING 192.168.1.1 (192.168.1.1) 56(84) bytes of data.
64 bytes from 192.168.1.1: icmp_seq=1 ttl=63 time=1.13 ms
64 bytes from 192.168.1.1: icmp_seq=2 ttl=63 time=2.30 ms
64 bytes from 192.168.1.1: icmp_seq=3 ttl=63 time=1.31 ms
64 bytes from 192.168.1.1: icmp_seq=4 ttl=63 time=2.49 ms

--- 192.168.1.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 1.130/1.809/2.492/0.594 ms
devasc@labvm:~$ 
```
Вы также можете пинговать имя, и система доменных имен (DNS) преобразует имя в IP-адрес. Например, выполнить ping веб-сайта Cisco. Ваша виртуальная машина сначала отправит DNS-запрос, чтобы получить IP-адрес, а затем отправит пакеты ping. Процесс DNS не отображается в выводе ping.
```shell
devasc@labvm:~$ ping -c 4 www.cisco.com
PING e2867.dsca.akamaiedge.net (23.204.11.200) 56(84) bytes of data.
64 bytes from a23-204-11-200.deploy.static.akamaitechnologies.com (23.204.11.200): icmp_seq=1 ttl=58 time=185 ms
64 bytes from a23-204-11-200.deploy.static.akamaitechnologies.com (23.204.11.200): icmp_seq=2 ttl=58 time=28.8 ms
64 bytes from a23-204-11-200.deploy.static.akamaitechnologies.com (23.204.11.200): icmp_seq=3 ttl=58 time=28.8 ms
64 bytes from a23-204-11-200.deploy.static.akamaitechnologies.com (23.204.11.200): icmp_seq=4 ttl=58 time=26.4 ms

--- e2867.dsca.akamaiedge.net ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3007ms
rtt min/avg/max/mdev = 26.443/67.339/185.363/68.147 ms
devasc@labvm:~$
```

### Шаг 3: Просмотр текущих процессов
Используйте команду ps для отображения процессов, запущенных в текущем терминале.
```shell
devasc@labvm:~$ ps
    PID TTY          TIME CMD
   1416 pts/0    00:00:00 bash
   1453 pts/0    00:00:00 ps
devasc@labvm:~$
``` 
Используйте команду ps с параметром -e для отображения всех процессов, запущенных на компьютере.
```shell
devasc@labvm:~$ ps -e
    PID TTY          TIME CMD
      1 ?        00:00:01 systemd
      2 ?        00:00:00 kthreadd
      3 ?        00:00:00 rcu_gp
      4 ?        00:00:00 rcu_par_gp
      6 ?        00:00:00 kworker/0:0H-kblockd
      7 ?        00:00:00 kworker/0:1-events
      9 ?        00:00:00 mm_percpu_wq
 (полный вывод опущен)
```
Вы можете направить вывод любой команды на один экран за раз, добавив | more. Отобразится один экран вывода с надписью - more-, показанной внизу. Теперь вы можете использовать клавишу Enter для вывода одной строки за раз, пробел для вывода одного экрана за раз или Ctrl+C для выхода и возврата в командную строку.
```shell
devasc@labvm:~$ ps -e | more
    PID TTY          TIME CMD
      1 ?        00:00:01 systemd
      2 ?        00:00:00 kthreadd
      3 ?        00:00:00 rcu_gp
      4 ?        00:00:00 rcu_par_gp
      6 ?        00:00:00 kworker/0:0H-kblockd
      9 ?        00:00:00 mm_percpu_wq
     10 ?        00:00:00 ksoftirqd/0
--More--
```
Используйте ps с параметром -ef для более детального отображения всех процессов, запущенных на компьютере.
```shell
devasc@labvm:~$ ps -ef
UID          PID    PPID  C STIME TTY          TIME CMD
root           1       0  0 20:57 ?        00:00:01 /sbin/init
root           2       0  0 20:57 ?        00:00:00 [kthreadd]
root           3       2  0 20:57 ?        00:00:00 [rcu_gp]
root           4       2  0 20:57 ?        00:00:00 [rcu_par_gp]
root           6       2  0 20:57 ?        00:00:00 [kworker/0:0H-kblockd]
root           9       2  0 20:57 ?        00:00:00 [mm_percpu_wq]
root          10       2  0 20:57 ?        00:00:00 [ksoftirqd/0]
root          11       2  0 20:57 ?        00:00:01 [rcu_sched]
(полный вывод опущен)
``` 

### Шаг 4: Управление пакетами
Используйте команду `apt-get update`, чтобы обновить список доступных пакетов в ОС, как было показано ранее в части 1 этой лабораторной работы. Вы должны использовать разрешения административного уровня для использования этой команды.
```shell
devasc@labvm:~$ sudo apt-get update
Hit:1 http://security.ubuntu.com/ubuntu focal-security InRelease
Get:2 http://us.archive.ubuntu.com/ubuntu focal InRelease [265 kB]
Hit:3 http://us.archive.ubuntu.com/ubuntu focal-updates InRelease
Hit:4 http://us.archive.ubuntu.com/ubuntu focal-backports InRelease
Get:5 http://us.archive.ubuntu.com/ubuntu focal/main i386 Packages [721 kB]
Get:6 http://us.archive.ubuntu.com/ubuntu focal/main amd64 Packages [974 kB]
Get:7 http://us.archive.ubuntu.com/ubuntu focal/main Translation-en [506 kB]
(полный вывод опущен)
```
Используйте команду `apt-cache search` для поиска определенного пакета. 
```shell
devasc@labvm:~$ apt-cache search speed test
(полный вывод опущен)
smalt-examples - Sequence Mapping and Alignment Tool (examples)
speedtest-cli - Command line interface for testing internet bandwidth using speedtest.net
sup - Software Upgrade Protocol implementation
sysbench - multi-threaded benchmark tool for database systems
tcpreplay - Tool to replay saved tcpdump files at arbitrary speeds (полный вывод опущен)
```
Используйте команду `apt-get install` для установки пакета.
```shell
devasc@labvm:~$ sudo apt-get install speedtest-cli
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  speedtest-cli
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 24,0 kB of archives.
After this operation, 106 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu focal-updates/universe amd64 speedtest-cli all 2.1.2-2ubuntu0.20.04.1 [24,0 kB]
Fetched 24,0 kB in 1s (22,8 kB/s)        
Selecting previously unselected package speedtest-cli. 
(полный вывод опущен)
```
Теперь вы можете использовать команду `speedtest-cli` для проверки текущей скорости подключения к Интернету.
```shell
devasc@labvm:~$ speedtest-cli
Retrieving speedtest.net configuration...
Testing from Beeline Home (95.24.224.57)...
Retrieving speedtest.net server list...
Selecting best server based on ping...
Hosted by AirNet (Saint Petersburg) [5.57 km]: 26.678 ms
Testing download speed................................................................................
Download: 90.87 Mbit/s
Testing upload speed......................................................................................................
Upload: 59.91 Mbit/s
devasc@labvm:~$
```
Используйте команду apt-get upgrade для обновления всех пакетов и зависимостей на компьютере.
devasc@labvm:~$ sudo apt-get upgrade 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Calculating upgrade... Done
The following packages have been kept back:
  libnss-systemd libpam-systemd libsystemd0 libyelp0 linux-generic linux-headers-generic
(полный вывод опущен)

Используйте команду `apt-get purge`, чтобы полностью удалить пакет с компьютера.
```shell
devasc@labvm:~$ sudo apt-get purge speedtest-cli
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be REMOVED:
  speedtest-cli*
0 upgraded, 0 newly installed, 1 to remove and and 502 not upgraded.
After this operation, 106 kB disk space will be freed.
Do you want to continue? [Y/n] 
(Reading database ... 211937 files and directories currently installed.)
Removing speedtest-cli (2.1.2-2) ... 
(полный вывод опущен)
```
### Шаг 5: Обновление паролей
Используйте команду passwd для обновления пароля. 
> Примечание: Если вы действительно меняете пароль для пользователя devasc, убедитесь, что вы его запомнили.
```shell
devasc@labvm:~$ passwd
Changing password for devasc.
Current password: 
New password: 
Retype new password: 
passwd: password updated successfully
devasc@labvm:~$ 
````
Используйте команду passwd с параметром -S для просмотра состояния пароля.
```shell
devasc@labvm:~$ passwd -S
devasc P 02/04/2022 0 99999 7 -1
devasc@labvm:~$
```
Используйте страницы руководства по команде passwd (man passwd) для изучения опции -S и поиска ответов на следующие вопросы.
* Каков текущий статус пароля?
* Какое минимальное количество дней должно пройти, чтобы пароль можно было изменить?
* Какое количество дней после истечения срока действия пароля учетная запись остается активной?