import unittest
from models.merchant import Merchant


class TestMerchant(unittest.TestCase):
    def setUp(self):
        self.merchant1 = Merchant("Tesco")

    def test_tag_has_name(self):
        self.assertEqual("Tesco", self.merchant1.name)
