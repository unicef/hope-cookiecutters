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
	@cd ${PROJECT_DIR} && .venv/bin/tox
	@cd ${PROJECT_DIR} && .venv/bin/python manage.py check
