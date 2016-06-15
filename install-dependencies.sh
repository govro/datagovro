#!/usr/bin/env bash

apt-add-repository ppa:ansible/ansible -y
apt-get update -qq
apt-get install git ansible=2.0.2.0-1ppa~trusty software-properties-common -qq
