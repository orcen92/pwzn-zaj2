# -*- coding: utf-8 -*-

import unittest
import types


class TestClass(unittest.TestCase):

    TESTED_MODULE = None

    def setUp(self):
        super().setUp()
        self.xrange = self.TESTED_MODULE.xrange

    def test1(self):
        self.assertEqual(list(self.xrange(10)), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test2(self):
        self.assertEqual(list(self.xrange(5, 10)), [5, 6, 7, 8, 9])

    def test3(self):
        self.assertEqual(list(self.xrange(5, 20, 2)), [5, 7, 9, 11, 13, 15, 17, 19])

    def test_type(self):
        self.assertEqual(type(self.xrange(1)), types.GeneratorType)
