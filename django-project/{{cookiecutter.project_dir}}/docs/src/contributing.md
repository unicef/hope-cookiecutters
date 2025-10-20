# Contributing


Install [uv](https://docs.astral.sh/uv/)


    git clone https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.github_repo}}
    uv venv .venv --python 3.12
    source .venv/bin/activate
    uv sync --all-extras
    pre-commit install --hook-type pre-commit --hook-type pre-push


## Run tests

    pytests tests

## Run Selenium tests (ONLY)

    pytests tests -m selenium


## Run Selenium any tests

    pytests tests --selenium


## Run local server


    ./manage.py runserver



## Docker compose

Alternatively you can use provided docker compose for development

    docker compose up

Alternatively you can use provided docker compose for development

    docker compose up
