# -*- coding: utf-8 -*-
"""
Scenario of tests
"""

from __future__ import unicode_literals

import sys


if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest



class testOneTestCase(unittest.TestCase):

    # @assertEqualWithComparator
    # def assertExpectedResult(self, result, check, **kwargs):
    #     return None

    def setUp(self):
        pass

    def testOne(self):
        self.assertTrue(True, True)
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()