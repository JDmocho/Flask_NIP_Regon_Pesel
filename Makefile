SERVICE_NAME=flask_nip_regon_pesel

deps:
		pip install -r requirements.txt

lint:
		flake8 validator tests

test:
		py.test

test_cov:
		py.test --cov=validator --cov-report html ./

test_smoke:
		curl --fail 127.0.0.1:5000

run:
		python run.py

docker_build:
		docker build -t $(SERVICE_NAME)

docker_run:
		docker run --name $(SERVICE_NAME)-dev -p 5001:5000 -d $(SERVICE_NAME)

docker_stop:
		docker stop $(SERVICE_NAME)-dev

docker_push:
		docker login --username $(DOCKER_USERNAME) --password ${DOCKER_PASSWORD}; \
		docker tag $(SERVICE_NAME) $(DOCKER_USERNAME)/$(SERVICE_NAME); \
		docker push $(DOCKER_USERNAME)/$(SERVICE_NAME); \
		docker logout;






