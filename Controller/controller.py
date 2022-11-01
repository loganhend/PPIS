from View.view import View
from Model.model import Model


class BuyingTicketsController:
    def __init__(self, model, view, currUser):
        self.model = model
        self.view = view
        self.strategy = currUser.userType
        self.currUser = currUser
        self.cart = {}

    def addToCart(self, ticket):
        if self.cart.get(ticket) is None:
            self.cart[ticket] = 1
        else:
            self.cart[ticket] += 1

    def removeFromCart(self, ticket):
        if self.cart.get(ticket) is not None:
            self.cart[ticket] -= 1

    def pay(self):
        # обращается к модели и её полю Банк, проводит псевдо-операцию оплаты,
        # добавляет билеты пользователю в его хранилище
        pass


class ShowingTicketsController:
    def __init__(self, model, view, currUser):
        self.model = model
        self.view = view
        self.strategy = currUser.userType
        self.currUser = currUser

    def getUserTickets(self):
        return self.model.userStorage.getUser(self.currUser.id).ticketStorage

    def changeTicketDate(self):
        # обращается к модели, ищет визитора, ищет нужный билет, изменяет у него дату
        pass

    def returnTicket(self):
        # обращается к модели, ищет визитора, ищет нужный билет, удаляет билет у визитора
        pass

    def showTicket(self):
        # обращается к модели, ищет визитора, ищет нужный билет, берёт его ID и отрисовывает типа QR-код
        pass

    def changeTicketStatus(self):
        # обращается к модели, ищет визитора, ищет нужный билет, изменяет у него статус
        pass


class ReviewController:
    def __init__(self, model, view, currUser):
        self.model = model
        self.view = view
        self.strategy = currUser.userType
        self.currUser = currUser

    def addReview(self):
        #обращается к модели, добавляет ревью
        pass

    def changeReview(self):
        # обращается к модели, проверяет, есть ли такой отзыв, изменяет его
        pass

    def DeleteReview(self):
        # обращается к модели, проверяет, есть ли такой отзыв, удаляет его
        pass


class Controller:
    def __init__(self, model):
        self.model = model
        self.view = View(self, self.model)
        self.strategy = None
        self.currUser = None
        #self.reviewController = ReviewController(model, self.view, self.currUser)
        #self.showTicketController = ShowingTicketsController(model, self.view, self.currUser)
        #self.buyTicketController = BuyingTicketsController(model, self.view, self.currUser)

    def start(self):
        self.view.show_start()

    def showAttractionsScreen(self):
        self.view.show_AttractionsScreen()

    def showFoodPlacesScreen(self):
        self.view.show_FoodPlacesScreen()

    def showMainScreen(self):
        self.view.show_MainScreen()

    def showMenuScreen(self):
        self.view.show_MenuScreen()

    def showPersonalScreen(self):
        #if self.strategy = 1:
        if True:
            self.view.show_PersonalScreen()
        else:
            self.view.show_UserSearchScreen()

    def showTicketsHistoryScreen(self, login):
        self.view.show_TicketsHistoryScreen(login)

    def showUserSearchScreen(self):
        self.view.show_UserSearchScreen()

    def showUserTicketsScreen(self):
        self.view.show_UserTicketsScreen()

    def showParkScreen(self):
        self.view.show_ParkScreen()

    def showBuyingTicketsScreen(self):
        self.view.show_BuyingTicketsScreen()

    def showCreateAccScreen(self):
        self.view.show_CreateAccScreen()

    def showEnterAccScreen(self):
        self.view.show_EnterAccScreen()

    def showLocationScreen(self, loc):
        self.view.show_LocationScreen(loc)

    def showDeletionDialogue(self):
        self.view.show_DeletionDialogue()

    def showReviewDialogue(self):
        self.view.show_ReviewDialogue()

    def showTicketStatusDialogue(self):
        self.view.show_TicketStatusDialogue()

    # залогиниться
    def enterAcc(self, login, password):
        #обращается к модели, ищетм пользователя, проверяет совпадение пароля и логина, устанавливаем
        # self.currUser, определяем self.strategy = currUser.userType
        self.showMenuScreen()

    #зарегистрироваться
    def createAcc(self, login, password):
        # обращается к модели, проверяем, нет ли такого пользователя, проверяет совпадение пароля и логина,
        # устанавливаем self.currUser, определяем self.strategy = currUser.userType
        self.showMenuScreen()