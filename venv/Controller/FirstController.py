from View.FirstView import FirstView
from Controller.MainController import MainController


class FirstController(FirstView):
    def __init__(self):
        super().__init__()
        self.view = FirstView()
        self.view.showButton.clicked.connect(self.showMainPage)

    def showMainPage(self):
        if (self.view.selectionMenu.currentText() in ('1', '2', '3')):
            self.mainController = MainController(int(self.view.selectionMenu.currentText()), self.view)
            self.mainController.mainView.show()
            self.view.hide()
