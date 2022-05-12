# Контроль версий программного обеспечения с помощью Git
![Иллюстрация к работе](../Resourses/README-LR-3-3-11.png)
## Цель лабораторной работы:
- Часть 1: Запуск виртуальной машины DEVASC
- Часть 2: Инициализация Git
- Часть 3: Постановка и фиксация файла в репозитории Git
- Часть 4: Управление файлом и отслеживание изменений
- Часть 5: Ветви и слияние
- Часть 6: Обработка конфликтов при слиянии
- Часть 7: Интеграция Git с GitHub

## Необходимые ресурсы:
- 1 ПК
- Virtual Box или VMWare
- DEVASC виртуальная машина

## Порядок выполнения работы
## Часть 1: Запуск виртуальной машины DEVASC
> Если вы еще не завершили лабораторную работу - Установка лабораторной среды виртуальной машины, сделайте это сейчас. Если вы уже завершили эту лабораторную работу, запустите виртуальную машину DEVASC.

## Часть 2: Инициализация Git
> В этой части вы инициализируете репозиторий Git.

### Шаг 1: Откройте терминал в DEVASC-LABVM.
Дважды щелкните значок эмулятора терминала на рабочем столе.
> Примечание: Автор будет выполнять все операции в терминале Visual Studio Code.

### Шаг 2: Инициализируем репозиторий Git.
Используйте команду ls для отображения списка текущего каталога. Помните, что команды чувствительны к регистру.
```shell
devasc@labvm:~$ ls
Desktop    Downloads  Music     Public  Templates
Documents  labs       Pictures  snap    Videos
devasc@labvm:~$
````

Далее настройте информацию о пользователе, которая будет использоваться для этого локального хранилища. Это позволит связать вашу информацию с работой, которую вы вносите в локальное хранилище. Используйте свое имя вместо "Имя Пользователяr" для имени в кавычках " ". Используйте @example.com для адреса электронной почты.

> Примечание: На данном этапе эти параметры могут быть любыми. Однако, когда вы сбросите эти глобальные значения в Части 7, вы будете использовать имя пользователя собственной учетной записи GitHub. Если хотите, вы можете использовать свое имя пользователя GitHub сейчас.

```shell
devasc@labvm:~$ git config --global user.name "SampleUser"
devasc@labvm:~$ git config --global user.email sample@example.com
````
В любой момент вы можете просмотреть эти настройки с помощью команды git config --list.
```shell
devasc@labvm:~$ git config --list
user.name=SampleUser
user.email=sample@example.com
devasc@labvm:~$
```
С помощью команды cd перейдите в папку devnet-src:
```shell
devasc@labvm:~$ cd labs/devnet-src/
devasc@labvm:~/labs/devnet-src$
```
Создайте каталог git-intro и перейдите в него:
```shell
devasc@labvm:~/labs/devnet-src$ mkdir git-intro
devasc@labvm:~/labs/devnet-src$ cd git-intro
devasc@labvm:~/labs/devnet-src/git-intro$
```
Используйте команду git init для инициализации текущего каталога (git-intro) в качестве репозитория Git. Появившееся сообщение указывает на то, что вы создали локальный репозиторий внутри вашего проекта, содержащийся в скрытом каталоге .git. Именно здесь находится вся история изменений. Вы можете увидеть ее с помощью команды ls -a.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git init
Initialized empty Git repository in /home/devasc/labs/devnet-src/git-intro/.git/
devasc@labvm:~/labs/devnet-src/git-intro$ ls -a
.  ..  .git
devasc@labvm:~/labs/devnet-src/git-intro$
```

В процессе работы над проектом вы захотите проверить, какие файлы изменились. Это полезно, когда вы фиксируете файлы в репозитории, но не хотите коммитить их все. Команда git status отображает измененные файлы в рабочем каталоге, которые помещены в очередь для следующих коммитов.

Это сообщение сообщает вам: 
- Что вы находитесь на ветке master. (Ветви обсуждаются позже в этой лабораторной работе).
- Сообщение о коммите - Initial commit.
- Для коммита ничего не изменилось.
Вы увидите, что статус вашего репозитория изменится, как только вы добавите файлы и начнете вносить изменения.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
devasc@labvm:~/labs/devnet-src/git-intro$ 
```

