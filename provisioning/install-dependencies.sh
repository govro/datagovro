#!/usr/bin/env bash

apt-get update -qq
apt-get install git software-properties-common python-dev python-pip build-essential libssl-dev libffi-dev -qq

pip install markupsafe
pip install ansible==2.0.2.0
