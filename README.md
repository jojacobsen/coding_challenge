# Coding Challenge

This application "Ship Management Project" with an Basic User Management System and REST API.

The API of this application will allow the user to perform CRUD (Create, Read, Update & Delete) operations on a ship. Each ship has a name (string), length (in metres), width (in metres) and code (a string with a format of AAAA-1111-A1 where A is any character from the Latin alphabet and 1 is a number from 0 to 9). 

![Travis (.com)](https://img.shields.io/travis/com/jojacobsen/coding_challenge)
[![Coverage Status](https://coveralls.io/repos/github/jojacobsen/coding_challenge/badge.svg?branch=main)](https://coveralls.io/github/jojacobsen/coding_challenge?branch=main)
![GitHub](https://img.shields.io/github/license/jojacobsen/coding_challenge)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

#Usage

## Getting Up and Running Locally With Docker

### Installation
This command will install all dependencies within the docker container. This will take a while, especially the first time you run this particular command on your development system:

    $ docker-compose -f local.yml build

Since a superuser is required in order to manage the database and the project, run following command:

    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

### Running the project locally

To get the docker container up an running enter following command:

    $ docker-compose -f local.yml up

To run in a detached (background) mode, use:

    $ docker-compose up -d

### Accessing the project

You will find the landing page of the project here: http://0.0.0.0:8000/

### Admin interface

Manage your application with the Django Admin interface. You can find it here and login with your superuser credentials: http://0.0.0.0:8000/admin

### Project overview

TODO 

### API overview

TODO 

### API usage

TODO 

## Development Commands

Useful commands for developing and maintaining this project:

### Type checks

Running type checks with mypy:

    $ mypy coding_challenge

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

#### Creating database migrations

To create migration files locally use following command:

    $ python manage.py makemigrations --settings=config.settings.local

The docker configuration will take care that these migration changes are applied in you database.