## Часть 3: Staging и Commiting файла в хранилище
> В этой части вы создадите файл, застэджите этот файл и закоммитите его в репозитории Git.

### Шаг 1: Создайте файл.
Репозиторий git-intro создан, но пуст. Используя команду echo, создайте файл DEVASC.txt с информацией, заключенной в кавычки.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ echo "Я на пути к успешной сдаче экзамена Cisco DEVASC" > DEVASC.txt
devasc@labvm:~/labs/devnet-src/git-intro$
```
С помощью команды ls -la убедитесь, что файл, а также каталог .git находятся в каталоге git intro.  Затем с помощью команды cat отобразите содержимое файла DEVASC.txt.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ ls -la
total 16
drwxrwxr-x 3 devasc devasc 4096 Apr 17 20:38 .
drwxrwxr-x 5 devasc devasc 4096 Apr 17 19:50 ..
-rw-rw-r-- 1 devasc devasc   48 Apr 17 20:38 DEVASC.txt
drwxrwxr-x 7 devasc devasc 4096 Apr 17 19:57 .git
evasc@labvm:~/src/git-intro$ cat DEVASC.txt
```
Я на пути к успешной сдаче экзамена Cisco DEVASC
```shell
devasc@labvm:~/labs/devnet-src/git-intro$
```

### Шаг 2: Изучите статус репозитория.
Изучите состояние репозитория с помощью git status. Обратите внимание, что Git нашел новый файл в каталоге и знает, что он не отслеживается.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
 DEVASC.txt

nothing added to commit but untracked files present (use "git add" to track)
devasc@labvm:~/labs/devnet-src/git-intro$ 
```

### Шаг 3: Постановка файла.
Далее используйте команду git add для "постановки" файла DEVASC.txt. Постановка - это промежуточный этап перед фиксацией файла в хранилище с помощью команды git commit. Эта команда создает снимок содержимого файла на момент ввода этой команды. Любые изменения в файле требуют еще одной команды git add перед фиксацией файла.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git add DEVASC.txt
```
Снова используя команду git status, обратите внимание на поэтапные изменения, отображаемые как "новый файл: DEVASC.txt".
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
 new file:   DEVASC.txt

devasc@labvm:~/labs/devnet-src/git-intro$
```
## Шаг 4: Коммит файла.
Теперь, когда вы поставили свои изменения, вам нужно зафиксировать их, чтобы сообщить Git'у, что вы хотите начать отслеживать эти изменения. Зафиксируйте ваш этапный контент как новый снимок фиксации с помощью команды git commit. Переключатель -m message позволяет добавить сообщение, объясняющее сделанные изменения. Обратите внимание на комбинацию цифр и букв, выделенную в выводе. Это и есть идентификатор фиксации. Каждый коммит идентифицируется уникальным хэшем SHA1. ID фиксации - это первые 7 символов полного хэша фиксации. Ваш ID фиксации будет отличаться от отображаемого.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git commit -m "Коммичу DEVASC.txt для начала отслеживания изменений"
[master (root-commit) 2008010] Коммичу DEVASC.txt для начала отслеживания изменений 1 file changed, 1 insertion(+)
 create mode 100644 DEVASC.txt
devasc@labvm:~/labs/devnet-src/git-intro$ 
```

### Шаг 5: Просмотр истории фиксации.
Используйте команду `git log`, чтобы показать все коммиты в истории текущей ветви. По умолчанию все коммиты делаются в ветке master. (Ветви будут обсуждаться позже.) Первая строка - это хэш фиксации с идентификатором фиксации в виде первых 7 символов. Файл зафиксирован в ветке master. Далее следует ваше имя и адрес электронной почты, дата фиксации и сообщение, которое вы приложили к фиксации.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git log
commit 2008010d883515b55a401ac1820e4335f848400a (HEAD -> master)
Author: Sample User <sample@example.com>
Date:  Mon Apr 18 18:03:28 2022 +0000

