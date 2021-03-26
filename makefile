backend-check:
	mypy **/*.py
	bandit **/*.py
	prospector --strictness high **/*.py
	pytest

frontend-check:
	mypy **/*.py
	bandit **/*.py
	prospector --strictness high **/*.py
	pytest
