install:
	#install commands
	pip install --upgrade pip && \
	pip install -r requirements.txt 

format:
	#format code
	black mylib/*.py main.py
lint:
	#fake8
	pylint --disable=R,C mylib/*.py main.py
test:
	#test
	python -m pytest -vv --cov=mylib tests/test_*.py
deploy:
	#deploy

all: install link test deploy
