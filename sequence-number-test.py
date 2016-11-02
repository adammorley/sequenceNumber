#!/usr/bin/python

import unittest

import SequenceNumber

class TestSequenceNumber(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1(self):
        sn = SequenceNumber.NumberGenerator()
        self.assertEqual(sn.get(), 1)
        self.assertEqual(sn.get(), 2)
        self.assertEqual(sn.get(), 3)

if __name__ == '__main__':
    unittest.main()
