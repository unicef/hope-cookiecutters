WORKDIR:=../../cc_test_dir

PROJECT_NAME=django-project-sample

PROJECT_DIR="${WORKDIR}/${PROJECT_NAME}"


clean:
	@rm -fr ${WORKDIR}/*


build: clean
	@echo "Creating project in ${PROJECT_DIR}"

	@cookiecutter . \
		--replay-file=./replay-test.json \
		--overwrite-if-exists \
		--output-dir ${WORKDIR} \
		--keep-project-on-failure


test:
	cd ${PROJECT_DIR} && .venv/bin/pre-commit run --all-files
	cd ${PROJECT_DIR} && .venv/bin/python manage.py check
	cd ${PROJECT_DIR} && .venv/bin/tox -e pkg_meta
	cd ${PROJECT_DIR} && .venv/bin/tox -e lint
	cd ${PROJECT_DIR} && .venv/bin/tox -e mypy
	cd ${PROJECT_DIR} && .venv/bin/tox -e docs
	cd ${PROJECT_DIR} && .venv/bin/tox -e tests
