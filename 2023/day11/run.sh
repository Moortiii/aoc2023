#!/bin/bash
PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 poetry run ptw -c --ignore .venv --ext .txt,.py -- -- -s -raFP -W ignore::pytest.PytestReturnNotNoneWarning -p no:cacheprovider
