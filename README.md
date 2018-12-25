# RememberFit


# Instructions for Windows

### Table Of Contents
  1. Setting up environment.
    a. Virtual Environment.
    b. initializing a Django project to fetch the SECRET_KEY = ''.  
  2. Creating a database off of PostgreSQL.
  3. Clone the repository and create a .ENV in root dir.
  4. Install dependencies and makemigrations/migrate.
  5. Run a server and test the functionalities.
  



## Environment Setup

  Let's start off by opening our cmd prompt and type: `cd c:\users\<name>\desktop\ & mkdir testapp` that'll redirect you to the desktop and creates a directory called testapp. 
  Change into that dir and run `python -m venv venv` this creates our virtual env, go ahead and activate it: `venv\scripts\activate`.
  
  Open up a notepad and type in Django~=2.0.6 save as `requirements.txt` and close it. Back on your cmd type `pip install -r requirements.txt` this downloads the Django dependency we saved. 
  Finally we can create our project folder, we're still in on testapp folder so run: `django-admin.exe startproject getkey . ` this initializes the project folder called getkey. Open a file explorer to our testapp folder and click on the getkey/ open the settings.py in an editor. 
  When you have settings opened you should immediately see `SECRET_KEY = 'SAMPLE-KEY-COPY-THIS` COPY THAT ON A NOTE PAD. 
  
  
  
## Database

  Download PostgreSQL and create your `username` and `password` after installation open another cmd and type: `psql username postgres` followed by a password prompt. 
  Create your database, `create database rfdb;`, you need to save the `DB_NAME = 'rfdb', DB_USER = 'your-psql-username, DB_PASSWORD = '`your-db-pw` at the same place you jotted down your `SECRET_KEY = ''`. 
  
  

## Clone Repo and create .ENV
  
  With your notepad still opened, type the rest in:
  
  DB_NAME = 'rfdb'
  
  DB_USER = 'psql-username'
  
  DB_PASSWORD = 'psql-password'
  
  DB_HOST = 'localhost'
  
  DB_PORT = ''
  
  DEBUG = True
  
  SECRET_KEY = 'your-secret-key'
  
  Before we save that file, open or download the bash cmd the git tool belt, `cd c:/users/<name>/desktop/testapp/` and `git clone https://github.com/ecosimon/RememberFit.git`. 
  Now we can save that `.ENV` file in the root of the cloned dir: `/RememberFit/.ENV`. 
  
  
  
## Dependencies, migration/makemigrations

  Go to your windows cmd and cd to that dir and run the project's dependencies: `pip install -r requirements.txt`. 
  After the download run: `python manage.py makemigrations` and `python manage.py migrate`.
  
 
 
## Run a server localhost:8000

  Now we can run: `python manage.py runserver` open Chrome and type the address `localhost:8000`. 
 
 
  ## FIN
  
