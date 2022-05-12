# Исследование YANG моделей
## Цель лабораторной работы:
- Часть 1: Запуск виртуальной машины DEVASC
- Часть 2: Изучение YANG модели на GitHub
- Часть 3: Изучение YANG модели с помощью pyang

## Необходимые ресурсы:
- 1 ПК
- Virtual Box или VMWare
- DEVASC виртуальная машина

## Порядок выполнения работы
## Часть 1: Запуск виртуальной машины DEVASC
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.

## Часть 2: Изучение YANG модели на GitHub
> В этой части вы установите модуль pyang в вашу виртуальную машину DEVASC и изучите, как он преобразует файлы YANG. Pyang упрощает работу с файлами YANG. Модуль поставляется с исполняемым файлом командной строки pyang, который преобразует файлы YANG в более человекочитаемый формат.

### Шаг 1: Изучите Cisco IOS XE YANG модели в репозитории GitHub.
Откройте Chromium и перейдите на страницу https://github.com/YangModels/yang.
В ветве master перейдите к моделям YANG для Cisco IOS XE версии 17.8.1, щелкнув следующие каталоги: vendor > cisco > xe > 1781
Щелкните ietf-interfaces.yang и прокрутите все узлы контейнера, узлы листа и узлы списка. Если вы знакомы с выводом команды IOS show interfaces, то вы должны узнать некоторые или все узлы. Например, около строки 221 вы увидите включенный лист.
```yang
leaf enabled {
  type boolean;
  default "true";
  description
    "This leaf contains the configured, desired state of the
     interface.
     Systems that implement the IF-MIB use the value of this
     leaf in the 'running' datastore to set
     IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry
     has been initialized, as described in RFC 2863.
     Changes in this leaf in the 'running' datastore are
     reflected in ifAdminStatus, but if ifAdminStatus is
     changed over SNMP, this leaf is not affected.";
  reference
    "RFC 2863: The Interfaces Group MIB - ifAdminStatus";
}
```

### Шаг 2: Скопируйте модель ietf-interfaces.yang в папку на вашей виртуальной машине.
Откройте код VS. 
Нажмите File > Open Folder... и перейдите в каталог devnet-src. 
Нажмите OK.
Откройте окно терминала в VS Code: Terminal > New Terminal.
Создайте подкаталог pyang в каталоге /devnet-src.
```shell
devasc@labvm:~/labs/devnet-src$ mkdir pyang
devasc@labvm:~/labs/devnet-src$
```
Вернитесь на вкладку Chromium, где модель ietf-interfaces.yang все еще открыта. При необходимости прокрутите страницу назад к вершине и нажмите Raw, чтобы отобразить только данные модели YANG.
Выберите и скопируйте URL-адрес.
В терминале перейдите в папку pyang.
С помощью wget сохраните необработанный файл ietf-interfaces.yang.
```shell
devasc@labvm:~/labs/devnet-src/pyang$ wget https://raw.githubusercontent.com/YangModels/yang/master/vendor/cisco/xe/1781/ietf-interfaces.yang
--2022-05-10 19:28:07--  https://raw.githubusercontent.com/YangModels/yang/master/vendor/cisco/xe/1781/ietf-interfaces.yang
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 24248 (24K) [text/plain]
Saving to: ‘ietf-interfaces.yang’

ietf-interfaces.ya 100%[===============>]  23,68K  --.-KB/s    in 0s      

2022-05-10 19:28:07 (55,8 MB/s) - ‘ietf-interfaces.yang’ saved [24248/24248]

devasc@labvm:~/labs/devnet-src/pyang$ 
```
Теперь у вас есть локальная версия модели ietf-interfaces.yang, которой вы можете манипулировать с помощью pyang.

## Часть 3: Изучение YANG модели с помощью pyang
> В этой части вы установите модуль pyang в вашу виртуальную машину DEVASC и изучите, как он преобразует модель YANG, которую вы скопировали с GitHub. Pyang упрощает работу с файлами YANG. Модуль поставляется с исполняемым файлом командной строки pyang, который преобразует файлы YANG в более удобочитаемый формат.

