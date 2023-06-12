#!/usr/bin/env bash

PIP_REPO='zzrc-pip'

rm -f dist/*
python3 setup.py sdist && twine register -r ${PIP_REPO} dist/* && twine upload -r ${PIP_REPO} dist/*