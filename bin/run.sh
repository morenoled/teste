#!/bin/bash

CURDIR="$(pwd)"
APPDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd "${APPDIR}/.."
export FLASK_ENV=development
export FLASK_APP=main.py
flask run
cd "${CURDIR}"