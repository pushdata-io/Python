#!/bin/bash

case $1 in
build)
  rm dist/*
  python3 setup.py sdist bdist_wheel
  ;;
upload-test)
  python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
  ;;
pip-install-test)
  pip install --upgrade --index-url https://test.pypi.org/simple/ pushdata-io
  ;;
*)
  echo "Usage: $0 [build] | [upload-test] [pip-install-test]"
esac
