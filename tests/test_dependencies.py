#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    core
    ~~~~~

    Implements core main

    :author:    BlBana <635373043@qq.com>
    :homepage:  https://github.com/wufeifei/cobra
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2017 Feei. All rights reserved
"""
import os

# for django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Kunlun_M.settings')

import django

django.setup()

import xml.etree.ElementTree as eT
from core.dependencies import Dependencies
from Kunlun_M.settings import PROJECT_DIRECTORY

requirements = PROJECT_DIRECTORY+'/tests/vulnerabilities/requirements.txt'
pom = PROJECT_DIRECTORY+'/tests/vulnerabilities/pom.xml'


def test_find_file():
    dependencies = Dependencies(requirements)
    file_path, flag = dependencies.find_file()
    assert isinstance(file_path, list)
    assert isinstance(flag, int)


def test_get_path():
    dependencies = Dependencies(requirements)
    for root, dirs, filenames in os.walk(dependencies.directory):
        for filename in filenames:
            file_path = dependencies.get_path(root, filename)
            assert isinstance(file_path, list)


def test_find_python_pip():
    dependencies = Dependencies(requirements)
    dependencies.dependencies()
    assert 'Flask' in dependencies.get_result


def test_find_java_mvn():
    dependencies = Dependencies(pom)
    dependencies.dependencies()
    assert 'pom-manipulation-io' in dependencies.get_result


def test_parse_xml():
    dependencies = Dependencies(pom)
    root = dependencies.parse_xml(pom)
    root_test = eT.parse(pom)
    assert isinstance(root, type(root_test))


def test_get_version():
    dependencies = Dependencies(requirements)
    dependencies.dependencies()
    version = dependencies.get_version('Flask')
    assert version == '0.10.1'


def test_get_result():
    dependencies = Dependencies(requirements)
    dependencies.dependencies()
    result = dependencies.get_result
    assert isinstance(result, dict)
