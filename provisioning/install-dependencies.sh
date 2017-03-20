#!/usr/bin/env bash

apt-get update -qq
apt-get install git software-properties-common python-dev python-pip build-essential libssl-dev libffi-dev -qq

apt-get install postgresql-9.3 -qq
pg_createcluster 9.3 main --start

pip install markupsafe
pip install ansible==2.0.2.0
pip install setuptools==11.3
