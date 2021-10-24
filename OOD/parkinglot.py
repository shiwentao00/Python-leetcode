"""
We will focus on the following set of requirements while designing the parking lot:

1. The parking lot should have multiple floors where customers can park their cars.

2. The parking lot should have multiple entry and exit points.

3. Customers can collect a parking ticket from the entry points and can pay the parking fee at the exit points on their way out.

4. Customers can pay the tickets at the automated exit panel or to the parking attendant.

5. Customers can pay via both cash and credit cards.

6. Customers should also be able to pay the parking fee at the customer’s info portal on each floor. If the customer has paid at the info portal, they don’t have to pay at the exit.

7. The system should not allow more vehicles than the maximum capacity of the parking lot. If the parking is full, the system should be able to show a message at the entrance panel and on the parking display board on the ground floor.

8. Each parking floor will have many parking spots. The system should support multiple types of parking spots such as Compact, Large, Handicapped, Motorcycle, etc.

9. The Parking lot should have some parking spots specified for electric cars. These spots should have an electric panel through which customers can pay and charge their vehicles.

10. The system should support parking for different types of vehicles like car, truck, van, motorcycle, etc.

Each parking floor should have a display board showing any free parking spot for each spot type.

12. The system should support a per-hour parking fee model. For example, customers have to pay $4 for the first hour, $3.5 for the second and third hours, and $2.5 for all the remaining hours.
"""
from abc import ABC

class Vehicle:
    def __init__(self, make, model, license_plate):
        self.make = make
        self.model = model
        self.license_plate = license_plate

class Person(ABC):
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

class Customer(Person):
    def __init__(self, vehicle):
        self.vehicle = vehicle
    
    def make_payment(self):
        None

class Payment:
    def __init__(self, amount, type, date, time):
        self.amount = amount
        self.type = type
        self.date = date
        self.time = time

class Ticket:
    def __init__(self, start_time, rate, license_plate):
        self.start_time = start_time
        self.rate = rate
        self.license_plate = license_plate

class Attendant(Person):
    def __init__(self, exit):
        self.exit = exit

    def process_ticket(self, ticket):
        None

class ExitPanel:
    def __init__(self, id):
        self.id = id
    
    def process_ticket(self, ticket):
        None

    def process_payment(self, payment):
        None

class Exit:
    def __init__(self, id, exit_panel):
        self.id = id
        self.exit_panel = exit_panel

    def checkout(self, ticket):
        None

class EntryPanel:
    def __init__(self, id):
        self.id = id
    
    def issue_ticket(self):
        None

class GroundFloorEntryPanel(EntryPanel):
    def __init__(self, parking_spots):
        self.parking_spots = parking_spots

    def display_available_spots(self):
        None        

class Entry:
    def __init__(self, id, entry_panel):
        self.id = id
        self.entry_panel = entry_panel

    def issue_ticket(self):
        None

class InfoPortal:
    def __init__(self, id):
        self.id = id

    def process_ticket(self, ticket):
        None

    def process_payment(self, payment):
        None

class Spot(ABC):
    def __init__(self, id):
        self.id = id

class ElectricitySpot(Spot):
    def __init__(self, charger_type):
        self.charger_type = charger_type

class Compact(Spot):
    None

class Large(Spot):
    None

class Handicapped(Spot):
    None

class Motorcycle(Spot):
    None

class DisplayBoard:
    def __init__(self, id, parking_spots):
        self.id = id
        self.parking_spots = parking_spots

    def update_parking_spots_status(self):
        None

    def show_parking_spots_status(self):
        None


class Floor:
    def __init__(self, parking_spots, info_portal, display_board):
        self.parking_spots = parking_spots
        self.info_portal = info_portal
        display_board = display_board

    def fill_spot(self, spot):
        None

    def free_spot(self, spot):
        None

class ParkingLot:
    def __init__(self, floors, entries, exists):
        self.floors = floors
        self.entries = entries
        self.exists = exists

    