Коммичу DEVASC.txt для начала отслеживания изменений
devasc@labvm:~/labs/devnet-src/git-intro$
```

## Часть 4: Изменение файла и отслеживание изменений
> В этой части вы измените файл, застэйжите файл, закоммитите его и проверите изменения в хранилище.

### Шаг 1: Измените файл.
Внесите изменения в файл DEVASC.txt с помощью команды echo. Обязательно используйте ">>" для добавления существующего файла. Символ ">" перезапишет существующий файл. Используйте команду cat для просмотра измененного файла.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ echo "Я начинаю понимать Git!" >> DEVASC.txt
```
Используйте команду cat для просмотра измененного файла.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ cat DEVASC.txt
Я на пути к успешной сдаче экзамена Cisco DEVASC
Я начинаю понимать Git!
devasc@labvm:~/labs/devnet-src/git-intro$
```

### Шаг 2: Проверьте изменения в хранилище.
Проверьте изменения в хранилище с помощью команды `git status`.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
 modified:   DEVASC.txt

no changes added to commit (use "git add" and/or "git commit -a")
devasc@labvm:~/labs/devnet-src/git-intro$
```

### Шаг 3: Застэйджите измененный файл.
Измененный файл нужно будет снова застэйджить, прежде чем его можно будет закоммитить с помощью команды git add.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git add DEVASC.txt
```

### Шаг 4: Закоммитье застэйджите файл.
Зафиксируйте поэтапный файл с помощью команды `git commit`. Обратите внимание на новый идентификатор фиксации.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git commit -m "Добавлена дополнительная строка в файл"
[master 018a3f3] Добавлена дополнительная строка в файл
1 file changed, 1 insertion(+)
devasc@labvm:~/labs/devnet-src/git-intro$
```

### Шаг 5: Проверьте изменения в хранилище.
Снова используйте команду `git log`, чтобы показать все фиксации. Обратите внимание, что журнал содержит исходную запись о фиксации вместе с записью о фиксации, которую вы только что выполнили. Последняя фиксация показана первой. В выводе выделены ID фиксации (первые 7 символов SHA1-хэша), дата/время фиксации и сообщение о фиксации для каждой записи.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git log
commit 018a3f3b6afa53f7b465d4c7009b2e2975212558 (HEAD -> master)
Author: Sample User <sample@example.com>
Date:   Mon Apr 18 19:17:50 2022 +0000

    Добавлена дополнительная строка в файл

commit 2008010d883515b55a401ac1820e4335f848400a
Author: Sample User <sample@example.com>
Date:   Mon Apr 18 18:03:28 2022 +0000

    Коммичу DEVASC.txt для начала отслеживания изменений
devasc@labvm:~/labs/devnet-src/git-intro$
```
Если у вас есть несколько записей в журнале, вы можете сравнить два коммита с помощью команды `git diff`, добавив ID оригинального коммита первым, а ID последнего коммита - вторым: git diff <коммит-ID оригинальный>  <коммит-ID последний>. Вам нужно будет использовать свои идентификаторы коммитов. Знак "+" в конце, за которым следует текст, указывает на содержимое, которое было добавлено в файл.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git diff 018a3f3 2008010
```

## Часть 5: Ветви и слияние
> При создании репозитория файлы автоматически помещаются в ветвь, называемую master. По возможности рекомендуется использовать ветви, а не обновлять главную ветвь напрямую. Ветвление используется для того, чтобы вы могли вносить изменения в другую область, не затрагивая основную ветвь. Это делается для того, чтобы предотвратить случайные обновления, которые могут переписать существующий код. 
В этой части вы создадите новую ветвь, проверите ветвь, внесете изменения в ветвь, выполните этап и фиксацию ветви, объедините изменения ветви с основной ветвью, а затем удалите ветвь.

### Шаг 1: Создайте новую ветвь
Создайте новую ветку под названием feature с помощью команды `git branch <имя ветки>`.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git branch feature
```

### Шаг 2: Проверьте текущую ветку
Используйте команду `git branch` без указания имени ветви, чтобы отобразить все ветви для этого хранилища.  Символ "*" рядом с веткой master указывает на то, что это текущая ветка - ветка, которая в данный момент "проверяется".
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git branch
  feature
* master
devasc@labvm:~/labs/devnet-src/git-intro$ 
```

