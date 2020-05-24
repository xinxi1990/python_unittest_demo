#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
unittest组织结构实例
"""

import unittest
import pprint

class SuitTestCase(unittest.TestCase):

    @classmethod

    def setUpClass(cls):
        pprint.pprint('setUpClass')


    def setUp(self):
        pprint.pprint('setUp')


    def test_method(self):
        pprint.pprint('test_method')


    def tearDown(self):
        pprint.pprint('tearDown')

    @classmethod
    def tearDownClass(cls):
        pprint.pprint('tearDownClass')



