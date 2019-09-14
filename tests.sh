#!/usr/bin/env bash
set -e -u

pip install -r requirements.txt
pip install pytest coverage
coverage run -m pytest
coverage report
rm -rf ./*
