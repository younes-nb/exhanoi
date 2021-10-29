from View.FirstView import FirstView
from Controller.MainController import MainController


class FirstController(FirstView):
    def __init__(self):
        super().__init__()
        self.view = FirstView()
        self.view.showButton.clicked.connect(self.showMainPage)
        self.view.speedDial.valueChanged.connect(self.speedLabelChange)

    def showMainPage(self):
        if (self.view.selectionMenu.currentText() in ('1', '2', '3', '4')):
            self.mainController = MainController(int(self.view.selectionMenu.currentText()),
                                                 (101 - self.view.speedDial.value()) * 100, self.view)
            self.mainController.mainView.show()
            self.view.hide()

    def speedLabelChange(self):
        self.view.speedLable.setText("Speed : {}%".format(self.view.speedDial.value()))
