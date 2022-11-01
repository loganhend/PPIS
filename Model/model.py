from enum import Enum


class Model:
    def __init__(self):
        self.Park = Park()
        self.bank = bankAbstraction()
        self.userList = UserStorage()



class User:
    def __init__(self, id, type, password, login, phone):
        self.id = id
        self.userType = type
        self.password = password
        self.login = login
        self.mobPhone = phone


class Employee(User):
    def __init__(self, id, type, password, login, phone, status):
        super().__init__(id, type, password, login, phone)
        self.position = status


class Visitor(User):
    def __init__(self, id, type, password, login, phone):
        super().__init__(id, type, password, login, phone)
        self.ticketStorage = TicketStorage()


class UserStorage:
    def __init__(self):
        self.EmployeeStorage = []
        self.VisitorStorage = []
        # заполнение EmployeeStorage экземплярами класса Employee
        # заполнение VisitorStorage экземплярами класса Visitor



class TicketType(Enum):
    Child = 1
    Student = 2
    Adult = 3


class TicketStatus(Enum):
    Active = 1
    Inactive = 2
    OverDue = 3


class Ticket:
    def __init__(self, type, status):
        self.id = 0
        self.date = ""
        self.type = TicketType(type)
        self.status = TicketStatus.Active


class TicketStorage:
    def __init__(self):
        self.TicketList = {}
        # заполнение TicketList экземплярами класса Ticket


class Review:
    def __init__(self, text, user, status):
        self.text = text
        self.user = user
        self.satus = status
        self.deletionReason = ""


class Location:
    def __init__(self, id, name, photo, description):
        self.id = id
        self.name = name
        self.photo = photo
        self.description = description
        self.reviews = []


class FoodPlace(Location):
    def __init__(self, id, name, photo, description, type):
        super().__init__(id, name, photo, description)
        self.type = type


class Attraction(Location):
    def __init__(self, id, name, photo, description, type, difficulty, inventory, restrictions, waterTemp):
        super().__init__(id, name, photo, description)
        self.type = type
        self.difficulty = difficulty
        self.inventory = inventory
        self.restrictions = restrictions
        self.waterTemperature = waterTemp


class AttractionStorage:
    def __init__(self):
        self.AttractionList = []
        # заполнение AttractionList экземплярами класса Attraction


class FoodPlaceStorage:
    def __init__(self):
        self.FoodPlaceList = []
        # заполнение FoodPlaceList экземплярами класса FoodPlace


class Park:
    def __init__(self):
        self.attractionList = AttractionStorage()
        self.foodPlaceList = FoodPlaceStorage()
        self.description = "something"
        self.address = "something"
        self.webSite = "something"
        self.phoneNum = "something"
        self.workingHours = "something"


class bankAbstraction:
    def makeTransaction(self, cardNum):
        if cardNum != "":
            return True
        else:
            return False
