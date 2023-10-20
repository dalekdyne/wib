IMAGE = read-write-api
VERSION = latest
DOCKERFILE = Dockerfile

requirements:
	@echo "Installing requirements..."
	@pip install -r requirements.txt

dev:
	@echo "Starting the service..."
	@cd src/ && uvicorn main:app --reload

fmt:
	@echo "Formatting code..."
	@black src/

lint:
	@echo "Linting code..."
	@flake8 src/

test:
	@echo "Running tests..."
	@python -m pytest

build:
	@echo "Building docker image..."
	@docker build -t $(IMAGE):$(VERSION) -f $(DOCKERFILE) .

.PHONY: requirements fmt lint test
