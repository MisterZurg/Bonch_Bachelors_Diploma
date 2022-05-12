# Автоматизированное тестирование с помощью pyATS и Genie
## Цель лабораторной работы:
- Часть 1: Запуск виртуальной машины DEVASC
- Часть 2: Создание виртуальной среды Python
- Часть 3: pyATS для тестирования
- Часть 4: Genie для анализа командного вывода IOS
- Часть 5: Genie для сравнения конфигураций
- Часть 6: Завершение лабораторной и дальнейшие исследования

## Необходимые ресурсы:
- 1 ПК
- Virtual Box или VMWare
- DEVASC виртуальная машина
- CSR1kv виртуальная машина

## Порядок выполнения работы
## Часть 1: Запуск виртуальной машины DEVASC
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.

## Часть 2: Создание виртуальной среды Python
> В этой части вы создадите виртуальную среду Python, называемую виртуальной средой Python или "venv".

### Шаг 1: Откройте терминал в DEVASC-LABVM.
Дважды щелкните значок эмулятора терминала на рабочем столе, или воспользуйтесь терминалом в VS Code.
### Шаг 2: Создание виртуальной среды Python (venv).
Инструмент pyATS лучше всего устанавливать для работы в окружении venv. Среда venv копируется из вашей базовой среды Python, но хранится отдельно от неё. Это позволяет вам избежать установки программ, которые могут навсегда изменить общее состояние вашего компьютера.
Создайте каталог pyats и перейдите в этот каталог. Вы можете использовать символы && для объединения двух команд в одной строке.
```shell
devasc@labvm:~$ mkdir labs/devnet-src/pyats && cd labs/devnet-src/pyats
devasc@labvm:~/labs/devnet-src/pyats$
```
Создайте новую виртуальную среду Python, которая создаст каталог csr1kv в каталоге pyats.
```shell
devasc@labvm:~/labs/devnet-src/pyats$ python3 -m venv csr1kv
```
> Примечание: Вы также можете использовать точку "." вместо имени каталога, если вы хотите создать среду venv в текущем каталоге.

### Шаг 3: Просмотрите свою виртуальную среду Python (venv).
Перейдите в новый "целевой" каталог csr1kv и перечислите файлы. Venv создает самодостаточное дерево каталогов (test-project), которое содержит установку Python для определенной версии Python, а также ряд дополнительных пакетов. Он также создает подкаталог bin, содержащий копию двоичного файла Python.
Обратите внимание, в частности, на поддиректорию bin и созданные файлы pyvenv.cfg.
```shell
devasc@labvm:~/labs/devnet-src/pyats$ cd csr1kv
devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ ls -l
total 20
drwxrwxr-x 2 devasc devasc 4096 мая 10 17:48 bin
drwxrwxr-x 2 devasc devasc 4096 мая 10 17:48 include
drwxrwxr-x 3 devasc devasc 4096 мая 10 17:48 lib
lrwxrwxrwx 1 devasc devasc    3 мая 10 17:48 lib64 -> lib
-rw-rw-r-- 1 devasc devasc   69 мая 10 17:48 pyvenv.cfg
drwxrwxr-x 3 devasc devasc 4096 мая 10 17:48 share
devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```
Изучите содержимое файла pyvenv.cfg. Обратите внимание, что этот файл указывает на местоположение вашей установки Python в /usr/bin.
```shell
devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ cat pyvenv.cfg
home = /usr/bin
include-system-site-packages = false
version = 3.8.2
devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```
Символьная ссылка — особый тип файла, который служит ссылкой на другой файл или каталог. Чтобы лучше понять venv и то, как он использует символические ссылки, перечислите файлы Python в каталоге /usr/bin, на которые ссылается файл pyvenv.cfg. Используйте опцию ls number one (-1), чтобы перечислить все файлы в одну строку.
```shell
devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ ls -1 /usr/bin/python*
/usr/bin/python3
/usr/bin/python3.8
/usr/bin/python3.8-config
/usr/bin/python3-config
/usr/bin/python-argcomplete-check-easy-install-script3
/usr/bin/python-argcomplete-tcsh3
devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```
Теперь изучите содержимое созданного venv подкаталога bin. Обратите внимание, что в этом подкаталоге есть два файла, оба из которых являются симлинками. В данном случае это ссылка на двоичные файлы Python в /usr/bin. Симлинки используются для связывания библиотек и обеспечения постоянного доступа к файлам без необходимости перемещения или создания копии исходного файла. Существует также файл activate, который будет рассмотрен далее.
```shell
devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ ls -l bin
total 44
-rw-r--r-- 1 devasc devasc 2225 мая 10 17:48 activate
-rw-r--r-- 1 devasc devasc 1277 мая 10 17:48 activate.csh
-rw-r--r-- 1 devasc devasc 2429 мая 10 17:48 activate.fish
-rw-r--r-- 1 devasc devasc 8471 мая 10 17:48 Activate.ps1
-rwxrwxr-x 1 devasc devasc  267 мая 10 17:48 easy_install
-rwxrwxr-x 1 devasc devasc  267 мая 10 17:48 easy_install-3.8
-rwxrwxr-x 1 devasc devasc  258 мая 10 17:48 pip
-rwxrwxr-x 1 devasc devasc  258 мая 10 17:48 pip3
-rwxrwxr-x 1 devasc devasc  258 мая 10 17:48 pip3.8
lrwxrwxrwx 1 devasc devasc    7 мая 10 17:48 python -> python3
lrwxrwxrwx 1 devasc devasc   16 мая 10 17:48 python3 -> /usr/bin/python3
devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```
Запустите виртуальную среду с помощью bin/activate. Заметьте, что теперь перед подсказкой стоит (csr1kv). Все команды, выполняемые с этого момента, находятся в этой виртуальной среде.
```shell
devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ source bin/activate
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```
> Примечание: Команда deactivate используется для выхода из среды venv и возврата в обычную среду оболочки.

