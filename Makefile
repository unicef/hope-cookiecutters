clean:
	cd django-application && make clean
	cd django-project && make clean
	cd python-library && make clean


test:
	cd django-application && make test
	cd django-project && make test
	cd python-library && make test

build:
	@cd django-application && make build
	@cd django-project && make build
	@cd python-library && make build

i18n:
	@cd django-project && make i18n
