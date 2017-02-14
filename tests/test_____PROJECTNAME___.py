#!/usr/bin/env python
# encoding: utf-8

"""
" ___FILENAME___
" ___PROJECTNAME___
"
" Created by ___FULLUSERNAME___ on ___DATE___.
" Copyright ___YEAR___ ___ORGANIZATIONNAME___. All rights reserved.
"""

import unittest


class TestMain(unittest.TestCase):
    
    def test_setup(self):
        """
            The objective is not to test the obvious, but
            but to check if layout is correct and the setup
            finds the tests!
            The shell sould say it found 1 test!
        """
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()