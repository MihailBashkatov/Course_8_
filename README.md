# Project Tracker for Good Habits

### Project is aimed to build SPA backend part

### To be able to start a project:

#### 1) Clone the repo to your machine
#### 2) Set up virtual environment
#### 3) Install requirements from requirements.txt, if use venv
#### 4) Create database Postgres
#### 5) Install redis
#### 6) Create .env file and add there all values from .env_sample
Genertate SECRET_KEY

    tr -dc 'A-Za-z0-9!#$%&\()*+,-./:;<=>?@[\]^_{|}~' </dev/urandom | head -c 50  ; echo
#### 7) Create Telegram Bot https://t.me/BotFather



#### To start a project, make sure you are in the folder, where repo is cloned run a command in terminal

    python manage.py runserver.

#### To create Superuser, run a command in terminal

    python manage.py createadmin

#### To create prepopulated database, run a command in terminal

    python manage.py add_database

#### Add your user profile

##### To be able to get a message via Telegram:
##### 1) create a Telagram Bot (step 5 and do not forget to add Token in .env file)
##### 2) Find out you Telegram ID (e.g via @userinfobot)
##### 3) Add field telegram_chat_id (Telegram ID) when you creating your profile 


#### Add habit. For that next fields are compulsory:

"habit_name"

"habit_place"

"habit_action"

habit_date" (format YYYY-MM-DD hh:mm)

"habit_time_duration" (reflected in seconds, max is 120 seconds)

#### Start celery and celery-beat command in terminal

    celery -A config worker --beat --scheduler django --loglevel=info


#### Project documentation is placed 
http://127.0.0.1:8000/swagger/

