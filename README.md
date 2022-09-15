# docs-system-control

##### Virtual environments
```angular2html
sudo apt-get install python-virtualenv
python3 -m venv venv
. venv/bin/activate
```


##### Install Dependencies
```angular2html
pip install -r requirements.txt
```


##### Running
```angular2html
export FLASK_APP=app.py
export FLASK_ENV=development
python -m flask run
```

This launches a very simple builtin server, which is good enough for testing but probably not what you want to use in production.

If you enable debug support the server will reload itself on code changes, and it will also provide you with a helpful debugger if things go wrong.

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line:

```angular2html
flask run --host=0.0.0.0
```

##### Alembic Migrations

```angular2html
flask db revision --autogenerate -m "description here"
flask db upgrade head
```

This project also uses the customized manager command to perform migrations.

````angular2html
python manage.py db revision --autogenerate -m "description here"
python manage.py db upgrade head
````


To upgrade the database with the newest migrations version, use:

```angular2html
python manage.py db upgrade head
```