### Шаг 3: Проверьте новую ветку
Используйте команду `git checkout <имя ветки>` для перехода к ветке с функциями.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git checkout feature
```

### Шаг 4: Проверка текущей ветки
Убедитесь, что вы переключились на функциональную ветвь с помощью команды git branch. Обратите внимание на "*" рядом с веткой feature. Теперь это рабочая ветвь.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git branch
* feature
  master
devasc@labvm:~/labs/devnet-src/git-intro$ 
```
Добавьте новую строку текста в файл DEVASC.txt, снова используя команду echo со знаками ">>".
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ echo "Этот текст был добавлен первоначально, во время работы над функцией" >> DEVASC.txt
```
Проверьте, что строка была добавлена в файл с помощью команды cat.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ cat DEVASC.txt
```

### Шаг 5: Поместите измененный файл в функциональную ветвь.
Поместите обновленный файл в текущую функциональную ветвь.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git add DEVASC.txt
```
Используйте команду `git status` и заметите, что измененный файл DEVASC.txt помещен в ветку feature.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git status
On branch feature
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
 modified:   DEVASC.txt

devasc@labvm:~/labs/devnet-src/git-intro$ 
```

### Шаг 6: Закоммитьте стэйджовый файл в фиче ветке.
Зафиксируйте поэтапный файл с помощью команды `git commit`. Обратите внимание на новый идентификатор фиксации и ваше сообщение.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git commit -m "Добавлена третья строка в feature ветке"
[feature bcbc441] Добавлена третья строка в feature ветке
 1 file changed, 1 insertion(+)
devasc@labvm:~/labs/devnet-src/git-intro$ 
```
Используйте команду `git log`, чтобы показать все коммиты, включая коммит, который вы только что сделали в ветви feature.  Предыдущая фиксация была сделана в ветке master.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git log
```

### Шаг 7: Проверьте master-ветку.
Переключитесь на master-ветку с помощью команды `git checkout master` и проверьте текущую рабочую ветку с помощью команды git branch.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git checkout master
Switched to branch 'master'
devasc@labvm:~/labs/devnet-src/git-intro$ git branch
  feature
* master
devasc@labvm:~/labs/devnet-src/git-intro$ 
```

### Шаг 8: Объедините содержимое файлов из функциональной ветви в основную ветвь. 
Ветви часто используются при внедрении новых функций или исправлений. Они могут быть представлены на рассмотрение членам команды, а затем, после проверки, могут быть перенесены в основную кодовую базу - главную ветвь.
Слейте содержимое (известное как история) из ветки функций в главную ветку с помощью команды git merge <имя ветки>. Имя ветви - это ветвь, из которой истории перетягиваются в текущую ветвь. Вывод показывает, что один файл был изменен и вставлена одна строка.

Проверьте добавление содержимого в файл DEVASC.txt в основной ветви с помощью команды cat.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ cat DEVASC.txt
```

### Шаг 9: Удаление ветки.
Убедитесь, что фича ветка всё ещё доступна, используя команду `git branch`.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git branch
  feature
* master
devasc@labvm:~/labs/devnet-src/git-intro$ 
```
Удалите функциональную ветвь с помощью команды `git branch -d <имя-ветки>`.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git branch -d feature
Deleted branch feature (was bcbc441).
devasc@labvm:~/labs/devnet-src/git-intro$
Убедитесь, что фича ветка больше не доступна, используя команду git branch.
devasc@labvm:~/labs/devnet-src/git-intro$ git branch
* master
devasc@labvm:~/labs/devnet-src/git-intro$
```

## Часть 6: Обработка конфликтов слияния
> Иногда может возникнуть конфликт слияния. Это происходит, когда вы внесли перекрывающиеся изменения в файл, а Git не может автоматически объединить изменения. 
В этой части вы создадите тестовую ветвь, измените ее содержимое, выполните постановку и фиксацию тестовой ветви, переключитесь на главную ветвь, снова измените содержимое, выполните постановку и фиксацию главной ветви, попытаетесь объединить ветви, обнаружите и разрешите конфликт, снова выполните постановку и фиксацию главной ветви и проверите свою фиксацию.

