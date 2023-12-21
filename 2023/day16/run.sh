#!/bin/bash
PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 poetry run ptw -c --ignore .venv --ext .txt,.py -- -- -raFP -s -W ignore::pytest.PytestReturnNotNoneWarning -p no:cacheprovider
