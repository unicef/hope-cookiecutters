# {{cookiecutter.project_title}}


[![Test](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_dir}}/actions/workflows/test.yml/badge.svg)](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_dir}}/actions/workflows/test.yml)
[![Lint](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_dir}}/actions/workflows/lint.yml/badge.svg)](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_dir}}/actions/workflows/lint.yml)
[![codecov](https://codecov.io/github/{{cookiecutter.github_user}}/{{cookiecutter.project_dir}}/graph/badge.svg?token=FBUB7HML5S)](https://codecov.io/github/{{cookiecutter.github_user}}/{{cookiecutter.project_dir}})
[![Documentation](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_dir}}/actions/workflows/docs.yml/badge.svg)](https://{{cookiecutter.github_user}}.github.io/{{cookiecutter.project_dir}}/)
[![Pypi](https://badge.fury.io/py/{{cookiecutter.github_user}}-{{cookiecutter.project_dir}}.svg)](https://badge.fury.io/py/{{cookiecutter.github_user}}-{{cookiecutter.project_dir}})
[![Docker Pulls](https://img.shields.io/docker/pulls/{{cookiecutter.github_user}}/{{cookiecutter.project_dir}})](https://hub.docker.com/repository/docker/{{cookiecutter.github_user}}/{{cookiecutter.project_dir}}/tags)

{% if cookiecutter.use_transifex == "y" %}
## Translations

You can contribute to the Portal translation at https://app.transifex.com/{{cookiecutter.transifex_organization}}/{{cookiecutter.transifex_project}}/dashboard/
{% endif %}

## Contributing

### Requirements

- [uv](https://docs.astral.sh/uv/)
- [direnv](https://direnv.net/)

### Checkout and configure development environment

```shell

    git checkout https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.github_repo}}.git
    cd {{cookiecutter.github_repo}}
    uv venv .venv
    uv sync

    ./manage.py env --develop > .envrc  # create initial development configuration
    direnv allow .  # enable enviroment
    createdb {{ cookiecutter.database_name }}  # create postgres database on localhost

```
