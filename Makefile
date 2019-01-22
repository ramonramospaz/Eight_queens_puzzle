SHELL := bash
DOCKER=docker-compose

clean-pyc:
		find . -name '__pycache__' -exec rm -r "{}" +
		find . -name '*.pyc' -delete
		find . -name '*~' -delete

docker-build: clean-pyc 
		$(DOCKER) build
		$(DOCKER) run queen

docker-test: clean-pyc
		$(DOCKER) -f docker-compose.test.yml run queen

docker-exec:
		$(DOCKER) run queen

docker-shell: 
		$(DOCKER) run queen bash

clean-docker: clean-pyc
		$(DOCKER) down --rmi local

.PHONY: clean-pyc docker-build docker-exec docker-shell clean-docker docker-test