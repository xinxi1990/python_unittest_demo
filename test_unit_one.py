

# import pytest
#
#
# def test_method_one():
#     print('test_method_one')



import unittest




class TestOne(unittest.TestCase):


    name = 1

    def test_method_one(self):
        print('test_method_one')
        self.assertEqual(1,2)


    def test_method_two(self):
        print('test_method_two')


    def test_method_three(self):
        print('test_method_three')


if __name__ == '__main__':
 unittest.main()