#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_boiler_plate
----------------------------------

Tests for `boiler_plate` module.
"""

import unittest

import boiler_plate

from boiler_plate import cli


class TestBoiler_plate(unittest.TestCase):

    def setUp(self):
        print(self)
        pass

    def test_something(self):
        print("test 2")
        assert(boiler_plate.__version__)

    def tearDown(self):
        print("test 3")
        pass

#shudson added for testing testing
    def test_muststartwithprefixtest(self):
        print ("test 4")
        print("boiler_plate.__version__")
        assert(boiler_plate.get_versions()=="0.1.1")

    def test_somethingNEW(self):
        print("test 5")
        boiler_plate.cli()
        assert(boiler_plate.__version__)

#shudson - added so can simply run at command line
#Need to put boiler_plate in python path though
if __name__ == '__main__':
    unittest.main()
