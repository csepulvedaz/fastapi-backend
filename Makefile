#
# Makefile
#

APP_DIR=api
TEST_DIR=tests

deps:
	@poetry --version &> /dev/null || (echo -e "ERROR: please install poetry" && false)
	poetry config virtualenvs.in-project true
	poetry env list
	poetry env info
	poetry install
	poetry run pre-commit install
	touch $@

format:
	poetry run isort --settings-path=.isort.cfg $(APP_DIR)/**.py $(TEST_DIR)/**.py
	poetry run black --config=pyproject.toml $(APP_DIR) $(TEST_DIR)

lint:
	poetry run ruff --version
	poetry run ruff --config ruff.toml ${APP_DIR} ${TEST_DIR}

isort:
	poetry run isort --check-only $(APP_DIR)/**.py $(TEST_DIR)/**.py

black:
	poetry run black --check $(APP_DIR) $(TEST_DIR)

run: ## run project in localhost web server
	poetry run uvicorn api.main:app --reload

generate:
	poetry run prisma generate

update-version:
	poetry run python api/utils/update_version.py

clean:
	rm -rf .venv deps .ruff_cache api/__pycache__ api/routes/__pycache__ poetry.lock

code-checks: isort black lint
