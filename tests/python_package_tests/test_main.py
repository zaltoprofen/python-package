# -*- coding: utf-8 -*-
import python_package.main


def test_hello_method_returns_hello_world():
    assert python_package.main.greet() == 'Hello World!'
