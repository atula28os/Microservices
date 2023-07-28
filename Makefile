install:
	#install commands
	pip install --upgrade pip && \
	pip install -r requirements.txt 

format:
	#format code
lint:
	#fake8
test:
	#test
deploy:
	#deploy
	
all: install link test deploy
