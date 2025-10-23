WORKDIR:=../../cc_test_dir

PROJECT_NAME=django-project-sample

PROJECT_DIR="${WORKDIR}/${PROJECT_NAME}"


clean:
	@rm -fr ${WORKDIR}/*


build:
	@echo "Creating project in ${PROJECT_DIR}"

	@cookiecutter . \
		--replay-file=./replay-test.json \
		--overwrite-if-exists \
		--output-dir ${WORKDIR} \
		--keep-project-on-failure

test:
	@cd ${PROJECT_DIR} && .venv/bin/tox -r
	@cd ${PROJECT_DIR} && ADMIN_EMAIL= ADMIN_PASSWORD= ALLOWED_HOSTS= .venv/bin/python manage.py check
	@cd ${PROJECT_DIR} && DEBUG=1 .venv/bin/python manage.py develop


i18n: build
	@cd ${PROJECT_DIR} && \
		${PROJECT_DIR}/.venv/bin/python manage.py makemessages --locale es --locale fr --locale ar --locale pt --ignore '~*' && \
		cp -r ${PROJECT_DIR}/src/django_project_sample/LOCALE "${PWD}/{{cookiecutter.project_dir}}/src/{{cookiecutter.package_name}}"
	git add "${PWD}/{{cookiecutter.project_dir}}/src/{{cookiecutter.package_name}}/LOCALE/"
