install:
	pip install -r requirements.txt

run:
	python main_pipeline.py

docker-up:
	docker compose up --build

docker-down:
	docker compose down

train:
	python pipelines/train.py

evaluate:
	python pipelines/evaluate.py

.PHONY: install run docker-up docker-down train evaluate
