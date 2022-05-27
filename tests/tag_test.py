import unittest
from models.tag import Tag


class TestTag(unittest.TestCase):
    def setUp(self):
        self.tag1 = Tag("Entertainment")

    def test_tag_has_name(self):
        self.assertEqual("Entertainment", self.tag1.name)
