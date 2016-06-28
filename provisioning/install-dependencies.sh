#!/usr/bin/env bash

apt-get update -qq
apt-get install git software-properties-common python-pip -qq

pip install ansible==2.0.2.0
