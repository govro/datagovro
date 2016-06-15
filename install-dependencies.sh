#!/usr/bin/env bash

apt-add-repository ppa:ansible/ansible -y
apt-get update -qq
apt-get install git ansible software-properties-common -qq
