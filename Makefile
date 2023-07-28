install:
	#install commands
	pip install --upgrade pip && \
	pip install -r requirements.txt 
format:
	#format code
	black mylib/*.py main.py
lint:
	#fake8
	pylint --disable=R,C mylib/*.py main.py cli-fire.py
test:
	#test
	python -m pytest -vv --cov=mylib --cov=main tests/test_*.py
build:
	docker build -t fastapi-img .
deploy:
	#deploy
all: install link test deploy build