### Шаг 1: Создайте тестовую ветку.
Создайте новую ветку test.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git branch test
```

### Шаг 2: Переключитесь на ветку тест.
Проверьте (переключитесь на) ветку test.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git checkout test
Switched to branch 'test'
devasc@labvm:~/labs/devnet-src/git-intro$
```
Убедитесь, что рабочая ветвь является тестовой.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git branch
  master
* test
devasc@labvm:~/labs/devnet-src/git-intro$ 
```

### Шаг 3: Проверьте текущее содержимое файла DEVASC.txt.
Проверьте текущее содержимое файла DEVASC.txt. Обратите внимание, что первая строка включает слово "Cisco".
  
### Шаг 4: Измените содержимое файла DEVASC.txt в тестовой ветке.
Используйте команду `sed`, чтобы изменить слово "Cisco" на "NetAcad" в файле DEVASC.txt.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ sed -i 's/Cisco/NetAcad/' DEVASC.txt
```

### Шаг 5: Проверьте содержимое измененного файла DEVASC.txt в тестовой ветке.
Проверьте изменения в файле DEVASC.txt.

### Шаг 6: Поставьте и зафиксируйте тестовую ветку.
Поставьте и зафиксируйте файл одной командой `git commit -a`. Опция `-a` влияет только на файлы, которые были изменены и удалены. Она не влияет на новые файлы.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git commit -a -m "Замена Cisco на NetAcad"
[test 830eab9] Замена Cisco на NetAcad
 1 file changed, 1 insertion(+), 1 deletion(-)
devasc@labvm:~/labs/devnet-src/git-intro$
```

### Шаг 7: Проверьте мастер-ветку.
Проверьте (переключитесь на) master-ветку.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git checkout master
Switched to branch 'master'
devasc@labvm:~/labs/devnet-src/git-intro$
```
Убедитесь, что ветвь master является вашей текущей рабочей ветвью.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git branch
* master
  test
devasc@labvm:~/labs/devnet-src/git-intro$
```

### Шаг 8: Измените содержимое файла DEVASC.txt в основной ветви.
```shell
Используйте команду sed, чтобы изменить слово "Cisco" на "DevNet" в файле DEVASC.txt.
devasc@labvm:~/labs/devnet-src/git-intro$ sed -i 's/Cisco/DevNet/' DEVASC.txt
```

### Шаг 9: Проверьте содержимое измененного файла DEVASC.txt в основной ветви.
Проверьте изменения в файле.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ cat DEVASC.txt
```

### Шаг 10: Поставьте и зафиксируйте мастер-ветвь.
Застэйжите и зафиксируйте файл с помощью команды `git commit -a`.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git commit -a -m "Замена Cisco на DevNet"
```

### Шаг 11: Попытайтесь объединить тестовую ветвь с основной ветвью.
Попытка объединить историю тестовой ветки с основной веткой.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git merge test
Auto-merging DEVASC.txt
CONFLICT (content): Merge conflict in DEVASC.txt
Automatic merge failed; fix conflicts and then commit the result.
devasc@labvm:~/labs/devnet-src/git-intro$ 
```

### Шаг 12: Найдите конфликт.
Например удобно смотреть историю ветвления в приложении GitKraken или Fork, которое вы можете дополнительно установить.

А пока вернемся в терминал. Используйте команду `git log` для просмотра коммитов. Обратите внимание, что версия HEAD является основной ветвью. Это будет полезно на следующем этапе.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git log
С помощью команды cat просмотрите содержимое файла DEVASC.txt. Теперь файл содержит информацию, которая поможет вам найти конфликт. Версия HEAD (ведущая ветвь), содержащая слово "DevNet", конфликтует с версией тестовой ветви и словом "NetAcad".
devasc@labvm:~/labs/devnet-src/git-intro$ cat DEVASC.txt
<<<<<<< HEAD
Я на пути к успешной сдаче экзамена DevNet DEVASC
=======
Я на пути к успешной сдаче экзамена NetAcad DEVASC
>>>>>>> test
Я начинаю понимать Git!
Этот текст был добавлен первоначально, во время работы над функцией
devasc@labvm:~/labs/devnet-src/git-intro$
```
_Тоже самое мы можем наблюдать в GitKraken_

### Шаг 13: Вручную отредактируйте файл DEVASC.txt, чтобы удалить противоречивый текст.
Используйте команду vim для редактирования файла.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ vim DEVASC.txt 
```
С помощью стрелок вверх и вниз выберите нужную строку текста.  Нажмите dd (удалить) на следующих выделенных строках. dd удалит строку, на которой находится курсор.
```shell
<<<<<<< HEAD
Я на пути к успешной сдаче экзамена DevNet DEVASC
=======
Я на пути к успешной сдаче экзамена NetAcad DEVASC exam
>>>>>>> test
Я начинаю понимать Git!
Этот текст был добавлен первоначально, во время работы над функцией
```
Сохраните изменения в vim, нажав ESC, затем наберите : (двоеточие), затем wq и нажмите enter.
```shell
ESC
:
wq
<Enter or Return>
```

