APPLICATION_NAME = disagreement
CODE = $(APPLICATION_NAME)

run:  ##@Application Run application server
	poetry run python3 -m $(APPLICATION_NAME)

lint:  ##@Code Check code with pylint
	poetry run python3 -m pylint $(CODE)

format:  ##@Code Reformat code with isort and black
	poetry run python3 -m isort $(CODE)
	poetry run python3 -m black $(CODE)

