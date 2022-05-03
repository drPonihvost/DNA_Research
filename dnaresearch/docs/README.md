Журнал исследований (research):
1. Регистрация (редактирование) исследований в форме:
    Поля формы:
    - дата поступления материалов
    - инициатор (ФИО, должность, подразделение) 
    - исполнитель (ФИО, должность, подразделение)
    - событие (№ дела (с указанием категории: у/д, РД, КУСП и т.д.), состав преступления, дата происшествия, адрес происшествия, дата формирования материалов, статья УК РФ)
    - количество образцов
   Возможность ручного ввода и ввода с помощью сканера
2. Переход к таблице связанных с исследованием лиц 
3. Регистрация на исполнение:
    Добавляется номер исследования и дата регистрации (форма)
4. Экспорт в txt файл отмеченных исследований

Журнал проверяемых лиц (person):

Разверстка:
- cd .\dnaresearch\dnaresearch\
- python manage.py makemigrations
- python manage.py migrate
- python manage.py loaddata criminal_articles.json
- python manage.py loaddata research_data.json
- python manage.py runserver

env.dev
- DEBUG=1
- SECRET_KEY=foo
- DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
- SQL_ENGINE=django.db.backends.postgresql
- SQL_DATABASE=dnaresearch_dev
- SQL_USER=dnaresearch
- SQL_PASSWORD=dnaresearch
- SQL_HOST=db
- SQL_PORT=5432
- DATABASE=postgres

env.prod
- DEBUG=1
- SECRET_KEY=change_me
- DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
- SQL_ENGINE=django.db.backends.postgresql
- SQL_DATABASE=dnaresearch_prod
- SQL_USER=dnaresearch
- SQL_PASSWORD=dnaresearch
- SQL_HOST=db
- SQL_PORT=5432
- DATABASE=postgres

env.prod.db
- POSTGRES_USER=dnaresearch
- POSTGRES_PASSWORD=dnaresearch
- POSTGRES_DB=dnaresearch_prod