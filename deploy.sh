#!/bin/bash

. /usr/lib/ckan/default/bin/activate
rm -rf /usr/lib/ckan/default/src/ckanext-romania_theme/
cp -R ckan/lib/default/src/ckanext-romania_theme/ /usr/lib/ckan/default/src/
python /usr/lib/ckan/default/src/ckanext-romania_theme/setup.py develop
