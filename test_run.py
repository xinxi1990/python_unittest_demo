#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import unittest

from test_unit_one import TestOne
from test_unit_two import TestTwo


# if __name__ == '__main__':
#     # suite = unittest.TestSuite()
#     # suite.addTest(TestOne("test_method_one"))
#     # suite.addTest(TestTwo("test_method_two"))
#     # unittest.TextTestRunner().run(suite)
#
#     unittest.main()
#

# cash_path = os.path.join(os.getcwd())
#
# print('文件地址：', os.getcwd())
# print("cash_path:", cash_path)
#
# discover = unittest.defaultTestLoader.discover(cash_path,
#                                                pattern="test_unit*.py",
#                                                top_level_dir=None)
# # top_level_dir : 这个是顶层目录的名称，一般默认等于None就行了
#
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     runner.run(discover)


if __name__ == '__main__':

    suite1 = unittest.makeSuite(TestOne)
    suite2 = unittest.makeSuite(TestTwo)

    unittest.TextTestRunner().run(suite1)
    unittest.TextTestRunner().run(suite2)
