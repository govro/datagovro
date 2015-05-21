#!/bin/bash

. /usr/lib/ckan/default/bin/activate
rm -rf /usr/lib/ckan/default/src/ckanext-romania_theme/
cp -R ckan/lib/src/ckanext-romania_theme/ /usr/lib/ckan/default/src/
python setup.py develop /usr/lib/ckan/default/src/ckanext-romania_theme/setup.py
