import pytest
import unittest
import mock

from atm_controller import ATMController
from dummy_model import DummyModel

class TestController(unittest.TestCase):

    def setUp(self):
        self.dummy_model = DummyModel()
        self.controller = ATMController(self.dummy_model)
        self.controller.card_no = 12345

    def test_valid_card(self):
        self.controller.confirm_valid_card(12345)
        self.assertEqual(self.controller.card_no, 12345)

    def test_valid_pin(self):
        self.controller.check_pin(0000)
        self.assertTrue(self.controller.pin_correct)

    def test_retrieve_accounts(self):
        accounts_received = self.controller.retrieve_accounts()
        self.assertEqual(accounts_received, ['Checking', 'Savings'])

    def test_retrieve_checkings_balance(self):
        balance_received = self.controller.retrieve_balance('Checking')
        self.assertEqual(balance_received, 500)

    def test_retrieve_savings_balance(self):
        balance_received = self.controller.retrieve_balance('Savings')
        self.assertEqual(balance_received, 1000)

    def test_make_deposit(self):
        self.assertEqual(self.controller.card_no, 12345)
        balance_before_deposit = self.controller.retrieve_balance('Checking')
        self.assertEqual(balance_before_deposit, 500)
        self.controller.make_deposit('Checking', 100)
        balance_after_deposit = self.controller.retrieve_balance('Checking')
        self.assertEqual(balance_after_deposit, 600)

    def test_make_withdrawal(self):
        self.assertEqual(self.controller.card_no, 12345)
        balance_before_withdrawal = self.controller.retrieve_balance('Checking')
        self.assertEqual(balance_before_withdrawal, 500)
        self.controller.make_withdrawal('Checking', 200)
        balance_after_withdrawal = self.controller.retrieve_balance('Checking')
        self.assertEqual(balance_after_withdrawal, 300)

    def test_make_transfer(self):
        sending_account_balance_before_transfer = self.controller.retrieve_balance('Checking')
        self.controller.make_transfer('Checking', 98765, 'Savings', 100)
        self.controller.card_no = 98765
        recipient_account_balance_after_transfer = self.controller.retrieve_balance('Savings')
        self.assertEqual(recipient_account_balance_after_transfer, 300)
