# Readme

Данный репозиторий содержит выполненное тестовое задание на позицию "Python-разработчик (Django, DRF)"

## Текст задания

**Задача**: Создайте сайт электронных объявлений.

Объявления делятся по категориям, в объявлении может быть одна фотография, заголовок и текст. Также в объявлении может быть указана цена (например, если это объявление о продаже чего-то). Объявление может относится к одной категории за раз.


У каждого объявления есть автор - пользователь, и три даты: дата создания, дата последнего редактирования и дата публикации.


Сразу после создания объявления недоступны для просмотра никому, кроме модераторов (сотрудники сайта), и имеют статус "На модерацию". Модератор может одобрить объявление или отклонить. Когда модератор одобряет объявление, оно становится опубликованным - у него меняется статус на "Опубликовано" и проставляется дата публикации. Когда модератор блокирует объявление - у него также меняется статус на "Отклонено", и оно больше нигде не выводится, кроме страницы пользователя, где видно только самому автору.


Авторизованные пользователи могут создавать новые объявления. Автор объявления может редактировать и удалять свои объявления. При редактировании статус объявления снова меняется на "На модерацию", если оно уже было опубликовано. Отклонённые объявления редактировать нельзя, только удалить. Удалённые объявления нигде не выводятся, но сохраняются в базе со статусом "На удаление".


У пользователей есть личные кабинеты, где они могут просмотреть свои собственные объявления. У пользователя должен быть указан телефон в профиле, который должен выводиться под его объявлениями. Телефон можно поменять на странице профиля. Перед сохранением номера - требуется проверять, что он соответствует маске +996 XXX XXX XXX


## Итого на сайте должны быть следующие страницы:

Главная страница - список объявлений. Здесь выводятся только одобренные объявления, отсортированные по дате публикации в убывающем порядке. Страница доступна всем пользователям, в т.ч. и анонимным. Ссылка сюда должна быть в меню.
Объявления на проверку - список объявлений. Здесь выводятся только новые объявления, отсортированные по дате создания в возрастающем порядке, для проверки модератором. Страница доступна только админу/модератору (is_staff). Ссылка сюда должна быть в меню, при входе в роли модератора.
Просмотр одного объявления. Страница для просмотра одного объявления. Здесь выводятся только одобренные объявления. Страница доступна всем пользователям, в т.ч. и анонимным. Сюда ведут ссылки с главной страницы.
Просмотр новых объявлений. Страница для просмотра одного объявления. Здесь выводятся только новые объявления, для проверки модератором. Страница доступна только админу/модератору (is_staff). Сюда ведут ссылки со страницы "Объявления на проверку". Объявление выводится так же, как на странице просмотра объявлений, но здесь должны быть две кнопки "Одобрить" и "Отклонить", которые по клику меняют статус объявления. Используйте JS и AJAX-запросы, чтобы реализовать эту задачу.
Создание объявления. Доступна только авторизованным пользователям. Ссылка сюда должна быть в меню.
Редактирование объявления. Доступна только автору. Ссылка на эту страницу должна быть на всех карточках объявлений на всех других страницах, где выводятся объявления (ссылка видна только автору).
Удаление объявления. Доступна только автору. Ссылка на эту страницу должна быть на всех карточках объявлений на всех других страницах, где выводятся объявления (ссылка видна только автору).
Страницы входа и выхода.
Личный кабинет. Доступен для просмотра всем пользователям, в т.ч. и анонимным. Для владельца страницы здесь выводятся все его объявления во всех статусах, кроме удалённых: новые, опубликованные, отклонённые. Для других пользователей здесь выводятся только опубликованные объявления этого автора. Имя пользователя на всех страницах должно быть ссылкой на его кабинет. Для текущего (вошедшего) пользователя в меню должна выводиться ссылка на его собственный личный кабинет.
Редактирование профиля. Здесь пользователь может поменять свой телефон. Страница доступна только владельцу профиля. Ссылка сюда выводится в его личном кабинете и видна только владельцу.

## Навигация:

Ссылка на главную страницу выводится в меню, видна всем.
Ссылка на страницу модерации, выводится в меню, видна только модератору.
Ссылка на просмотр объявления - выводится на каждой карточке объявления на главной и в профиле пользователя, видна всем.
Ссылка на просмотр объявления для модерации, выводится только на странице модерации.
Ссылка на создание объявления - выводится в главном меню, видна только авторизованным пользователям.
Ссылка на редактирование объявления - выводится под каждым объявлением на всех страницах, видна только автору объявления.
Ссылка на удаление объявления - выводится под каждым объявлением на всех страницах, видна только автору объявления.
Ссылки на профили пользователей - имена авторов объявлений на всех страницах являются ссылками на их профили.
Ссылка на профиль авторизованного пользователя - для авторизованных пользователей в меню должна быть ссылка "Мой профиль", ведущая на страницу их профиля.

## Указания:

Используйте базовый и включаемые шаблоны.
Стилизуйте сайт любым способом, но стилизация должна быть аккуратной - без прилипающих блоков и расползающегося текста. Как минимум, должен быть контейнер, выравнивание по рядам и колонкам и соблюдение отступов между элементами страницы.
Не забывайте создавать и отправлять миграции.
Сделайте и отправьте дамп данных, картинки от загруженных объявлений сожмите в архив и отправьте вместе с дампом.
Делайте небольшие коммиты после каждой задачи (модели, страницы, представления).
Все страницы для отображения списков объявлений должны иметь: поиск (по заголовку и описанию) и пагинацию
Приложение должно работать с СУБД PostgreSQL или MySQL
Приложение должно сопровождаться минимальным ридми, в котором нужно описать как поднимать приложение для разработки и данные для входа фикстурных пользователей. Над качеством разметки можно не заморачиваться, главное, чтобы всё было читаемо.
Бонус (+5 баллов).
Добавьте возможность для пользователей оставлять комментарии к объявлениям, используя форму, выводящуюся на странице просмотра одного объявления.


### Комментарии должны выводиться под объявлением по дате создания в убывающем порядке (более свежие - выше).


### В каждом комментарии должно выводиться имя автора, дата и текст комментария.




### На что будет обращаться внимание при проверке задания:

Полнота и качество реализации функционала
Чистота кода
Работа с системой контроля версий
Безопасность


## Установка

1. Клонируем репозиторий с гитхаба

    ```bash
    https://github.com/Gustaff0/project_test_for_fabrique.git
    ```

2. Выполняем миграцию базы данных

    ```bash
    ./manage.py migrate
    ```
3. Создаем PostgreSQL базу и подключаемся c помощью .env


4. Создаем администратора для django, или используем существующего

    ```bash
    ./manage.py createsuperuser
    ```
    
4. Запускаем сервер на локальном хосте

    ```bash
    ./manage.py runserver 
    ```
    
## Использование

Приложение запущенно и доступно на порту 8000

### Функционал для администратора системы

Функционал для администратора системы полностью реализован на админке django.

1. переходим на url http://127.0.0.1:8000/admin
2. авторизуемся под созданным нами администратором
3. переходим в раздел `Обьявления`
4. создаем, меняем удаляем обьявление.
5. так же иммунитет Администрации Доступно в самом Web-Приложении

### Функционал для Модератора
1. Может Создавать, Удалять, Менять и Подтверждать или Отклонять Обьявления на модерацию!
2. Имеет иммунитет Администратора в Web-Приложении но не в Админке

### Функционал для пользователей системы

Функционал для пользователей системы реализован в виде API.

## База данных

База данных в проекте используется postgres

