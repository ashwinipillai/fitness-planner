Fitness Planner
===================

These are the major functions of Fitness Planner as a service:

1. Service that allows user creation and authentication
2. Users can create their own workout plans and Fitness goals
3. Users are enabled to track their goals and update weight tracking information

## Getting started
---
### Environment Setup

### Step 1: Setup local repository


Clone the repo

```bash
git clone [ENTERREPOLINKHERE]  #TODO: Enter repolink here
```


### Step 2: Setup external requisites

[Docker]

Ensure you have docker running in your machine. [If not, Go to Step 3]

[Docker run]

Run the following command, so docker can initialise on your local.

```bash
docker compose up
````


### Step 3: Setup In your local instead of DOCKER (This is in case docker is not required.)

Install Python 3.9 on your machine.

> Recommended to install [pyenv](https://github.com/pyenv/pyenv) and then install Python 3.9 using pyenv.

#### Linux:

Use your favourite package manager:

Ubuntu:
```bash
sudo apt install python3
```

Fedora:
```bash
sudo dnf install python3
```

RHEL/Centos:
```sh
sudo yum install python3
```

#### Windows:

Recommended to use a package manager like [chocolatey](https://chocolatey.org/) or [winget](https://github.com/microsoft/winget-cli)

OR

Directly [download Python](https://www.python.org/downloads/)

#### Mac

```bash
brew install python
```

>If you are a PyCharm user, run export LC_CTYPE=en_US.UTF-8 to avoid codec errors.
>Add it to your .bash_profile to set it automatically whenever you login


### Step 4: Install dependencies


```bash
pip install -r requirements.txt
```

> Problems installing typed_ast or psycopg2? Get prebuilt binaries from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/).

In case of M1 Mac, [install postgres using homebrew](https://formulae.brew.sh/formula/postgresql)

If you're unable to install uwsgi on an M1 Mac using pyenv, please use the below command to install:
```commandline
LDFLAGS=-L/opt/homebrew/Cellar/gettext/0.21/lib pip install --no-cache-dir "uWSGI==2.0.20"
```

### Step 5: Running the Django server

#### 5.1 Start Postgres

Prior to running the server, please ensure that you have your postgres server up and running. 

#### 5.2 Create Database fitness_tracker  [This needs to be done ONLY  if DB doesn't exist]
Ensure there is a DB called "fitness_tracker" created in your local postgres server.
```bash
psql -U your_admin_username -d your_default_database -c "CREATE DATABASE fitness_planner WITH OWNER postgres IF NOT EXISTS;"
```

#### 5.3 Set DB creds  [This needs to be done ONLY  if DB doesn't exist]
* Go to fitness_tracker/settings.py
* Update the DATABASES json to your local credentials for postgres.


#### 5.4 Apply Migrations  

```bash
python manage.py migrate
```

#### 5.4 Start the server

Fitness Tracker is a Django application.
To run the django server,

```bash
python manage.py runserver 0.0.0.0:8007
```

[Solutions Engg Onboarding]: https://outline.skit.ai/doc/solutions-engineer-onboarding-OuUiRimbbR
[Redis]: https://redis.io/topics/quickstart
[pyenv]: https://realpython.com/intro-to-pyenv/
[Mac]: https://gitlab.com/vernacularai/voice-services/integration-proxy/-/edit/master/README.md#mac
[Postgres DB]: https://www.postgresql.org/download/