## Часть 3: Использование библиотеки тестирования pyATS
> В этой части вы будете использовать pyATS, библиотеку тестирования на языке python.

### Шаг 1: Установка pyATS.
Установите pyATS с помощью pip3. Это займет несколько минут. Во время установки вы можете увидеть некоторые ошибки. Обычно их можно игнорировать, пока pyATS может быть проверен, как показано в следующем шаге.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ pip3 install pyats[full]
Collecting pyats[full]
  Downloading pyats-22.4-cp38-cp38-manylinux1_x86_64.whl (3.3 MB)

<вывод опущен>
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ 
```

### Шаг 2: Проверка pyATS.
Убедитесь, что pyATS был успешно установлен, используя команду pyats --help. Обратите внимание, что вы можете получить дополнительную справку по любой команде pyats с помощью команды pyats <команда> --help.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ pyats --help
Usage:
  pyats <command> [options]

Commands:
    create              create scripts and libraries from template
    diff                Command to diff two snapshots saved to file or directory
    dnac                Command to learn DNAC features and save to file (Prototype)
    learn               Command to learn device features and save to file
    logs                command enabling log archive viewing in local browser
    parse               Command to parse show commands
    run                 runs the provided script and output corresponding results.
    secret              utilities for working with secret strings.
    shell               enter Python shell, loading a pyATS testbed file and/or pickled data
    validate            utlities that helps to validate input files
    version             commands related to version display and manipulation

General Options:
  -h, --help            Show help

Run 'pyats <command> --help' for more information on a command.
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```

### Шаг 3: Клонируйте и изучите примеры скриптов pyATS с GitHub.
Клонируйте репозиторий образцов сценариев CiscoTestAutomation на Github pyATS.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ git clone https://github.com/CiscoTestAutomation/examples
Cloning into 'examples'...
remote: Enumerating objects: 1245, done.
remote: Counting objects: 100% (93/93), done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 1245 (delta 68), reused 62 (delta 62), pack-reused 1152
Receiving objects: 100% (1245/1245), 1.09 MiB | 1.63 MiB/s, done.
Resolving deltas: 100% (640/640), done.
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```
Убедитесь, что копирование прошло успешно, перечислив файлы в текущем каталоге. Обратите внимание, что появился новый подкаталог example.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ ls -l
total 24
drwxrwxr-x  3 devasc devasc 4096 мая 10 17:56 bin
drwxrwxr-x 24 devasc devasc 4096 мая 10 17:57 examples
drwxrwxr-x  2 devasc devasc 4096 мая 10 17:48 include
drwxrwxr-x  3 devasc devasc 4096 мая 10 17:48 lib
lrwxrwxrwx  1 devasc devasc    3 мая 10 17:48 lib64 -> lib
-rw-rw-r--  1 devasc devasc   69 мая 10 17:48 pyvenv.cfg
drwxrwxr-x  3 devasc devasc 4096 мая 10 17:48 share
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```
Отобразите файлы в подкаталоге examples. Обратите внимание, что в нем есть подкаталог basic, а также несколько других файлов.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ ls -l examples
total 96
drwxrwxr-x  3 devasc devasc  4096 мая 10 17:57 abstraction_example
drwxrwxr-x  3 devasc devasc  4096 мая 10 17:57 basic
<вывод опущен>
drwxrwxr-x  2 devasc devasc  4096 мая 10 17:57 uids
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ 
```
Отобразите файлы в этой поддиректории. Здесь находятся скрипты, которые мы будем использовать в следующем шаге.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ ls -l examples/basic
total 16
-rw-rw-r-- 1 devasc devasc  534 мая 10 17:57 basic_example_job.py
-rwxrwxr-x 1 devasc devasc 4510 мая 10 17:57 basic_example_script.py
drwxrwxr-x 2 devasc devasc 4096 мая 10 17:57 results
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```

### Шаг 4: Изучите файлы со скриптами.
Синтаксис объявления тестов в pyATS основан на популярных фреймворках модульного тестирования Python, таких как pytest. Он поддерживает базовые утверждения тестирования, такие как утверждение, что переменная имеет заданное значение, и наряду с явным предоставлением результатов через определенные API.
Python скрипт, который вы будете использовать, называется basic_example_script.py. Отобразите содержимое с помощью команды cat. Обратите внимание, что этот скрипт содержит следующие разделы, как выделено в выводе ниже:
- Общий блок настройки
- Несколько блоков тестирования
- Общий блок очистки

Эти блоки содержат операторы, которые подготавливают и/или определяют готовность тестовой топологии (процесс, который может включать создание проблем), выполняют тесты, а затем возвращают топологию в известное состояние.
Блоки тестирования — часто упоминаемые в документации pyATS как Test Cases — могут содержать несколько тестов, каждый из которых имеет свой собственный код настройки и очистки. Однако, согласно лучшей практике, общая секция Cleanup в конце должна быть разработана с учетом идемпотентности, то есть она должна проверять и восстанавливать все изменения, сделанные Setup и Test, и возвращать топологию в исходное, желаемое состояние.
> Примечание: Хотя понимать код не обязательно, вам будет полезно прочитать комментарии внутри Python скрипта.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ cat examples/basic/basic_example_script.py | more
```
```python
#!/usr/bin/env python
###################################################################
# basic_example.py : A very simple test script example which include:
#     common_setup
#     Tescases
#     common_cleanup
# The purpose of this sample test script is to show the "hello world"
# of aetest.
###################################################################