### Шаг 14: Проверьте свои правки в файле DEVASC.txt в основной ветви.
Проверьте изменения с помощью команды cat
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ cat DEVASC.txt
```

### Шаг 15: Застэйджите и зафиксируйте мастер-ветку.
Застэйджите и зафиксируйте DEVASC.txt в ветке master с помощью команды git commit -a.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git add DEVASC.txt
devasc@labvm:~/labs/devnet-src/git-intro$ git commit -a -m "Ручное слияние из тестовой ветки"
[master 22d3da4] Ручное слияние из тестовой ветки
devasc@labvm:~/labs/devnet-src/git-intro$ 
```

### Шаг 16: Проверьте коммит.
Используйте команду `git log` для проверки фиксации. При необходимости вы можете использовать q, чтобы выйти из отображения журнала git.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ git log
```

## Часть 7: Интеграция Git с GitHub
> До сих пор все изменения, которые вы внесли в свой файл, хранились на вашей локальной машине. Git работает локально и не требует центрального файлового сервера или облачного хостинга. Git позволяет пользователю локально хранить файлы и управлять ими. 
Хотя Git полезен для одного пользователя, интеграция локального репозитория Git с облачным сервером, таким как GitHub, полезна при работе в команде. Каждый член команды хранит копию репозитория на своей локальной машине и обновляет центральный облачный репозиторий для обмена любыми изменениями.
Существует довольно много популярных сервисов Git, включая GitHub, Stash от Atlassian и GitLab. Поскольку он легко доступен, в этих примерах вы будете использовать GitHub.

### Шаг 1: Создайте учетную запись GitHub.
Если вы не сделали этого ранее, перейдите на сайт github.com и создайте учетную запись GitHub. Если у вас есть учетная запись GitHub, перейдите к шагу 2.

### Шаг 2: Войдите в свою учетную запись GitHub.
Войдите в свою учетную запись GitHub.

### Шаг 3: Создайте репозиторий.
Выберите кнопку "New repository" или нажмите на значок "+" в правом верхнем углу и выберите "Новое хранилище". 
Создайте репозиторий, используя следующую информацию:
- **Имя репозитория:** devasc-study-team
- **Описание:** Совместная работа по материалам DEVASC
- **Публичный/частный:** Частный
- **Выбрать:** Create repository

### Шаг 4: Создайте новый каталог devasc-study-team
Если вы еще не находитесь в каталоге git-intro, перейдите в него сейчас.
```shell
devasc@labvm:~$ cd ~/labs/devnet-src/git-intro
```
Создайте новый каталог с именем devasc-study-team. Каталог не обязательно должен совпадать с именем хранилища.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ mkdir devasc-study-team
```

### Шаг 5: Измените каталог на devasc-study-team.
Используйте команду cd, чтобы изменить каталоги на devasc-study-team.
```shell
devasc@labvm:~/labs/devnet-src/git-intro$ cd devasc-study-team
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$
```

### Шаг 6: Скопируйте файл DEVASC.
С помощью команды cp скопируйте файл DEVASC.txt из родительского каталога git-intro в подкаталог devasc-study-team.  Две точки и косая черта перед именем файла указывают на родительский каталог. Пробел и точка после имени файла указывают на копирование файла в текущий каталог с тем же именем.
```shell
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ cp ../DEVASC.txt .
```
Проверьте, что файл был скопирован с помощью команды ls, а содержимое файла - с помощью команды cat.
```shell
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ ls
DEVASC.txt
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ cat DEVASC.txt
```

