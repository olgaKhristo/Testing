start with entering the shell:
pipenv shell

to install test:
pipenv install --dev pytest
pytest -h <=== to check if test loded

to run the test:
pytest 

for coverege
pipenv install pytest-cov
add line to pipfile:
cov="pytest --cov-report term-missing --cov=."
to run coverage:
pipenv run cov