# To get a logger for the script
import logging

# Needed for aetest script
from pyats import aetest

# Get your logger for your script
log = logging.getLogger(__name__)

###################################################################
###                  COMMON SETUP SECTION                       ###
###################################################################

# This is how to create a CommonSetup
# You can have one of no CommonSetup
# CommonSetup can be named whatever you want

class common_setup(aetest.CommonSetup):
    """ Common Setup section """

    # CommonSetup have subsection. 
    # You can have 1 to as many subsection as wanted
    # here is an example of 2 subsections

    # First subsection
    @aetest.subsection
    def sample_subsection_1(self):
        """ Common Setup subsection """
        log.info("Aetest Common Setup ")

    # If you want to get the name of current section, 
    # add section to the argument of the function.

    # Second subsection
    @aetest.subsection
    def sample_subsection_2(self, section):
        """ Common Setup subsection """
        log.info("Inside %s" % (section))

        # And how to access the class itself ?

        # self refers to the instance of that class, and remains consistent
        # throughout the execution of that container.
        log.info("Inside class %s" % (self.uid))

###################################################################
###                     TESTCASES SECTION                       ###
###################################################################

# This is how to create a testcase
# You can have 0 to as many testcase as wanted

# Testcase name : tc_one
class tc_one(aetest.Testcase):
    """ This is user Testcases section """

    # Testcases are divided into 3 sections
    # Setup, Test and Cleanup.

    # This is how to create a setup section
    @aetest.setup
    def prepare_testcase(self, section):
        """ Testcase Setup section """
        log.info("Preparing the test")
        log.info(section)

    # This is how to create a test section
    # You can have 0 to as many test section as wanted
    
    # First test section
    @ aetest.test
    def simple_test_1(self):
        """ Sample test section. Only print """
        log.info("First test section ")

    # Second test section
    @ aetest.test
    def simple_test_2(self):
        """ Sample test section. Only print """
        log.info("Second test section ")

    # This is how to create a cleanup section
    @aetest.cleanup
    def clean_testcase(self):
        """ Testcase cleanup section """
        log.info("Pass testcase cleanup")

# Testcase name : tc_two
class tc_two(aetest.Testcase):
    """ This is user Testcases section """

    @ aetest.test
    def simple_test_1(self):
        """ Sample test section. Only print """
        log.info("First test section ")
        self.failed('This is an intentional failure')

    # Second test section
    @ aetest.test
    def simple_test_2(self):
        """ Sample test section. Only print """
        log.info("Second test section ")

    # This is how to create a cleanup section
    @aetest.cleanup
    def clean_testcase(self):
        """ Testcase cleanup section """
        log.info("Pass testcase cleanup")

#####################################################################
####                       COMMON CLEANUP SECTION                 ###
#####################################################################