### Шаг 7: Инициализируйте новый Git-репозиторий.
Используйте команду git init для инициализации текущего каталога (devasc-study-team) в качестве репозитория Git. Появившееся сообщение указывает на то, что вы создали локальный репозиторий внутри вашего проекта, содержащийся в скрытом каталоге .git. Именно здесь находится вся история изменений.
```shell
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ git init
Initialized empty Git repository in /home/devasc/src/git-intro/devasc-study-team/.git/
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$
```
Затем проверьте свои глобальные переменные git с помощью команды `git config --list`.
```shell
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ git config --list
user.name=SampleUser
user.email=sample@example.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$
```
Если переменные `user.name` и `user.email` не соответствуют вашим учетным данным GitHub, измените их сейчас.
```shell
devasc@labvm:~$ git config --global user.name "Имя пользователя GitHub "
devasc@labvm:~$ git config --global user.email Адрес электронной почты GitHub
```

### Шаг 8: Соедините Git-репозиторий с репозиторием GitHub.
Используйте команду `git remote add`, чтобы добавить URL-адрес Git в качестве удаленного псевдонима. Значение "origin" указывает на вновь созданный репозиторий на GitHub. Используйте ваше имя пользователя GitHub в пути URL для github-username.
Примечание: Ваше имя пользователя чувствительно к регистру.
```shell
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ git remote add origin https://github.com/имя-пользователя-github-/devasc-study-team.git
```
Убедитесь, что удаленный репозиторий на github.com, связан с локальным.
```shell
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ git remote --verbose
origin https://github.com/username/devasc-study-team.git (fetch)
origin https://github.com/username/devasc-study-team.git (push)
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ 
```
Просмотрите журнал git. Ошибка указывает на отсутствие фиксаций.
```shell
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ git log
fatal: your current branch 'master' does not have any commits yet
```

### Шаг 9: Застэйджите и закоммитьте файл DEVASC.txt.
Используйте команду `git add` для стэджинга файла DEVASC.txt.
```shell
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ git add DEVASC.txt
```
Используйте команду git commit для коммита файла DEVASC.txt.
```shell
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ git commit -m "Добавлен файл DEVASC.txt в devasc-study-team"
[master (root-commit) c60635f] Добавлен файл DEVASC.txt в devasc-study-team
 1 file changed, 3 insertions(+)
 create mode 100644 DEVASC.txt
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$
```

### Шаг 10: Проверьте коммит.
Используйте команду `git log` для проверки фиксации.
```shell
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ git log
commit c60635fe4a1f85667641afb9373e7f49a287bdd6 (HEAD -> master)
Author: username <user@example.com>
Date:  Thu Apr 28 23:41:08 2022 +0000

    Добавлен файл DEVASC.txt в devasc-study-team
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ 
```
Используйте команду `git status` для просмотра информации о состоянии. Фраза "working tree clean" означает, что Git сравнил ваш список файлов с тем, что вы сообщили Git'у, и это чистый лист, на котором нет ничего нового.
```shell
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ git status
On branch master
nothing to commit, working tree clean
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$
```

### Шаг 11: Запушьте файл из Git в GitHub.
Используйте команду `git push origin master` для отправки (push’а) файла в ваш репозиторий GitHub. Вам будет предложено ввести имя пользователя и пароль, которые вы использовали при создании учетной записи GitHub.
```shell
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ git push origin master
Username for 'https://github.com': имя_пользователя
Password for 'https://username@github.com': пароль
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 2 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 347 bytes | 347.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/username/devasc-study-team.git
 * [new branch]      master -> master
devasc@labvm:~/labs/devnet-src/git-intro/devasc-study-team$ 
```

> Примечание: Если после ввода имени пользователя и пароля вы получаете фатальную ошибку о том, что репозиторий не найден, скорее всего, вы ввели неверный URL. Вам необходимо отменить команду git add командой git remote rm origin.

### Шаг 12: Проверьте файл на GitHub.
Зайдите в свою учетную запись GitHub и в разделе "Репозитории" выберите имя пользователя/devasc-study-team. 
Вы должны увидеть, что файл DEVASC.txt был добавлен в этот репозиторий GitHub. Нажмите на файл, чтобы просмотреть его содержимое. 
