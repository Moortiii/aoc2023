#!/bin/bash
PYTHONDONTWRITEBYTECODE=1 poetry run ptw -c --ignore .venv --ext .txt,.py -- -- -raFP -W ignore::pytest.PytestReturnNotNoneWarning -p no:cacheprovider