# This is how to create a CommonCleanup
# You can have 0 , or 1 CommonCleanup.
# CommonCleanup can be named whatever you want :)
class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """

    # CommonCleanup follow exactly the same rule as CommonSetup regarding
    # subsection 
    # You can have 1 to as many subsection as wanted
    # here is an example of 1 subsections

    @aetest.subsection
    def clean_everything(self):
        """ Common Cleanup Subsection """
        log.info("Aetest Common Cleanup ")

if __name__ == '__main__': # pragma: no cover
    aetest.main()
```
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```
Скрипт pyATS — это файл Python, в котором объявлены тесты pyATS. Он может быть запущен непосредственно как отдельный файл Python, генерируя вывод только в окно терминала. В качестве альтернативы, один или несколько скриптов pyATS могут быть скомпилированы в "задание" и запущены вместе как пакетный процесс с помощью модуля pyATS EasyPy. EasyPy обеспечивает параллельное выполнение нескольких сценариев, собирает журналы в одном месте и предоставляет центральную точку для внесения изменений в тестируемую топологию.
Используйте cat для отображения файла задания pyATS, pyats_sample_job.py. Обратите внимание на инструкции по запуску этого файла, выделенные ниже.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ cat examples/basic/basic_example_job.py
```
```python
# To run the job:
# pyats run job basic_example_job.py
# Description: This example shows the basic functionality of pyats
#              with few passing tests

import os
from pyats.easypy import run

# All run() must be inside a main function
def main():
    # Find the location of the script in relation to the job file
    test_path = os.path.dirname(os.path.abspath(__file__))
    testscript = os.path.join(test_path, 'basic_example_script.py')

    # Execute the testscript
    run(testscript=testscript)
```
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```

### Шаг 5: Запустите pyATS вручную, чтобы вызвать обычный тест-кейс.
Используя задание pyATS и файлы сценария, запустите pyATS вручную, чтобы вызвать основной тестовый пример. Это позволит убедиться, что задание pyATS и файлы сценария работают правильно. Информация в выходных данных выходит за рамки данной лабораторной работы, однако вы заметите, что задание и сценарий выполнили все необходимые задачи.
Примечание: приведенный ниже вывод был усечен. Репозиторий Cisco Test Automation на GitHub может быть изменен, что включает задание pyATS и файлы скриптов. Ваш вывод может быть другим, но не должен фатально повлиять на результат. Например, в файл basic_example_script.py был добавлен преднамеренный сбой, который не вызывает никаких проблем. Это пример того, что репозитории динамичны.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ pyats run job examples/basic/basic_example_job.py
2022-05-10T18:03:54: %EASYPY-INFO: Starting job run: basic_example_job
2022-05-10T18:03:54: %EASYPY-INFO: Runinfo directory: /home/devasc/.pyats/runinfo/basic_example_job.2022May10_18:03:53.899937
2022-05-10T18:03:54: %EASYPY-INFO: --------------------------------------------------------------------------------
2022-05-10T18:03:57: %EASYPY-INFO: Starting task execution: Task-1
2022-05-10T18:03:57: %EASYPY-INFO:     test harness = pyats.aetest
2022-05-10T18:03:57: %EASYPY-INFO:     testscript   = /home/devasc/labs/devnet-src/pyats/csr1kv/examples/basic/basic_example_script.py
2022-05-10T18:03:57: %AETEST-INFO: +------------------------------------------------------------------------------+
2022-05-10T18:03:57: %AETEST-INFO: |                            Starting common setup                             |
<вывод опущен>
-------+
2022-05-10T18:03:57: %SCRIPT-INFO: First test section 
2022-05-10T18:03:57: %AETEST-ERROR: Failed reason: This is an intentional failure
2022-05-10T18:03:57: %AETEST-INFO: The result of section simple_test_1 is => FAILED
2022-05-10T18:03:57: %AETEST-INFO: +------------------------------------------------------------------------------+
2022-05-10T18:03:57: %AETEST-INFO: |                        Starting section simple_test_2                        |
<вывод опущен>
-------+
2022-05-10T18:03:59: %EASYPY-INFO: |                                Easypy Report                                 |
2022-05-10T18:03:59: %EASYPY-INFO: +------------------------------------------------------------------------------+
<вывод опущен>
2022-05-10T18:03:59: %EASYPY-INFO: Overall Stats
2022-05-10T18:03:59: %EASYPY-INFO:     Passed     : 3
2022-05-10T18:03:59: %EASYPY-INFO:     Passx      : 0
2022-05-10T18:03:59: %EASYPY-INFO:     Failed     : 1
2022-05-10T18:03:59: %EASYPY-INFO:     Aborted    : 0
2022-05-10T18:03:59: %EASYPY-INFO:     Blocked    : 0
2022-05-10T18:03:59: %EASYPY-INFO:     Skipped    : 0
2022-05-10T18:03:59: %EASYPY-INFO:     Errored    : 0
2022-05-10T18:03:59: %EASYPY-INFO: 
2022-05-10T18:03:59: %EASYPY-INFO:     TOTAL      : 4
2022-05-10T18:03:59: %EASYPY-INFO: 
2022-05-10T18:03:59: %EASYPY-INFO: Success Rate   : 75.00 %
2022-05-10T18:03:59: %EASYPY-INFO: 
2022-05-10T18:03:59: %EASYPY-INFO: +------------------------------------------------------------------------------+
2022-05-10T18:03:59: %EASYPY-INFO: |                             Task Result Summary                              |
2022-05-10T18:03:59: %EASYPY-INFO: +------------------------------------------------------------------------------+
2022-05-10T18:03:59: %EASYPY-INFO: Task-1: basic_example_script.common_setup                                 PASSED
2022-05-10T18:03:59: %EASYPY-INFO: Task-1: basic_example_script.tc_one                                       PASSED
2022-05-10T18:03:59: %EASYPY-INFO: Task-1: basic_example_script.tc_two                                       FAILED
2022-05-10T18:03:59: %EASYPY-INFO: Task-1: basic_example_script.common_cleanup                               PASSED
2022-05-10T18:03:59: %EASYPY-INFO: 
2022-05-10T18:03:59: %EASYPY-INFO: +------------------------------------------------------------------------------+
2022-05-10T18:03:59: %EASYPY-INFO: |                             Task Result Details                              |
2022-05-10T18:03:59: %EASYPY-INFO: +------------------------------------------------------------------------------+
2022-05-10T18:03:59: %EASYPY-INFO: Task-1: basic_example_script
2022-05-10T18:03:59: %EASYPY-INFO: |-- common_setup                                                          PASSED
2022-05-10T18:03:59: %EASYPY-INFO: |   |-- sample_subsection_1                                               PASSED
2022-05-10T18:03:59: %EASYPY-INFO: |   `-- sample_subsection_2                                               PASSED
2022-05-10T18:03:59: %EASYPY-INFO: |-- tc_one                                                                PASSED
2022-05-10T18:03:59: %EASYPY-INFO: |   |-- prepare_testcase                                                  PASSED
2022-05-10T18:03:59: %EASYPY-INFO: |   |-- simple_test_1                                                     PASSED
2022-05-10T18:03:59: %EASYPY-INFO: |   |-- simple_test_2                                                     PASSED
2022-05-10T18:03:59: %EASYPY-INFO: |   `-- clean_testcase                                                    PASSED
2022-05-10T18:03:59: %EASYPY-INFO: |-- tc_two                                                                FAILED
2022-05-10T18:03:59: %EASYPY-INFO: |   |-- simple_test_1                                                     FAILED
2022-05-10T18:03:59: %EASYPY-INFO: |   |-- simple_test_2                                                     PASSED
2022-05-10T18:03:59: %EASYPY-INFO: |   `-- clean_testcase                                                    PASSED
2022-05-10T18:03:59: %EASYPY-INFO: `-- common_cleanup                                                        PASSED
2022-05-10T18:03:59: %EASYPY-INFO:     `-- clean_everything                                                  PASSED
2022-05-10T18:03:59: %EASYPY-INFO: Sending report email...
2022-05-10T18:03:59: %EASYPY-INFO: Missing SMTP server configuration, or failed to reach/authenticate/send mail. Result notification email failed to send.
2022-05-10T18:03:59: %EASYPY-INFO: Done!

Pro Tip
-------
   Use the following command to view your logs locally:
       pyats logs view

(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ 
```

## Часть 4: Genie для анализа командного вывода IOS
> В этой части вы будете использовать Genie для получения неструктурированного вывода IOS и его разбора в JSON.

### Шаг 1: Создайте testbed YAML.
Инструменты pyATS и Genie используют файл YAML, чтобы знать, к каким устройствам подключаться и каковы соответствующие учетные данные. Этот файл известен как testbed. Genie включает встроенную функциональность для создания testbed для вас.
Введите команду `genie --help`, чтобы увидеть все доступные команды. Для получения дополнительной справки по любой команде используйте параметр <команда>, как показано ниже для команды create. Обратите внимание, что testbed является одним из параметров команды create.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ genie --help
Usage:
  genie <command> [options]

Commands:
    create              Create Testbed, parser, triggers, ...
    diff                Command to diff two snapshots saved to file or directory
    dnac                Command to learn DNAC features and save to file (Prototype)
    learn               Command to learn device features and save to file
    parse               Command to parse show commands
    run                 Run Genie triggers & verifications in pyATS runtime environment
    shell               enter Python shell, loading a pyATS testbed file and/or pickled data

General Options:
  -h, --help            Show help

Run 'genie <command> --help' for more information on a command.
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ genie create --help
Usage:
  genie create <subcommand> [options]

Subcommands:
    parser              create a new Genie parser from template
    testbed             create a testbed file automatically
    trigger             create a new Genie trigger from template

General Options:
  -h, --help            Show help
  -v, --verbose         Give more output, additive up to 3 times.
  -q, --quiet           Give less output, additive up to 3 times, corresponding to WARNING, ERROR,
                        and CRITICAL logging levels
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ 
```
Чтобы создать testbed YAML, введите приведенную ниже команду. Параметр --output создаст файл testbed.yml в каталоге с именем yaml. Каталог будет создан автоматически. Параметр --encode-password закодирует пароли в YAML-файле. Параметр interactive означает, что вам будет задан ряд вопросов. Ответьте "нет" на первые три вопроса. Затем дайте следующие ответы, чтобы создать файл testbed.yaml.
- Device hostname — должно соответствовать имени хоста устройства, которое для данной лабораторной работы является CSR1kv.
- IP адрес — адрес должен соответствовать IPv4 адресу CSR1kv, который вы обнаружили ранее в этой лаборатории. Здесь показан 192.168.56.101.
- Username — локальное имя пользователя, используемое для ssh.
- Default password — локальный пароль, используемый для ssh.
- Enable password — Оставьте пустым. На маршрутизаторе не настроен привилегированный пароль.
- Protocol — SSH вместе с группой обмена ключами, ожидаемой маршрутизатором.
- OS — ОС на маршрутизаторе.

```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ genie create testbed interactive --output yaml/testbed.yml --encode-password
Start creating Testbed yaml file ...
Do all of the devices have the same username? [y/n] n
Do all of the devices have the same default password? [y/n] n
Do all of the devices have the same enable password? [y/n] n

Device hostname: CSR1kv
   IP (ip, or ip:port): 192.168.56.101
   Username: cisco
Default Password (leave blank if you want to enter on demand): cisco123!
Enable Password (leave blank if you want to enter on demand): 
   Protocol (ssh, telnet, ...): ssh -o KexAlgorithms=diffie-hellman-group14-sha1
   OS (iosxr, iosxe, ios, nxos, linux, ...): iosxe
More devices to add ? [y/n] n
Testbed file generated: 
yaml/testbed.yml 

(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```
С помощью cat просмотрите файл testbed.yml в каталоге yaml. Обратите внимание на ваши записи в файле YAML. Ваш пароль SSH зашифрован, а пароль включения "попросит" пользователя ввести пароль, если он требуется.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ cat yaml/testbed.yml
```
```yaml
devices:
  CSR1kv:
    connections:
      cli:
        ip: 192.168.56.101
        protocol: ssh -o KexAlgorithms=diffie-hellman-group14-sha1
    credentials:
      default:
        password: '%ENC{w5PDosOUw5fDosKQwpbCmMKH}'
        username: cisco
      enable:
        password: '%ASK{}'
    os: iosxe
    type: iosxe
```
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ 
```

### Шаг 2: Используйте Genie для разбора вывода команды show ip interface brief в JSON.
Если вы еще не завершили лабораторную работу — установка виртуальной машины CSR1kv, вы зачем сюда поступали? Если вы уже завершили эту лабораторную работу, запустите ВМ CSR1kv сейчас.
На ВМ CSR1kv введите команду show ip interface brief из привилегированного режима exec. Ваш адрес может быть увеличен до другого адреса, отличного от 192.168.56.101. Запишите IPv4-адрес для вашей ВМ CSR1kv. Вы будете использовать его позже в лабораторной работе.
```shell
CSR1kv> en
CSR1kv# show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       192.168.56.101  YES DHCP   up                    up      
CSR1kv#
```
Используя testbed YAML, вызовите Genie для разбора неструктурированного вывода команды show ip interface brief в структурированный JSON. Эта команда включает команду IOS для разбора (show ip interface brief), testbed YAML (testbed.yml) и указанное устройство в файле тестовой площадки (CSR1kv).
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ genie parse "show ip interface brief" --testbed-file yaml/testbed.yml --devices CSR1kv
Enter enable password for device CSR1kv: <Enter>
2022-05-10T18:12:20: %UNICON-WARNING: Device 'CSR1kv' connection 'cli' does not have IP and/or port specified, ignoring
Device 'CSR1kv' connection 'cli' does not have IP and/or port specified, ignoring
  0%|                                                                                     | 0/1 [00:00<?, ?it/s]{
  "interface": {
    "GigabitEthernet1": {
      "interface_is_ok": "YES",
      "ip_address": "192.168.56.101",
      "method": "DHCP",
      "protocol": "up",
      "status": "up"
    }
  }
}
100%|█████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.22it/s]

(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ ^C
```

### Шаг 3: Используйте Genie для разбора вывода команды show version в JSON.
Для другого примера разберите неструктурированный вывод команды show version в структурированный JSON.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ genie parse "show version" --testbed-file yaml/testbed.yml --devices CSR1kv
Enter enable password for device CSR1kv: <Enter>
2022-05-10T18:13:20: %UNICON-WARNING: Device 'CSR1kv' connection 'cli' does not have IP and/or port specified, ignoring
Device 'CSR1kv' connection 'cli' does not have IP and/or port specified, ignoring
  0%|                                                                                     | 0/1 [00:00<?, ?it/s]{
  "version": {
    "chassis": "CSR1000V",
    "chassis_sn": "9K8P1OFYE3D",
    "compiled_by": "mcpre",
    "compiled_date": "Thu 30-Jan-20 18:48",
    "curr_config_register": "0x2102",
    "disks": {
      "bootflash:.": {
        "disk_size": "7774207",
        "type_of_disk": "virtual hard disk"
      },
      "webui:.": {
        "disk_size": "0",
        "type_of_disk": "WebUI ODM Files"
      }
    },
    "hostname": "CSR1kv",
    "image_id": "X86_64_LINUX_IOSD-UNIVERSALK9-M",
    "image_type": "production image",
    "last_reload_reason": "reload",
    "license_level": "ax",
    "license_type": "Default. No valid license found.",
    "main_mem": "2182252",
    "mem_size": {
      "non-volatile configuration": "32768",
      "physical": "3985032"
    },
    "next_reload_license_level": "ax",
    "number_of_intfs": {
      "Gigabit Ethernet": "1"
    },
    "os": "IOS-XE",
    "platform": "Virtual XE",
    "processor_type": "VXE",
    "returned_to_rom_by": "reload",
    "rom": "IOS-XE ROMMON",
    "rtr_type": "CSR1000V",
    "system_image": "bootflash:packages.conf",
    "uptime": "2 days, 6 hours, 26 minutes",
    "uptime_this_cp": "2 days, 6 hours, 27 minutes",
    "version": "16.9.5",
    "version_short": "16.9"
  }
}
100%|█████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.06it/s]

(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ 
```

## Часть 5: Использование Genie для сравнения конфигураций
> Как вы видели, Genie можно использовать для разбора команд show в структурированный json. Genie также можно использовать, для: 
> - Ежегодных снапшотов конфигураций и сравнивнения их между собой
> - Автоматизированного тестового деплоя в виртуальной среде для проверки перед развертыванием в проде.
> - Устранения неполадок в конфигурациях путем проведения сравнений между устройствами.
>
> В частях 5 и 6 вы увидите, как проводить сравнение между двумя различными выходами.

### Шаг 1: Добавьте IPv6-адрес к CSR1kv.
На виртуальной машине CSR1kv добавьте следующий адрес IPv6:
```shell
CSR1kv(config)# interface gig 1
CSR1kv(config-if)# ipv6 address 2001:db8:acad:56::101/64
```

### Шаг 2: Используйте Genie для проверки конфигурации и разбора вывода в JSON.
Разберите неструктурированный вывод команды show ipv6 interface в структурированный JSON. Используйте параметр --output для отправки вывода в каталог verify-ipv6-1. Обратите внимание, что в выводе Genie сообщает, что было создано два файла.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ genie parse "show ipv6 interface gig 1" --testbed-file yaml/testbed.yml --devices CSR1kv --output verify-ipv6-1
Enter enable password for device CSR1kv: <Enter>
2022-05-10T18:14:25: %UNICON-WARNING: Device 'CSR1kv' connection 'cli' does not have IP and/or port specified, ignoring
Device 'CSR1kv' connection 'cli' does not have IP and/or port specified, ignoring
100%|█████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.08it/s]
+==============================================================================+
| Genie Parse Summary for CSR1kv                                               |
+==============================================================================+
|  Connected to CSR1kv                                                         |
|  -  Log: verify-ipv6-1/connection_CSR1kv.txt                                 |
|------------------------------------------------------------------------------|
|  Parsed command 'show ipv6 interface gig 1'                                  |
|  -  Parsed structure: verify-ipv6-1/CSR1kv_show-ipv6-interface-              |
| gig-1_parsed.txt                                                             |
|  -  Device Console:   verify-ipv6-1/CSR1kv_show-ipv6-interface-              |
| gig-1_console.txt                                                            |
|------------------------------------------------------------------------------|
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```
Отобразите файлы, созданные Genie в каталоге verify-ipv6-1. Обратите внимание, что было создано два файла с одинаковыми именами, но один заканчивается на _console.txt, а другой на _parsed.txt. Имя каждого файла включает имя устройства и команду IOS, использованную в команде разбора Genie.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ ls -l verify-ipv6-1
total 16
-rw-rw-rw- 1 devasc devasc 9094 connection_CSR1kv.txt
-rw-rw-r-- 1 devasc devasc  745 мая 10 18:10 CSR1kv_show-ipv6-interface-gig-1_console.txt
-rw-rw-r-- 1 devasc devasc  877 мая 10 18:10 CSR1kv_show-ipv6-interface-gig-1_parsed.txt
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```
С помощью cat просмотрите содержимое файла _console.txt. Обратите внимание на глобальный одноадресный адрес IPv6, который вы настроили, и автоматический локальный адрес канала EUI-64.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ cat verify-ipv6-1/CSR1kv_show-ipv6-interface-gig-1_console.txt 
+++ CSR1kv: executing command 'show ipv6 interface gig 1' +++
show ipv6 interface gig 1
GigabitEthernet1 is up, line protocol is up
  IPv6 is enabled, link-local address is FE80::A00:27FF:FE73:D79F 
  No Virtual link-local address(es):
  Description: VBox
  Global unicast address(es):
    2001:DB8:ACAD:56::101, subnet is 2001:DB8:ACAD:56::/64 
  Joined group address(es):
    FF02::1
    FF02::1:FF00:101
    FF02::1:FF73:D79F
  MTU is 1500 bytes
  ICMP error messages limited to one every 100 milliseconds
  ICMP redirects are enabled
  ICMP unreachables are sent
  ND DAD is enabled, number of DAD attempts: 1
  ND reachable time is 30000 milliseconds (using 30000)
  ND NS retransmit interval is 1000 milliseconds
CSR1kv#
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```
Используйте cat для изучения содержимого файла _parsed.txt. Это разобранный JSON-файл команды show ipv6 interface gig 1.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ cat verify-ipv6-1/CSR1kv_show-ipv6-interface-gig-1_parsed.txt 
```
```json
{
  "GigabitEthernet1": {
    "enabled": true,
    "ipv6": {
      "2001:DB8:ACAD:56::101/64": {
        "ip": "2001:DB8:ACAD:56::101",
        "prefix_length": "64",
        "status": "valid"
      },
      "FE80::A00:27FF:FE73:D79F": {
        "ip": "FE80::A00:27FF:FE73:D79F",
        "origin": "link_layer",
        "status": "valid"
      },
      "enabled": true,
      "icmp": {
        "error_messages_limited": 100,
        "redirects": true,
        "unreachables": "sent"
      },
      "nd": {
        "dad_attempts": 1,
        "dad_enabled": true,
        "ns_retransmit_interval": 1000,
        "reachable_time": 30000,
        "suppress": false,
        "using_time": 30000
      }
    },
    "joined_group_addresses": [
      "FF02::1",
      "FF02::1:FF00:101",
      "FF02::1:FF73:D79F"
    ],
    "mtu": 1500,
    "oper_status": "up"
  },
  "_exclude": []
}
```
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ 
```

### Шаг 3: Измените IPv6 Link-Local адрес.
На виртуальной машине CSR1kv добавьте следующий адрес IPv6:
```shell
CSR1kv> en
CSR1kv# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
CSR1kv(config)# interface gig 1
CSR1kv(config-if)# ipv6 address fe80::56:1 link-local
```

### Шаг 4: Используйте Genie для проверки конфигурации и разбора вывода в JSON.
Разберите неструктурированный вывод команды show ipv6 interface в структурированный JSON. Используйте параметр --output для отправки вывода в другой каталог verify-ipv6-2. Вы можете использовать историю команд для вызова предыдущей команды (стрелка вверх). Убедитесь, что вы изменили 1 на 2, чтобы создать новый каталог verify-ipv6-2.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ genie parse "show ipv6 interface gig 1" --testbed-file yaml/testbed.yml --devices CSR1kv --output verify-ipv6-2
Enter enable password for device CSR1kv: <Enter>
2022-05-10T18:16:29: %UNICON-WARNING: Device 'CSR1kv' connection 'cli' does not have IP and/or port specified, ignoring
Device 'CSR1kv' connection 'cli' does not have IP and/or port specified, ignoring
100%|█████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.24it/s]
+==============================================================================+
| Genie Parse Summary for CSR1kv                                               |
+==============================================================================+
|  Connected to CSR1kv                                                         |
|  -  Log: verify-ipv6-2/connection_CSR1kv.txt                                 |
|------------------------------------------------------------------------------|
|  Parsed command 'show ipv6 interface gig 1'                                  |
|  -  Parsed structure: verify-ipv6-2/CSR1kv_show-ipv6-interface-              |
| gig-1_parsed.txt                                                             |
|  -  Device Console:   verify-ipv6-2/CSR1kv_show-ipv6-interface-              |
| gig-1_console.txt                                                            |
|------------------------------------------------------------------------------|

(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ 
```
Отобразите файлы, созданные Genie в каталоге verify-ipv6-2. Они аналогичны двум файлам, которые вы создали перед изменением локального адреса канала IPv6.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ ls -l verify-ipv6-2
total 16
-rw-rw-rw- 1 devasc devasc 4536 мая 10 18:16 connection_CSR1kv.txt
-rw-rw-r-- 1 devasc devasc  728 мая 10 18:16 CSR1kv_show-ipv6-interface-gig-1_console.txt
-rw-rw-r-- 1 devasc devasc  846 мая 10 18:16 CSR1kv_show-ipv6-interface-gig-1_parsed.txt
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ 
```
Используйте cat для изучения содержимого каждого файла. Изменения выделены в выводе ниже.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ cat verify-ipv6-2/CSR1kv_show-ipv6-interface-gig-1_console.txt 
+++ CSR1kv: executing command 'show ipv6 interface gig 1' +++
show ipv6 interface gig 1
GigabitEthernet1 is up, line protocol is up
  IPv6 is enabled, link-local address is FE80::56:1 
  No Virtual link-local address(es):
  Description: VBox
  Global unicast address(es):
    2001:DB8:ACAD:56::101, subnet is 2001:DB8:ACAD:56::/64 
  Joined group address(es):
    FF02::1
    FF02::1:FF00:101
    FF02::1:FF56:1
  MTU is 1500 bytes
  ICMP error messages limited to one every 100 milliseconds
  ICMP redirects are enabled
  ICMP unreachables are sent
  ND DAD is enabled, number of DAD attempts: 1
  ND reachable time is 30000 milliseconds (using 30000)
  ND NS retransmit interval is 1000 milliseconds
CSR1kv#
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ cat verify-ipv6-2/CSR1kv_show-ipv6-interface-gig-1_parsed.txt 
```
```json
{
  "GigabitEthernet1": {
    "enabled": true,
    "ipv6": {
      "2001:DB8:ACAD:56::101/64": {
        "ip": "2001:DB8:ACAD:56::101",
        "prefix_length": "64",
        "status": "valid"
      },
      "FE80::56:1": {
        "ip": "FE80::56:1",
        "origin": "link_layer",
        "status": "valid"
      },
      "enabled": true,
      "icmp": {
        "error_messages_limited": 100,
        "redirects": true,
        "unreachables": "sent"
      },
      "nd": {
        "dad_attempts": 1,
        "dad_enabled": true,
        "ns_retransmit_interval": 1000,
        "reachable_time": 30000,
        "suppress": false,
        "using_time": 30000
      }
    },
    "joined_group_addresses": [
      "FF02::1",
      "FF02::1:FF00:101",
      "FF02::1:FF56:1"
    ],
    "mtu": 1500,
    "oper_status": "up"
  },
  "_exclude": []
}
```
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```

### Шаг 5: Используйте Genie для сравнения разницы между конфигурациями.
В предыдущем шаге довольно легко найти изменение локального адреса канала IPv6. Но предположим, что вы ищете проблему в сложной конфигурации. Возможно, вы пытаетесь найти различия между конфигурацией OSPF на маршрутизаторе, который получает правильные маршруты, и на другом маршрутизаторе, который их не получает, и вы хотите увидеть разницу в их конфигурациях OSPF.Возможно, вы пытаетесь найти разницу в длинном списке ACL-запросов между двумя маршрутизаторами, которые должны иметь идентичные политики безопасности. Genie может выполнить сравнение за вас и облегчить поиск различий.
Используйте следующую команду, чтобы Genie нашел различия между двумя разобранными JSON-файлами. Обратите внимание, что в выводе указано, где вы можете найти сравнения Genie. В данном случае первое имя файла — это предыдущая конфигурация, а второе имя файла — текущая конфигурация.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ genie diff verify-ipv6-1 verify-ipv6-2
1it [00:00, 579.32it/s]
+==============================================================================+
| Genie Diff Summary between directories verify-ipv6-1/ and verify-ipv6-2/     |
+==============================================================================+
|  File: CSR1kv_show-ipv6-interface-gig-1_parsed.txt                           |
|   - Diff can be found at ./diff_CSR1kv_show-ipv6-interface-gig-1_parsed.txt  |
|------------------------------------------------------------------------------|
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ 
```
Используйте cat для просмотра содержимого файла с различиями. Знак плюс "+" указывает на добавления, а знак минус "-" — на то, что было удалено.
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ cat ./diff_CSR1kv_show-ipv6-interface-gig-1_parsed.txt
--- verify-ipv6-1/CSR1kv_show-ipv6-interface-gig-1_parsed.txt
+++ verify-ipv6-2/CSR1kv_show-ipv6-interface-gig-1_parsed.txt
 GigabitEthernet1:
  ipv6:
+  FE80::56:1: 
+   ip: FE80::56:1
+   origin: link_layer
+   status: valid
-  FE80::A00:27FF:FE73:D79F: 
-   ip: FE80::A00:27FF:FE73:D79F
-   origin: link_layer
-   status: valid
  joined_group_addresses:
-  index[2]: FF02::1:FF73:D79F
+  index[2]: FF02::1:FF56:1
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$
```

## Часть 6: Завершение лабораторной и дальнейшие исследования
> В этой части вы деактивируете Python venv и изучите другие варианты использования Genie.

### Шаг 1: Деактивируйте виртуальную среду Python.
После завершения этой лабораторной работы вы можете деактивировать виртуальную среду Python с помощью команды deactivate. Заметьте, что перед prompt больше не стоит "(csr1kv)".
```shell
(csr1kv) devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ deactivate
devasc@labvm:~/labs/devnet-src/pyats/csr1kv$ 
```

### Шаг 2: Изучите больше примеров использования pyATS и Genie.
Ранее в этой лаборатории вы клонировали папку с примерами из репозитория Cisco Test Automation with pyATS and Genie на GitHub.
В этом репозитории GitHub есть много других примеров использования. Возможно, вы захотите изучить другие папки и различные другие примеры использования. Дополнительную информацию можно найти на следующих веб-сайтах:
- Поиск: "NetDevOps validation using Cisco pyATS | Genie for network engineers: no coding necessary". 
- Cisco GitHub: `https://github.com/CiscoTestAutomation` 
