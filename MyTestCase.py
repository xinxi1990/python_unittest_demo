#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
unittest跳过用例

# 跳过测试与预计的失败

## 直接跳过
```
@unittest.skip
```

## 正确就强制跳过
```
@unittest.skipIf(a > b, u"a>b，正确就强制跳过")
```

## 错误就跳过
```
@unittest.skipUnless(a%b == 2, u"错误就跳过")
```

## 方法内跳过
```
self.skipTest("external resource not available")
```

"""

import sys
import unittest



class MyLib():

    __version__ = 7


def external_resource_available():
    return True

class MyTestCase(unittest.TestCase):


    mylib = MyLib()


    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass


    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass