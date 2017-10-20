# -*- coding: utf-8 -*-
"""
Internal helper functions for unit tests of parsedatetime
"""
from __future__ import unicode_literals

def assertEqualWithComparator(comparator):
    """
    Fail a little less cryptically that unittest.assertTrue when comparing a
    result against a target value. Shows the result and the target in the
    failure message.
    """

    def decoratedComparator(self, result, check, errMsg=None, **kwargs):
        errMsg = errMsg or 'Result does not match target value'
        equal = comparator(self, result, check, **kwargs)
        failureMessage = ('%s\n\n\t'
                          'Result:\n\t%s\n\n\tExpected:\n\t%s')

        if not equal:
            self.fail(failureMessage % (errMsg, result, check))

    return decoratedComparator