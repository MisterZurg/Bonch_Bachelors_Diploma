# Установка виртуальной лабораторной среды

![Иллюстрация к работе](../Resourses/README-LR-1-1-2.png)

## Цель лабораторной работы:
- [Часть 1: Подготовка компьютера к Виртуализации](#Часть-1:-Подготовка-компьютера-к-Виртуализации)
- [Часть 2: Знакомство с DEVASC VM GUI](#Часть-2:-Знакомство-с-DEVASC-VM-GUI)
- [Часть 3: Создание Учётной записи для лабораторной среды](#Часть-3:-Создание-Учётной-записи-для-лабораторной-среды)
- [Часть 4: Установка Webex Teams на ваше устройство](#Часть-4:-Установка-Webex-Teams-на-ваше-устройство)

## Необходимые ресурсы:
- Хост-компьютер как минимум с 4 ГБ ОЗУ и 15 ГБ свободного дискового пространства.
- Высокоскоростной доступ в Интернет для загрузки Oracle VirtualBox и DEVASC VM

## Порядок выполнения работы:
## Часть 1: Подготовка компьютера к Виртуализации 
В этой части вы установите на программное обеспечение для виртуализации и DEVASC VM. Ваш инструктор предоставит вам файл DEVASC VM.

> **Примечание:** Описанные ниже действия исполнялись на Windows 10 используя VirtualBox v6.1.4. Ваши шаги могут отличаться.

Независимо от операционной системы или версии VirtualBox, убедитесь, что вы нашли и выбрали опции, указанные в следующих шагах.
Примечание: Если у вас установлен VirtualBox, вы можете перейти к Шагу 2.

### Шаг 1: Загрузка и установка VirtualBox.
VMware Player и Oracle VirtualBox — это две программы виртуализации, которые вы можете загрузить и установить для поддержки образов виртуальных машин. В этой лабораторной работе вы будете использовать программу VirtualBox.
-	Перейдите на сайт https://www.virtualbox.org/. На открывшейся странице, перейдите в раздел Downloads.
-	Выберите и загрузите соответствующий установочный файл VirtualBox в зависимости от вашей операционной системы.
-	Запустите установщик VirtualBox, выбрав в параметры устаноки по умолчанию.
-	Запустите VirtualBox, и переходите к следующему шагу.

### Шаг 2: Импорт DEVASC VM.
-	Перейдите на страницу DevNet Associate Virtual Machines (VMs) netacad.com.
-	Скачайте DEVASC_VM.OVA и запомните расположение загруженной виртуальной машины. 

> **Примечание:** На странице также расположен файл DEVASC_CSR1000v.zip. Сейчас нет необходимости его загружать. Для его установки требуется дополнительный файл, предоставляемый инструктором

-	В VirtualBox, выберете Файл > Импорт Конфигураций.
-	В поле Источник выберите Локальная файловая система. В поле Файл укажите путь до образа загруженной виртуальной машины DEVASC VM. И нажмите далее
-	Нажмите Импорт что бы продолжить. Сам процесс импорта займет какое-то время.

## Часть 2: Знакомство с DEVASC VM GUI
-	Запустите DEVASC VM. Это займет несколько минут, поскольку образ Ubuntu начнет загрузку. 
-	DEVASC VM содержит Packet Tracer. Вы должны согласиться с Cisco Packet Tracer EULA чтобы продолжить запуск VM. Когда вы увидите лицензионное соглашение используйте клавиши со стрелками для прокрутки текста. Нажмите клавишу со стрелкой вправо, чтобы выбрать, когда закончите. Нажмите клавишу пробела, чтобы перейти к экрану Соглашение. Нажмите клавишу со стрелкой влево, чтобы выбрать нужный пункт.
-	Образ Ubuntu продолжит загрузку. Закрывайте любые всплывающие сообщения. 
-	В следующих лабораторных, вы будете использовать терминал, VS Code, Packet Tracer, Браузер Chromium и Postman. Откройте эти приложения и познакомьтесь с ними. 

_Помните, что это виртуальная машина и она полностью отделена от компьютера, на котором она установлена. Вы можете вносить любые изменения. Если вы допустите ошибку или что-то сломаете, вы можете просто удалить виртуальную машину из VirtualBox и импортировать свежую копию из загруженного файла. Это отличный способ экспериментировать с программами, не затрагивая реальный компьютер. Не бойтесь исследовать и получать удовольствие!_

## Часть 3: Создание Учётной записи для лабораторной среды
Существует множество инструментов, которые вам понадобится использовать для выполнения лабораторных работ в этом курсе. Некоторые из них требуют наличия собственной учетной записи. Их легко настроить и можно сделать это бесплатно. В этой части вы создадите учетные записи, которые понадобятся вам в течение всего курса.

### Шаг 1: Создание учетной записи DevNet. 
- Откройте Браузер Chromium/FireFox и прейдите по адресу developer.cisco.com.
- Нажмите SIGN UP FREE. 
- Вы можете выбрать любой из типов входа, для которого у вас уже есть учетная запись. Это позволяет легко ассоциировать учетную запись с другими учетными записями. Если вы не хотите связывать свою учетную запись DevNet с другими приложениями, выберите Вход с помощью Cisco ID.
- Следуйте инструкциям чтобы продолжить создание учетной записи. 

### Шаг 2: Создание учетной записи GitHub. 
- Прейдите по адресу github.com и нажмите кнопку Sign Up. 
- Заполните поля Email, Password и Username и нажмите кнопку Continue.
-	Пройдите верификацию, того что вы человек. После чего нажмите кнопку Create Account
-	На открывшейся странице введите код, высланный на ваш e-mail, чтобы подтвердить свою учетную запись. 
- Проведите начальные настройки персонализации, или нажмите Skip personalization внизу страницы.

### Шаг 3: Создание учетной записи Webex. 
- Прейдите по адресу webex.com. 
- Нажмите Start for Free или Sign up now, it's free. 
- Введите Email. 
- Нажмите Sign Up. 
- Следуйте инструкциям чтобы продолжить создание учетной записи

### Шаг 4: Выключите VM. 
Когда вы закончите работу с ВМ, вы можете сохранить состояние машины ВМ для дальнейшего использования или закрыть ВМ. Закройте ВМ с помощью графического интерфейса пользователя:
- Из Virtual Box меню Файл, выберите Закрыть... 
- Нажмите радиокнопку Сохранить состояние машины и нажмите OK. При следующем запуске виртуальной машины вы сможете возобновить работу в операционной системе в ее текущем состоянии. Другие два варианта: 
  -	Отправьте сигнал выключения: Это имитирует нажатие кнопки питания на физическом компьютере.
  -	Выключите питание машины: Это имитирует выдергивание вилки из розетки на физическом компьютере. Закрытие ВМ с помощью CLI: Чтобы выключить ВМ с помощью командной строки, можно воспользоваться опциями меню внутри ВМ или ввести команду sudo shutdown -h now в окне терминала. Перезагрузка ВМ: Если вы хотите перезагрузить ВМ, вы можете воспользоваться опциями меню внутри ВМ или ввести команду sudo reboot в терминале. 

## Часть 4: Установка Webex Teams на ваше устройство
В этой части, вы установите Webex Teams

### Шаг 1: Загрузка и установка. 
-	Прейдите по адресу www.webex.com/downloads.html 
-	В разделе Webex Teams нажмите Загрузить для Windows, или вы можете выбрать установку Teams на мобильное устройство.
> **Примечание:** Для MacOS вы загрузите версию для Mac. На момент написания этой лабораторной работы настольного приложения для Linux не существует. Однако вы можете запустить Webex Teams в браузере. Нажмите Войти в верхней части и выберите Webex Teams. Затем войдите в систему, используя учетные данные новой учетной записи Webex. 

- Откройте установочный файл и следуйте инструкциям для завершения установки. 
### Шаг 2: Запуск Webex Teams. 
Откройте Webex Teams. Если ваш преподаватель уже создал команду, вы должны увидеть, что теперь являетесь ее членом. Если нет, то вы можете сделать одно из следующих действий: 
-	Сообщите преподавателю свой адрес электронной почты, чтобы вас можно было добавить в группу класса.  
-	Создайте свою собственную команду. На левой панели нажмите кнопку Команды. Затем нажмите кнопку с плюсом, чтобы Создать команду. Команда необходима для следующего шага. 

### Шаг 3: Добавление пользователя в Webex Teams. 
- В Webex Teams найдите пользователя в поле "Поиск". Вы можете искать по имени пользователя или электронной почте. Пользователь должен быть членом вашей команды. b. Щелкните пользователя в списке результатов поиска, чтобы открыть место.
- Введите сообщение для пользователя. Пользователь получит уведомление о вашем сообщении и сможет ответить на него.
