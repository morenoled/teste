#!/bin/bash

CURDIR="$(pwd)"
APPDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd "${APPDIR}/.."
pip install -r requirements.txt
cd "${CURDIR}"
