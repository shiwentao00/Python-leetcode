"""
Our ticket booking service should meet the following requirements:

1. It should be able to list the cities where affiliate cinemas are located.
2. Each cinema can have multiple halls and each hall can run one movie show at a time.
3. Each Movie will have multiple shows.
4. Customers should be able to search movies by their title, language, genre, release date, and city name.
5. Once the customer selects a movie, the service should display the cinemas running that movie and its available shows.
6. The customer should be able to select a show at a particular cinema and book their tickets.
The service should show the customer the seating arrangement of the cinema hall. The customer should be able to select multiple seats according to their preference.
The customer should be able to distinguish between available seats and booked ones.
The system should send notifications whenever there is a new movie, as well as when a booking is made or canceled.
Customers of our system should be able to pay with credit cards or cash.
The system should ensure that no two customers can reserve the same seat.
Customers should be able to add a discount coupon to their payment.
"""
from abc import ABC

class City:
    def __init__(self, name, state):
        self.name = name
        self.state = state

class Hall:
    def __init__(self, number):
        self.number = number

class Address(ABC):
    def __init__(self, street_num, street, city, state, zip):
        self.street_num = street_num
        self.street = street
        self.city = city
        self.zip = zip

class Cinema:
    def __init__(self, address, halls):
        self.address = address
        self.halls = halls

class Movie:
    def __init__(self, title, rating, release_date, language, genre, shows):
        self.title = title
        self.rating = rating
        self.release_date = release_date
        self.language = language
        self.genre = genre

        self.shows = shows

    def get_cinemas(self):
        """Display available cinemas where the movie is on"""
        None

    def get_shows(self):
        None

class Show:
    def __init__(self, price, time, cinema, hall):
        self.price = price
        self.time = time
        self.cinema = cinema
        self.hall = hall

    def display_seats(self):
        None

class Catelog:
    def __init__(self, movies):
        self.movies = movies

    def search_by_tile(self):
        None

    def search_by_language(self):
        None

    def search_by_genre(self):
        None
    
    def search_by_release_date(self):
        None

    def search_by_city(self):
        None


class Person(ABC):
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

class Customer(Person):
    def __init__(self):
        self.bookings = []

    def make_booking(self):
        None

    def get_bookings(self):
        None

class Boooking:
    def __init__(self, show, num_tickets, seats, customer):
        self.show = show
        self.num_tickets = num_tickets
        self.seats = seats
        self.customer = customer

    def pay(self):
        None

    def cancel(self):
        None


class MovieTicketService:
    def __init__(self, cities, catelog):
        self.cities = cities
        self.catelog = catelog

    def list_cities(self):
        None

    def add_movie(self):
        None

    def remove_movie(self):
        None

    