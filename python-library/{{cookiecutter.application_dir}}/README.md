=============================
{{ cookiecutter.application_title }}
=============================


[![Test](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.application_dir}}/actions/workflows/test.yml/badge.svg)](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.application_dir}}/actions/workflows/test.yml)
[![Lint](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.application_dir}}/actions/workflows/lint.yml/badge.svg)](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.application_dir}}/actions/workflows/lint.yml)
[![codecov](https://codecov.io/github/{{cookiecutter.github_user}}/{{cookiecutter.application_dir}}/graph/badge.svg?token=FBUB7HML5S)](https://codecov.io/github/{{cookiecutter.github_user}}/{{cookiecutter.application_dir}})
[![Documentation](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.application_dir}}/actions/workflows/docs.yml/badge.svg)](https://{{cookiecutter.github_user}}.github.io/{{cookiecutter.application_dir}}/)
[![Pypi](https://badge.fury.io/py/{{cookiecutter.github_user}}-{{cookiecutter.application_dir}}.svg)](https://badge.fury.io/py/{{cookiecutter.github_user}}-{{cookiecutter.application_dir}})
[![Docker Pulls](https://img.shields.io/docker/pulls/{{cookiecutter.github_user}}/{{cookiecutter.application_dir}})](https://hub.docker.com/repository/docker/{{cookiecutter.github_user}}/{{cookiecutter.application_dir}}/tags)

Simple django app to expose system infos like libraries version, database server.

Easy to extend to add custom checks.

## Features


    - dump system informations
    - admin integration
    - API to add custom checks
    - simple echo
    - retrieve library version


## Quickstart

Install {{cookiecutter.package_name}}::

    pip install {{cookiecutter.package_name}}

put it in your `INSTALLED_APPS`::

    INSTALLED_APPS=[
        ...
        '{{cookiecutter.package_name}}'
    ]

add relevant entries in your url.conf::

    urlpatterns = (
        ....
        url(r'', include({{cookiecutter.package_name}}.urls)),
    )
