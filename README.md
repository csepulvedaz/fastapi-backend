# FastAPI + Prisma + PostgreSQL

This repository contains a RESTful API project based on FastAPI and Prisma.

## Installation

To install the dependencies for this project, follow the steps below:

1. Make sure you have Poetry installed. If not, please install Poetry.

   `curl -sSL https://install.python-poetry.org | python3 -`

2. Install the project dependencies by running:

   `make deps`

   This command will install the required dependencies and set up pre-commit hooks.

## Generating Prisma Schema

To generate the Prisma schema, execute the following command:

- `make prisma-generate`

  This command will generate the necessary Prisma client code based on the schema defined in the project.

## Pushing the Prisma Schema

To push the Prisma schema to the database, run the following command:

- `make prisma-push`

  This command will apply any pending changes in the schema to the database.

## Running the Project

To run the project on a local web server, execute the following command:

- `make run`

  **This command will start the project using Uvicorn and enable auto-reloading for development purposes.**

Check API is up and running by opening it's root URL [http://localhost:8000](http://localhost:8000) in your web browser.

Check [OpenAPI](https://swagger.io/specification/) docs is up and running by opening it's URL [http://localhost:8000/docs](http://localhost:8000/docs) in your web browser.

## Makefile Commands

The following are additional commands available in the Makefile:

- `make format`: Formats the code using isort and black.
- `make lint`: Performs linting using ruff with the configuration specified in ruff.toml.
- `make isort`: Checks the code formatting using isort.
- `make black`: Checks the code formatting using black.
- `make clean`: Removes generated files and directories.
- `make code-checks`: Runs isort, black, and lint commands to perform code checks.

Please refer to the Makefile for more details on each command and its usage.
