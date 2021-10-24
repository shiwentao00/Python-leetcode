from abc import ABC

class CardReader:
    def read_card(self, card):
        None

class Card:
    def __init__(self, card_id, customer_name, exp_data, pin):
        self.card_id = card_id
        self.customer_name = customer_name
        self.exp_data = exp_data
        self.pin = pin

class Keyboard:
    def take_input(self):
        None

class Screen:
    def get_input(self):
        None

    def show_info(self):
        None

class CashDispenser:
    def get_amount(self):
        None
    
    def dispense(self):
        None

class DepositSlot:
    def take_money(self):
        None

class SystemInfra:
    def authenticate_user(self):
        None
    
    def make_transaction(self):
        None

class Person(ABC):
    def __init__(self, first, last, email, phone):
        self.first = first
        self.last = last
        self.email = email
        self.phone = phone

class Customer(Person):
    def __init__(self, first, last, email, phone, cards):
        super().__init__(first, last, email, phone)
        self.cards = cards

    def make_transaction(self, atm, card, transaction):
        None

class Account(ABC):
    def __init__(self, acc_number, owner, balance):
        self.acc_number = acc_number
        self.owner = owner
        self.balance = balance

class SavingAccount(Account):
    def __init__(self, withdraw_limit):
        self.withdraw_limit = withdraw_limit

class ChceckingAccount(Account):
    def __init__(self, debitcard_number):
        self.debitcard_number = debitcard_number

from enum import Enum 
class TransactionType(Enum):
    BALANCE_INQUIRY, DEPOSIT_CASH, DEPOSIT_CHECK, WITHDRAW, TRANSFER = 1, 2, 3, 4, 5

class Transaction(ABC):
    def __init__(self, transaction_id, time, type):
        self.transaction_id = transaction_id
        self.time = time
        self.type = type

class BalanceInquiry(Transaction):
    def __init__(self, account):
        self.account = account
    
    def make_transaction(self):
        None

class DepositCash(Transaction):
    def __init__(self, amount, account):
        self.amount = amount
        self.account = account

    def make_transaction(self):
        None

class Check:
    def __init__(self, amount, account):
        self.amount = amount
        self.account = account

class DepositCheck(Transaction):
    def __init__(self, check, account):
        self.check = check
        self.account = account

    def make_transaction(self):
        None

class WithDraw(Transaction):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def make_transaction(self):
        None

class Transfer(Transaction):
    def __init__(self, amount, source, destination):
        self.amount = amount
        self.source = source
        self.destination = destination
    
    def make_transaction(self):
        None


class ATM:
    def __init__(self, id, location):
        self.id = id 
        self.location = location

        self.card_reader = CardReader()
        self.keyboard = Keyboard()
        self.screen = Screen()
        self.cash_dispenser = CashDispenser()
        self.deposit_slot = DepositSlot()
        self.system = SystemInfra()

    def authenticate_user(self, card):
        None

    def make_transaction(self, customer, transaction):
        None