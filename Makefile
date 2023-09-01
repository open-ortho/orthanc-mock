.PHONY: build
build:
	docker compose build
	docker compose up -d
	sleep 1
	./import_sample_data.py
