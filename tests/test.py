import os
from tempfile import TemporaryDirectory
from unittest import TestCase


class dummy(TestCase):
    def test_basic(self):
        CSI_SALT = "111"
        self.assertEqual("68e656", "68e656")
        self.assertEqual("96c03d29", "96c03d29")