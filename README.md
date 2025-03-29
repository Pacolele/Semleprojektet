# Semmelfrossan 

This project was made using Django, HTMX and Tailwind CSS

## Prerequisites
For the prerequisites follow the guides avaiable for your machine to run this code.

* Postgresql
* Python
* Pip
* NPM

## Before running the project

To be able to run the project a python virtual environment is required. To do this run the venv command and then source it:

```
python -m venv venv
source venv/bin/activate
```

With the virutal environment activated proceed by running the pip install
```
pip install -r requirements.txt
```


## Setting up db with django

To setup the database so semlor can be added to DB we have to use migrate and makemigrations functions from Django.

```
createdb SEMLADB
python manage.py makemigrations
python manage.py migrate
```
### Populating DB
To add the relevant data to the database run this command:
```
python manage.py import_semlor_from_csv semlor.csv
```

#### DB errors
If there are reason the DB can't be accessed go into semlesite/settings.py to find the project settings and change the DATABASES USER field to your own name to be able to run the commands. 

To be able to access you r postgresql go into the interactive db like this:
```
psql postgres
```

Run these command:
```
\l
                                                       List of databases
   Name    |      Owner      | Encoding | Collate | Ctype | ICU Locale | Locale Provider |          Access privileges
-----------+-----------------+----------+---------+-------+------------+-----------------+-------------------------------------
 SEMLEDB   | elliothernesten | UTF8     | C       | C     |            | libc            |
 postgres  | elliothernesten | UTF8     | C       | C     |            | libc            |
 template0 | elliothernesten | UTF8     | C       | C     |            | libc            | =c/elliothernesten                 +
           |                 |          |         |       |            |                 | elliothernesten=CTc/elliothernesten
 template1 | elliothernesten | UTF8     | C       | C     |            | libc            | =c/elliothernesten                 +
           |                 |          |         |       |            |                 | elliothernesten=CTc/elliothernesten
(4 rows)

\du
                                      List of roles
    Role name    |                         Attributes                         | Member of
-----------------+------------------------------------------------------------+-----------
 ADMIN           | Create DB                                                  | {}
 elliothernesten | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

```
Enter the rolename with Superuser privelage in settings.py if it doesn't work.

## Running the django server
``` django
python manage.py runserver
```

## Start tailwind
For styling to work on the website the tailwind server has to be started without the page will look weird.
```
python manage.py tailwind build
python manage.py tailwind start
```

## Admin controls
To get admin access in django please run this command and input the relevant fields in the interactive interface then head to **localhost:8000/admin** and enter the credentials. 
```
python manage.py createsuperuser
```

From this page ratings can be added even if ip address gets blocked from main page.

## Project Structure

The project structure is simple for this project but it is possible to add more applications to the django and integrate them into the project. There is one app in this project called semlerating where most of the current relevant files reside in.

in semlerating/models.py there is the model structure for Django to add into the database and is used for a custom command to add semlor from csv files and also make relevant ratings connected to these semlor.
in semlerating/views.py there is the paths and urls which is generated and the backend logic resides. From these views there are 3 types of pages:

* Home page for semlerating: **localhost:8000/semlerating/**
* Page for all semlor: **localhost:8000/semlerating/semlor/**
* Detail page for semlor: **localhost:8000/semlerating/semlor/<semla_id>**

* Lastly there is the POST request url for performing ratings:
**localhost:8000/semlerating/semlor/rate/<semla_id>**


## Running tests
To run the tests we use djangos built in commands to run the test with:
```
python manage.py test
```

### Tree of project
```
.
├── README.md
├── manage.py
├── requirements.txt
├── semlerating
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── management
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   └── __init__.cpython-312.pyc
│   │   └── commands
│   │       ├── __init__.py
│   │       ├── __pycache__
│   │       │   ├── __init__.cpython-312.pyc
│   │       │   └── import_semlor_from_csv.cpython-312.pyc
│   │       └── import_semlor_from_csv.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_rating_comment.py
│   │   ├── 0003_rating_created_at_rating_ip_address_and_more.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-312.pyc
│   │       ├── 0002_rating_comment.cpython-312.pyc
│   │       ├── 0003_rating_created_at_rating_ip_address_and_more.cpython-312.pyc
│   │       └── __init__.cpython-312.pyc
│   ├── models.py
│   ├── static
│   │   └── semlerating
│   │       ├── babettes.jpg
│   │       ├── bostallet.jpg
│   │       ├── komet-kaffesemla.jpg
│   │       ├── komet.jpg
│   │       ├── lanemos.jpg
│   │       ├── linds.jpg
│   │       ├── melins.jpg
│   │       ├── normandie.jpg
│   │       ├── opennewdoors.jpg
│   │       ├── ronaldos.jpg
│   │       ├── simons.jpg
│   │       ├── stadsmissionen.jpg
│   │       ├── steinbrennernyberg.jpg
│   │       ├── svedjan.jpg
│   │       └── tossewrap.jpg
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── semlesite
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── settings.cpython-312.pyc
│   │   ├── urls.cpython-312.pyc
│   │   └── wsgi.cpython-312.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── semlor.csv
└── templates
    ├── base
    │   └── base.html
    ├── navbar
    │   └── navbar.html
    └── semlerating
        ├── form
        │   ├── base_form.html
        │   └── rate_form.html
        ├── index
        │   └── index.html
        └── semlor
            ├── partials
            │   └── semlor_list.html
            ├── semlor.html
            └── semlor_detail.html
```
