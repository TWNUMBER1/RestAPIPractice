CURRENT_DIR:=$(shell PWD)
IMAGE_NAME=$(shell basename $(CURRENT_DIR))
TAG:="latest"
USERNAME:=""
PWD:=""
REGISTRY=tsungchh
CMD:=

login:
	docker login

rmc:
	docker ps -a | grep "${REGISTRY}/${IMAGE_NAME}" | awk '{print $$1}' | xargs docker rm

rmi:
	docker images | grep "${REGISTRY}/${IMAGE_NAME}" | awk '{print $$3}' | xargs docker rmi -f

clean: rmc rmi

dcrm:
	docker-compose down && rm -f

push: build
	docker push ${REGISTRY}/${IMAGE_NAME}:${TAG}

build:
	docker build -t ${REGISTRY}/${IMAGE_NAME}:${TAG} .

# run: build
# 	docker run -it ${REGISTRY}/${IMAGE_NAME}:${TAG} ${CMD}

run:
	docker-compose up --build -d