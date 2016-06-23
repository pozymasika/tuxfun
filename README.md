# tuxfun (beta)
A minimalistic pluggable Blog application that you can easily reuse in your Django Project

Overview
---------
It has a simple pure Django backend, best under Python 2.7.x  or 3.x
I used a MySQL backend but you can get an RDBMS of your choice
The database API's for MySQL and PostgreSQL are mysqldb and psycopg respetively

Frontend technologies
---------------------
The frontend has HTML5, CSS3 and JavaScript.

Libraries
---------
The app is bundled with Bootstrap v3.0.1, jQuery and Quill.js (broken)

Installation
------------
- Clone this app to your local development environment
- ``cd  tuxfun/ `` and run  ``pip install -r requirements.txt``
- `` cd tuxfun/tuxfun `` and edit your ``settings.py`` file:
- Change the **DATABASE NAME**, **USER** and **PASSWORD**
-  ``cd  tuxfun/ `` and run:
- `` python manage.py migrate 0001_initial `` to install your models
- `` python manage.py migrate blog 0002_blog_category `` to install your updated models
- Run the server  `` python manage.py runserver 8000 ``
- In your browser, got to ``http://localhost:8000/blog/home``

