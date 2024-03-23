PROJECT_NAME = orthanc-mock
DOCKER_REGISTRY = cr.gingosrl.it
DOCKER_IMAGE_NAME = $(DOCKER_REGISTRY)/open-ortho/$(PROJECT_NAME)
VERSION = 0.1.0

.PHONY: build
build:
	docker build -t $(DOCKER_IMAGE_NAME):$(VERSION) -t $(DOCKER_IMAGE_NAME):latest ./orthanc_mock/

.PHONY: deploy
deploy: build
	docker login $(DOCKER_REGISTRY)
	docker push $(DOCKER_IMAGE_NAME):$(VERSION)
	docker push $(DOCKER_IMAGE_NAME):latest