### Шаг 1: Убедитесь, что pyang установлен и обновлен.
В VS Code откройте окно терминала. 
Проверьте, что pyang уже установлен, с помощью команды pyang -v. Номер вашей версии может отличаться от указанного здесь.
```shell
devasc@labvm:~/labs/devnet-src$ pyang -v
pyang 2.2.1
devasc@labvm:~/labs/devnet-src$
```
(Опционально) Вы можете проверить наличие последних обновлений pyang с помощью следующей команды pip3. Любые обновления после написания этой лабораторной работы будут загружены и установлены.
```shell
devasc@labvm:~/labs/devnet-src$ pip3 install pyang --upgrade
Collecting pyang
  Downloading pyang-2.5.3-py2.py3-none-any.whl (592 kB)
     |████████████████████████████████| 592 kB 1.1 MB/s 
Requirement already satisfied, skipping upgrade: lxml in /home/devasc/.local/lib/python3.8/site-packages (from pyang) (4.5.1)
Installing collected packages: pyang
  Attempting uninstall: pyang
    Found existing installation: pyang 2.2.1
    Uninstalling pyang-2.2.1:
      Successfully uninstalled pyang-2.2.1
Successfully installed pyang-2.5.3
devasc@labvm:~/labs/devnet-src/pyang$
```

### Шаг 2: Преобразование модели ietf-interfaces.yang.
Перейдите в каталог pyang.
```shell
devasc@labvm:~/labs/devnet-src$ cd pyang
devasc@labvm:~/labs/devnet-src/pyang$
```
Введите pyang -h | more, чтобы изучить варианты преобразования модели YANG. Найдите опцию -f, как показано ниже. Вы будете использовать опцию форматирования дерева.
```shell
devasc@labvm:~/labs/devnet-src/pyang$ pyang -h | more
Usage: pyang [options] [<filename>...]

Validates the YANG module in <filename> (or stdin), and all its dependencies.

Options:
  -h, --help            Show this help message and exit
  -v, --version         Show version number and exit
<вывод опущен>
  -f FORMAT, --format=FORMAT
                        Convert to FORMAT.  Supported formats are: yang, yin,
                        dsdl, jstree, jsonxsl, capability, identifiers, jtox,
                        uml, name, omni, tree, depend, sample-xml-skeleton
<вывод опущен>
devasc@labvm:~/labs/devnet-src/pyang$
```
Преобразуйте модель ietf-interfaces.yang в формат дерева с помощью следующей команды. Обратите внимание, что включенный лист гораздо легче найти и прочитать в этом формате.
```shell
devasc@labvm:~/labs/devnet-src/pyang$ pyang -f tree ietf-interfaces.yang 
ietf-interfaces.yang:6: error: module "ietf-yang-types" not found in search path
module: ietf-interfaces
  +--rw interfaces
  |  +--rw interface* [name]
  |     +--rw name                        string
  |     +--rw description?                string
  |     +--rw type                        identityref
  |     +--rw enabled?                    boolean
  |     +--rw link-up-down-trap-enable?   enumeration {if-mib}?
  +--ro interfaces-state
     +--ro interface* [name]
        +--ro name               string
        +--ro type               identityref
        +--ro admin-status       enumeration {if-mib}?
        +--ro oper-status        enumeration
        +--ro last-change?       yang:date-and-time
        +--ro if-index           int32 {if-mib}?
        +--ro phys-address?      yang:phys-address
        +--ro higher-layer-if*   interface-state-ref
        +--ro lower-layer-if*    interface-state-ref
        +--ro speed?             yang:gauge64
        +--ro statistics
           +--ro discontinuity-time    yang:date-and-time
           +--ro in-octets?            yang:counter64
           +--ro in-unicast-pkts?      yang:counter64
           +--ro in-broadcast-pkts?    yang:counter64
           +--ro in-multicast-pkts?    yang:counter64
           +--ro in-discards?          yang:counter32
           +--ro in-errors?            yang:counter32
           +--ro in-unknown-protos?    yang:counter32
           +--ro out-octets?           yang:counter64
           +--ro out-unicast-pkts?     yang:counter64
           +--ro out-broadcast-pkts?   yang:counter64
           +--ro out-multicast-pkts?   yang:counter64
           +--ro out-discards?         yang:counter32
           +--ro out-errors?           yang:counter32
devasc@labvm:~/labs/devnet-src/pyang$
```