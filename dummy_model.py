
class DummyModel(object):

    def __init__(self):
        self.dummydb = {
            12345: {'Checking': 500, 'Savings': 1000},
            98765: {'Checking': 100, 'Savings': 200}
        }

    def is_valid_card_no(self, card_no):
        return True

    def is_valid_pin(self, card_no, pin):
        return True

    def get_accounts(self, card_no):
        return ['Checking', 'Savings']

    def get_balance(self, card_no, account_type):
        return self.dummydb[card_no][account_type]

    def deposit(self, card_no, account_type, deposit_amount):
        self.dummydb[card_no][account_type] += deposit_amount
        return True

    def withdrawal(self, card_no, account_type, withdrawal_amount):
        self.dummydb[card_no][account_type] -= withdrawal_amount
        return True

    def transfer(self, card_no, sending_account_type, receiving_card_no,
        receiving_account_type, transfer_amount):
        self.withdrawal(card_no, sending_account_type, transfer_amount)
        self.deposit(receiving_card_no, receiving_account_type, transfer_amount)
        return True

