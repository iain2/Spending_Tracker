import unittest
from models.tag import Tag
from models.merchant import Merchant
from models.transaction import Transaction


class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.tag1 = Tag("Entertainment")
        self.merchant1 = Merchant("Tesco")
        self.transaction1 = Transaction(4, self.tag1, self.merchant1)

    def test_transaction_has_amount(self):
        self.assertEqual(4, self.transaction1.amount)

    def test_transaction_has_tag(self):
        self.assertEqual(self.tag1, self.transaction1.tag)

    def test_transaction_has_mechant(self):
        self.assertEqual(self.merchant1, self.transaction1.merchant)
