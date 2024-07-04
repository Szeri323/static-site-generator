import unittest
from copy_from_static_to_public import (
    list_directory
    )

class TestCopyFromStaticToPublic(unittest.TestCase):
    def test_copy_from_static_to_public(self):
        list_directory()