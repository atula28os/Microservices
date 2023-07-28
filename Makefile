install:
	#install commands
	pip install --upgrade pip && \
	pip install -r requirements.txt 

format:
	#format code
	black mylib/*.py main.py
lint:
	#fake8
test:
	#test
deploy:
	#deploy

all: install link test deploy
