# Tree Menu App
Database diagram
![alt text](https://ibb.co/mFM8k6c)

## Setup
The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/nurlan5t/menuapp.git
$ cd menuapp
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ source venv/bin/activate

```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Create a `.env` file in your base directory (where manage.py is).

Add your `SECRET_KEY` to .env file.
For example:
SECRET_KEY = 'django-insecure-jqx&mb49hn8h*r774y1dhnf!4g)gu0va@sl+uz6uy6h$fw3p8y'

Create an admin:

```sh
(venv)$ python manage.py createsuperuser
```

Once `pip` has finished downloading the dependencies:
```sh
(venv)$ python manage.py runserver
```
