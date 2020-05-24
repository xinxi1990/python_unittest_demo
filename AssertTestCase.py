#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
unittest的断言
"""

import unittest
import pprint
import copy

class AssertTestCase(unittest.TestCase):


    def __init__(self, methodName='runTest', param=None):
        super(AssertTestCase, self).__init__(methodName)
        self.param = param
        # 重写父类方法
        self.addTypeEqualityFunc(str, 'assertDebug')


    def get_func(self):
        return True


    def assertDebug(self):
        self.assertAlmostEqual(1,1)


    def test_method(self):

        self.assertAlmostEqual(1, 1)
        # 等于

        self.assertNotAlmostEqual(1, 2)
        # 不等于

        self.assertGreater(2, 1)
        # 大于

        self.assertGreaterEqual(2, 1)
        # 大于等于

        self.assertLess(1, 2)
        # 小于

        self.assertLessEqual(1, 2)
        # 小于等于


        self.assertRegex('abc', 'a')
        # re.search
        # 匹配

        self.assertNotRegex('abc', 'd')
        # re.search
        # 不匹配

        self.assertCountEqual([0, 1, 1], [1, 0, 1])
        # 数量


        # function = self.get_func
        #
        # new_function = copy.copy(function)

        self.assertDebug()
