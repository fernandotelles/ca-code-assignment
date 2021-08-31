setup:
	pipenv install --dev
	pipenv run python application/manage.py migrate
	pipenv shell

s: setup

run:
	python application/manage.py runserver 0.0.0.0:8080

r: run

test:
	pushd application &&\
	pytest &&\
	popd

t: test