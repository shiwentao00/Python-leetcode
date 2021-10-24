from abc import ABC
from enum import Enum

class Address:
    def __init__(self, street, city, country, zip):
        self.street = street
        self.city = city
        self.country = country
        self.zip = zip

class BookStatus(Enum):
    AVAILABLE, LENDED, RESERVED, LOST = 1, 2, 3, 4




# ------------
#   Actors
# ------------

class System:
    def __init__(self):
        pass

    def send_notification(self):
        pass

class Person(ABC):
    def __init__(self,first, last):
        self.first = first
        self.last = last

# ------------------------
#   Book related classes
# ------------------------
class Book(ABC):
    def __init__(self, author, title, category, id):
        self.author = author
        self.title = title
        self.category = category
        self.id = id

class BookItem(Book):
    def __init__(self, barcode, status, rack):
        self.barcode = barcode
        self.status = status
        self.rack = rack

class Rack:
    def __init__(self, floor, id):
        self.floor = floor
        self.id = id

class Author(Person):
    def __init__(self, published_books):
        self.published_books = []

class Library:
    def __init__(self, street, city, country, zip):
        self.address = Address(street, city, country, zip)
        self.books = []
        self.customers = []
        self.libarians =[]
        self.system = System()
