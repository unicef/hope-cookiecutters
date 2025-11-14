WORKDIR:=../../cc_test_dir

PROJECT_NAME=django-project-sample

PROJECT_DIR="${WORKDIR}/${PROJECT_NAME}"

define PRINT_HELP_PYSCRIPT
import re, sys, os

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z0-9_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		help.format(**os.environ)
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


clean:  ## clean produced project dir
	@rm -fr ${WORKDIR}/*

.ONESHELL: run
.SHELLFLAGS: -e

${PROJECT_DIR}:
	@echo "Creating project in ${PROJECT_DIR}"
	@cookiecutter . \
		--replay-file=./replay-test.json \
		--overwrite-if-exists \
		--output-dir ${WORKDIR} \
		--keep-project-on-failure

build: ${PROJECT_DIR}  ## build project

test:  ## run project tests (tox)
	@cd ${PROJECT_DIR} && .venv/bin/tox -r
	@cd ${PROJECT_DIR} && ADMIN_EMAIL= ADMIN_PASSWORD= ALLOWED_HOSTS= .venv/bin/python manage.py check
	@cd ${PROJECT_DIR} && DEBUG=1 .venv/bin/python manage.py develop


run: build  ## performs runserver of the produced project
	@cd ${PROJECT_DIR} && . ${PROJECT_DIR}/.envrc && .venv/bin/python manage.py develop
	@cd ${PROJECT_DIR} && . ${PROJECT_DIR}/.envrc && .venv/bin/python manage.py runserver


i18n: build  ## check i18n messages for the template
	@cd ${PROJECT_DIR} && \
		${PROJECT_DIR}/.venv/bin/python manage.py makemessages --locale es --locale fr --locale ar --locale pt --ignore '~*' && \
		cp -r ${PROJECT_DIR}/src/django_project_sample/LOCALE "${PWD}/{{cookiecutter.project_dir}}/src/{{cookiecutter.package_name}}"
	git add "${PWD}/{{cookiecutter.project_dir}}/src/{{cookiecutter.package_name}}/LOCALE/"
