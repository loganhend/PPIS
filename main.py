from Model.model import Model
from Controller.controller import Controller

class Main:
    def __init__(self):
        self.model = Model()
        self.controller = Controller(self.model)

    def build(self):
        self.controller.start()

if __name__ == '__main__':
    main = Main()
    main.build()