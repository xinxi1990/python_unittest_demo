#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
unittest组织结构实例
"""

import unittest


class Widget():

    def __init__(self,name):
        self.name = name
        self.wight = 30
        self.height = 10


    def resize(self,wight,height):
        self.wight = wight
        self.height = height


    def size(self):
        return (self.wight,self.height)


    def dispose(self):
        return 0



class DefaultWidgetSizeTestCase(unittest.TestCase):

    def test_default_widget_size(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50))


class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget('The widget')


    def test_default_widget_size(self):
        print(self.widget.size())
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        print(self.widget.size())
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')

    def tearDown(self):
        self.widget.dispose()


def makeSomethingDB():
    print('makeSomethingDB')

def deleteSomethingDB():
    print('deleteSomethingDB')


def testSomething():
    print('testSomething')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite


# 复用已有的测试代码



if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(suite())

    testcase = unittest.FunctionTestCase(testSomething,
                                         setUp=makeSomethingDB,
                                         tearDown=deleteSomethingDB)

    testcase.run()