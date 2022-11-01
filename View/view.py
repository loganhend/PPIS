from View.pyui.about_park import Ui_aboutParkWindow
from View.pyui.buying_tickets import Ui_BuyingTicketsScreen
from View.pyui.create_account import Ui_CreateAccWindow
from View.pyui.deletion_dialogue import Ui_Dialog
from View.pyui.enter_account import Ui_EnterWindow
from View.pyui.location_screen import Ui_LocationScreen
from View.pyui.locations_screen import Ui_LocationsScreen
from View.pyui.main_screen import Ui_MainWindow
from View.pyui.menu_screen import Ui_mainMenu
from View.pyui.personal_screen import Ui_PersonalWindow
from View.pyui.tickets_history import Ui_userTicketsStoryScreen
from View.pyui.user_search import Ui_userSearchWindow
from View.pyui.user_tickets import Ui_UserTicketsScreen
from View.pyui.review_dialogue import Ui_Dialog1
from View.pyui.ticket_status_dialogue import Ui_Dialog2

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class View:
    def __init__(self, c, m):
        self.model = m
        self.controller = c

        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()

        self.ParkScreen = Ui_aboutParkWindow(self.controller,self.model)
        self.BuyingTicketsScreen = Ui_BuyingTicketsScreen(self.controller,self.model)
        self.CreateAccScreen = Ui_CreateAccWindow(self.controller,self.model)
        self.EnterAccScreen = Ui_EnterWindow(self.controller,self.model)
        self.LocationScreen = Ui_LocationScreen(self.controller,self.model)
        self.LocationsScreen = Ui_LocationsScreen(self.controller,self.model)
        self.MainScreen = Ui_MainWindow(self.controller,self.model)
        self.MenuScreen = Ui_mainMenu(self.controller,self.model)
        self.PersonalScreen = Ui_PersonalWindow(self.controller,self.model)
        self.TicketsHistoryScreen = Ui_userTicketsStoryScreen(self.controller,self.model)
        self.UserSearchScreen = Ui_userSearchWindow(self.controller,self.model)
        self.UserTicketsScreen = Ui_UserTicketsScreen(self.controller,self.model)

        self.deletion_dialogue = Ui_Dialog(self.controller,self.model)
        self.review_dialogue = Ui_Dialog1(self.controller,self.model)
        self.ticket_dialogue = Ui_Dialog2(self.controller,self.model)

    def show_AttractionsScreen(self):
        self.MenuScreen.hide()
        self.LocationsScreen.show()

    def show_FoodPlacesScreen(self):
        self.MenuScreen.hide()
        self.LocationsScreen.show()

    def show_start(self):
        self.MainScreen.show()
        sys.exit(self.app.exec_())

    def show_MainScreen(self):
        self.CreateAccScreen.hide()
        self.EnterAccScreen.hide()
        self.MainScreen.show()

    def show_MenuScreen(self):
        self.CreateAccScreen.hide()
        self.EnterAccScreen.hide()
        self.ParkScreen.hide()
        self.LocationsScreen.hide()
        self.LocationScreen.hide()
        self.PersonalScreen.hide()
        self.UserSearchScreen.hide()
        self.MenuScreen.show()

    def show_PersonalScreen(self):
        self.MenuScreen.hide()
        self.UserTicketsScreen.hide()
        self.PersonalScreen.show()

    def show_TicketsHistoryScreen(self, login):
        self.TicketsHistoryScreen.setUser(login)
        self.UserSearchScreen.hide()
        self.TicketsHistoryScreen.show()

    def show_UserSearchScreen(self):
        self.MenuScreen.hide()
        self.TicketsHistoryScreen.hide()
        self.UserSearchScreen.show()

    def show_UserTicketsScreen(self):
        self.PersonalScreen.hide()
        self.BuyingTicketsScreen.hide()
        self.UserTicketsScreen.show()

    def show_ParkScreen(self):
        self.MenuScreen.hide()
        self.ParkScreen.show()

    def show_BuyingTicketsScreen(self):
        self.UserTicketsScreen.hide()
        self.BuyingTicketsScreen.show()

    def show_CreateAccScreen(self):
        self.MainScreen.hide()
        self.CreateAccScreen.show()

    def show_EnterAccScreen(self):
        self.MainScreen.hide()
        self.EnterAccScreen.show()

    def show_LocationScreen(self, loc):
        self.LocationsScreen.hide()
        self.LocationScreen.setLoc(loc)
        self.LocationScreen.show()

    def show_DeletionDialogue(self):
        self.deletion_dialogue.show()

    def show_ReviewDialogue(self):
        self.review_dialogue.show()

    def show_TicketStatusDialogue(self):
        self.ticket_dialogue.show()