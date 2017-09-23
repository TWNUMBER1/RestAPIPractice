CURRENT_DIR:=$(shell PWD)
IMAGE_NAME=$(shell basename $(CURRENT_DIR))
TAG:="latest"
POSTGRESTAG:="latest"
USERNAME:=""
PWD:=""
REGISTRY=tsungchh
CMD:=

login:
	docker login

stop:
	docker ps | grep "${REGISTRY}/${IMAGE_NAME}" | awk '{print $$1}' | xargs docker stop

rmc:
	docker ps -a | grep "${REGISTRY}/${IMAGE_NAME}" | awk '{print $$1}' | xargs docker rm

rmi:
	docker images | grep "${REGISTRY}/${IMAGE_NAME}" | awk '{print $$3}' | xargs docker rmi -f

rmdangling:
	docker images --quiet --filter "dangling=true" | xargs docker rmi

clean: stop rmc rmi rmdangling

build:
ifeq ($(TAG), "latest")
	docker build -t ${REGISTRY}/${IMAGE_NAME}:${TAG} .
else
	docker build -t ${REGISTRY}/${IMAGE_NAME}:latest . && \
	docker tag ${REGISTRY}/${IMAGE_NAME}:latest ${REGISTRY}/${IMAGE_NAME}:${TAG}
endif

push: build
ifeq ($(TAG),)
	docker push ${REGISTRY}/${IMAGE_NAME}:latest
else
	docker push ${REGISTRY}/${IMAGE_NAME}:${TAG} && docker push ${REGISTRY}/${IMAGE_NAME}:latest
endif

## for postgres ################

pullpostgres:
	docker pull tsungchh/postgres_docker:$(POSTGRESTAG)

runpostgres:
	docker run --name "postgres" -d --rm -p 5432:5432 tsungchh/postgres_docker:$(POSTGRESTAG)

rmipostgres:
	docker images | grep ${REGISTRY}/"postgres" | awk '{print $$3}' | xargs docker rmi -f

rmcpostgres:
	docker ps -a | grep ${REGISTRY}/"postgres" | awk '{print $$1}' | xargs docker rm 

stoppostgres:
	docker ps | grep ${REGISTRY}/"postgres" | awk '{print $$1}' | xargs docker stop 

cleanpostgres: stoppostgres rmcpostgres rmipostgres rmdangling

################################

cleanall: cleanpostgres clean

stopall: stop stoppostgres

depend: pullpostgres runpostgres

run: stop stoppostgres build depend
ifeq ($(CMD),)
	docker run -d --rm --link postgres:postgres -p 8000:8000 ${REGISTRY}/${IMAGE_NAME}:${TAG} ${CMD}
else
	docker run -it --rm --link postgres:postgres -p 8000:8000 ${REGISTRY}/${IMAGE_NAME}:${TAG} ${CMD}
endif

## docker-compose ################

dcrm:
	docker-compose down && rm -f

dcrun:
	docker-compose up --build -d

##################################

.PHONY: login rmc rmi rmdangling clean push  pullpostgres runpostgres  rmipostgres \
	rmcpostgres stoppostgres cleanpostgres cleanall depend build dcrm dcrun run
