from exceptions import NotValidCardError, NotValidPINError, InsufficientBalanceError


class ATMController(object):

    def __init__(self, model, view = None):
        self.model = model
        self.view = view
        self.card_no = None
        self.pin_correct = False
    

    def confirm_valid_card(self, card_no):
        if self.model.is_valid_card_no(card_no):
            self.card_no = card_no
            return True
        
        else:
            raise NotValidCardError

    def check_pin(self, pin):
        if self.model.is_valid_pin(self.card_no, pin):
            self.pin_correct = True
            return True
        
        else:
            raise NotValidPINError
    
    def retrieve_accounts(self):
        accounts = self.model.get_accounts(self.card_no)
        return accounts

    def retrieve_balance(self, account_type):
        current_balance = self.model.get_balance(self.card_no, account_type)
        return current_balance

    def make_deposit(self, account_type, deposit_amount):
        return self.model.deposit(self.card_no, account_type, deposit_amount)

    def make_withdrawal(self, account_type, withdrawal_amount):
        current_balance = self.retrieve_balance(account_type)
        if current_balance > withdrawal_amount:
            return self.model.withdrawal(self.card_no, account_type, withdrawal_amount)
        else:
            raise InsufficientBalanceError

    def make_transfer(self, sending_account_type, receiving_card_no, receiving_account_type, transfer_amount):
        sending_account_balance = self.retrieve_balance(sending_account_type)
        if sending_account_balance > transfer_amount:
            return self.model.transfer(self.card_no, sending_account_type, receiving_card_no,
            receiving_account_type, transfer_amount)
        else:
            raise InsufficientBalanceError

    def go(self):
        # card_no
        while self.card_no == None:
            card_no = self.view.read_card_no()
            self.confirm_valid_card(card_no)

        while not self.pin_correct:
            pin = self.view.get_pin()
            self.check_pin(pin)

        self.view.display_accounts(self.retrieve_accounts)
        account_type = self.view.choose_account()


        while True:
            self.view.display_action_options()
            action = self.view.choose_action()

            if action == 'Check Balance':
                return self.retrievebalance(account_type)
            
            elif action == 'Deposit':
                deposit_amount = self.view.input_deposit_amount()
                return self.make_deposit(account_type, deposit_amount)
            
            elif action == 'Withdraw':
                withdrawal_amount = self.view.input_withdrawal_amount()
                return self.make_withdrawal(account_type, withdrawal_amount)
            
            elif action == 'Transfer':
                sending_account = account_type
                receiving_card_no = self.view.input_recipient_card_no()
                receiving_account_type = self.view.input_recipient_account_type()
                transfer_amount = self.view.input_transfer_amount()
                return self.make_transfer(sending_account, receiving_account, transfer_amount)
            
            elif action == 'Exit':
                break