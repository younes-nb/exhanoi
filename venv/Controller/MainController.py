from View.MainView import MainView
from View.FirstView import FirstView
from Model.MainModel import MainModel
from PyQt6.QtWidgets import QFrame


class MainController(MainView):
    def __init__(self, count, firstView=FirstView):
        super().__init__(count)
        self.mainView = MainView(count)
        self.firstView = firstView
        mainModel = MainModel()
        self.moves = mainModel.exhanoi(count, 'A', 'B', 'C', [])
        self.nextMove = 0
        self.rodA = []
        self.rodB = []
        self.rodC = []
        for disk in range(self.mainView.disks.__len__()):
            match (int(self.mainView.disks[disk].x().__repr__()) + (
                    int(self.mainView.disks[disk].width().__repr__()) / 2) - 5):
                case 130:
                    self.rodA.append(disk)
                case 295:
                    self.rodB.append(disk)
                case 460:
                    self.rodC.append(disk)

        self.initButtons()

    def initBackButton(self):
        self.mainView.hide()
        self.firstView.show()

    def initManualButton(self):
        try:
            match (self.moves[self.nextMove]):
                case ('A', 'B'):
                    self.moveDisk(self.rodA, self.rodB, 295)
                    self.rodB.append(self.rodA[-1])
                    self.rodA.pop(-1)
                    self.nextMove += 1
                case ('A', 'C'):
                    self.moveDisk(self.rodA, self.rodC, 460)
                    self.rodC.append(self.rodA[-1])
                    self.rodA.pop(-1)
                    self.nextMove += 1
                case ('B', 'A'):
                    self.moveDisk(self.rodB, self.rodA, 130)
                    self.rodA.append(self.rodB[-1])
                    self.rodB.pop(-1)
                    self.nextMove += 1
                case ('B', 'C'):
                    self.moveDisk(self.rodB, self.rodC, 460)
                    self.rodC.append(self.rodB[-1])
                    self.rodB.pop(-1)
                    self.nextMove += 1
                case ('C', 'A'):
                    self.moveDisk(self.rodC, self.rodA, 130)
                    self.rodA.append(self.rodC[-1])
                    self.rodC.pop(-1)
                    self.nextMove += 1
                case ('C', 'B'):
                    self.moveDisk(self.rodC, self.rodB, 295)
                    self.rodB.append(self.rodC[-1])
                    self.rodC.pop(-1)
                    self.nextMove += 1

        except Exception as e:
            print(e.__repr__())

    def initAutomaticButton(self):
        pass

    def initResultButton(self):
        pass

    def initButtons(self):
        self.mainView.backButton.clicked.connect(self.initBackButton)
        self.mainView.manualButton.clicked.connect(self.initManualButton)
        self.mainView.automaticButton.clicked.connect(self.initAutomaticButton)
        self.mainView.resultButton.clicked.connect(self.initResultButton)

    def moveDisk(self, startRod, endRod, endRodX):
        x = int(endRodX - (int(self.mainView.disks[startRod[-1]].width().__repr__()) / 2)) + 5
        if (endRod == []):
            y = 320
        else:
            y = int(int(self.mainView.disks[endRod[-1]].y().__repr__()) - 25)
        self.mainView.disks[startRod[-1]].move(x, y)
