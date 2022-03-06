# ![Shipping rulez](https://raw.githubusercontent.com/jojacobsen/coding_challenge/main/coding_challenge/static/images/favicons/favicon.ico) Coding Challenge


This project is a "Ship Management" application including a Basic User Management System and REST API.

The API of this application will allow the user to perform CRUD (Create, Read, Update & Delete) operations on a ship.
Each ship has a name (string), length (in metres), width (in metres) and code (a string with a format of AAAA-1111-A1
where A is any character from the Latin alphabet and 1 is a number from 0 to 9).

![Travis (.com)](https://img.shields.io/travis/com/jojacobsen/coding_challenge)
[![Coverage Status](https://coveralls.io/repos/github/jojacobsen/coding_challenge/badge.svg?branch=main)](https://coveralls.io/github/jojacobsen/coding_challenge?branch=main)
![GitHub](https://img.shields.io/github/license/jojacobsen/coding_challenge)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# Overview

## Used technologies

- *Python 3.9*
- *Django 3.2.12* (https://www.djangoproject.com/)
- *Django REST Framework 3.13* (https://www.django-rest-framework.org/  - *DRF*)
- *Postgres 14.1*

## Features

- REST API with Web browsable interface (http://0.0.0.0:8000/api/)
- Landing page with ship overview in table
- User management system (accessible via API)
- Ship management system designed for CRUD API usage
- Swagger API documentation (http://0.0.0.0:8000/api/docs/)
- and much more ...

# Usage

You can run the project in a Docker container (all necessary dependencies are installed automatically) or run it
locally (the dependencies need to be installed manually). Both options are described here:

## Getting Up and Running Locally With Docker

### Installation

This command will install all dependencies within the docker container. This will take a while, especially the first
time you run this particular command on your development system:

    $ docker-compose -f local.yml build

### Running the Project With Docker

To get the docker container up an running enter following command:

    $ docker-compose -f local.yml up

To run in a detached (background) mode, use:

    $ docker-compose up -d

Since a superuser is required in order to manage the database and the project, run following command:

    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

To run any migrations in your database use following command (this will be also executed when you simply run the
container):

    $ docker-compose -f local.yml run --rm django python manage.py migrate

## Getting Up and Running Locally

Make sure to have the following on your host:

- *Python 3.9*
- *PostgreSQL*

Create a new PostgreSQL database using createdb:

    $ createdb --username=postgres coding_challenge

Set the environment variables for the coding_challenge database and the project settings:

    $ export DATABASE_URL=postgres://postgres:<password>@127.0.0.1:5432/coding_challenge
    $ export DJANGO_SETTINGS_MODULE=config.settings.local
    $ export USE_DOCKER=no

Apply migrations:

    $ python manage.py migrate

Run the server:

    $ python manage.py runserver 0.0.0.0:8000

## General Project Usage  & Overview

### Accessing the Project

You will find the landing page of the project here: http://0.0.0.0:8000/ (or in some cases http://localhost:8000)

### Admin Interface

Manage your application with the Django Admin interface. You can find it here and login with your superuser
credentials: http://0.0.0.0:8000/admin

### Project Overview

The project comes with a landing page where there is a tabular view of all available ships, sorted by newest creation
date first.

These ships can be managed and created via a rest interface. Complex validation rules are enforced for the correctness
of the use of this interface. For example, the `code` field must be unique in the database and must conform to the
following regex `[a-zA-Z]{4}-[0-9]{4}-[a-zA-Z][0-9]$`. All `code` characters are stored uppercase in the database.

Furthermore, this project includes an interface for managing the user database.

All interfaces are documented in interactive API descriptions (see the following section).

### Project Structure

The program code follows the folder structure below (the most important):

    .
    ├── coding_challenge/         # Main project folder that inclues all applications
    │   ├── ship_manager/         # Ship Management application
    │   │   ├── api/              # Files regarding the API (serializers & views)
    │   │   ├── tests/            # Tests for this application
    │   │   ├── views/            # Non-API views
    │   │   ├── admin.py          # Admin interface configuration
    │   │   └── models.py         # Model definition
    │   ├── users/                # User application (strucure as above)
    │   ├── templates/             # Static templates
    │   └── conftest.py           # Test configurations
    ├── config/                   # Superior project configuration
    │   ├── settings/             # Folder for django settings (local, production, test & base)
    │   ├── api_router.py         # API router definition
    │   └── urls.py               # URL definition on project level
    ├── compose/                  # Dockerfiles
    ├── locale/                   # Translations
    ├── .envs/                    # Environment variables
    └── requirements/             # Python requirements (base, local & production)


### API Overview

There are two API interfaces with CRUD functionality:

1. `/api/users/` All user entries in the database can be managed via this endpoint.
2. `/api/ships/` In this endpoint new ships can be created, deleted, edited and a list of all ships can be displayed.

A detailed overview of the API endpoints, including all necessary parameters, can be viewed here:

1. http://0.0.0.0:8000/api/docs/  : Swagger Documentation
2. http://0.0.0.0:8000/api/  : Interactive DRF Documentation

### API Usage

To make an API request, the user must authenticate. The easiest way to do this is via token authentication.
Documentation on the exact implementation of DRF (Django Rest Framework) token authentication can be found
here: https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication

Here is a short step-by-step guide to obtain a token in this application and utilize it in an API request:

1. Log into the admin interface (admin access required) and go to the app Auth
   Token (http://0.0.0.0:8000/admin/authtoken/tokenproxy/).
2. Create an authentication token for your user.
3. To allow clients to authenticate, the token key should be included in the Authorization HTTP header. The key should
   be preceded by the string literal "token", with spaces separating the two strings. For example:

```
Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
```

An alternative way to get your authentication token is via the API interface `/auth-token/`. The following request must
be sent to obtain your token:

    $ curl -X POST -H "Content-Type: application/json" \
    -d '{"username": "myusername", "password": "mypassword"}' \
    http://0.0.0.0:8000/auth-token/

The response looks as follows:

```  
{"token":"9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"}
```   
### Project Documentation

It is intended to create user documentation. This documentation can be found here: http://0.0.0.0:9000/ (in Docker
operation). The documentation files can be found here `docs/`.

## Development Commands

Useful commands for developing and maintaining this project:

### Type checks

Running type checks with mypy:

    $ mypy coding_challenge

### Test Coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

### Running Tests with pytest

    $ pytest

### Creating Database Migrations

To create migration files locally use following command:

    $ python manage.py makemigrations

The docker configuration will take care that these migration changes are applied in your database, otherwise: 

    $ python manage.py migrate

### Python Shell Operations

If you wish to perform Python commands (e.g. Database operations) with all the underlying Django Project feature, do the following:

    $ python manage.py shell

### Load Initial Ship Data

To kickstart your project and directly have some data to play around with, there is a method to load initial ships. To do this, execute the following command: 

    $ python manage.py loaddata ships

## Troubleshooting

- [ ] Locally: Make sure to have the correct Python version all required Packages installed.
- [ ] Database issues: Make sure that your db is created & all migrations have been executed.
- [ ] Docker: Is Docker running?

## Acknowledgement

This project was created using the Django Rest Framework and Django Cookiecutter. 
