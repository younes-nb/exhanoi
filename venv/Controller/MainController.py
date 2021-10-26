from View.MainView import MainView
from View.FirstView import FirstView
from Model.MainModel import MainModel
from PyQt6.QtWidgets import QFrame


class MainController(MainView):
    def __init__(self, n, firstView=FirstView):
        super().__init__(n)
        self.mainView = MainView(n)
        self.firstView = firstView
        mainModel = MainModel()
        self.moves = mainModel.exhanoi(n, 'A', 'B', 'C', )
        self.peg_A = []
        self.peg_B = []
        self.peg_C = []
        for disk in range(self.mainView.disks.__len__()):
            match (int(self.mainView.disks[disk].x().__repr__()) + (
                    int(self.mainView.disks[disk].width().__repr__()) / 2) - 5):
                case 130:
                    self.peg_A.append(disk)
                case 295:
                    self.peg_B.append(disk)
                case 460:
                    self.peg_C.append(disk)

        self.initButtons()

    def initBackButton(self):
        self.mainView.hide()
        self.firstView.show()

    def initManualButton(self):
        try:
            match (next(self.moves)):
                case ('A', 'B'):
                    self.moveDisk(self.peg_A, self.peg_B, 295)
                    self.peg_B.append(self.peg_A.pop(-1))
                case ('A', 'C'):
                    self.moveDisk(self.peg_A, self.peg_C, 460)
                    self.peg_C.append(self.peg_A.pop(-1))
                case ('B', 'A'):
                    self.moveDisk(self.peg_B, self.peg_A, 130)
                    self.peg_A.append(self.peg_B.pop(-1))
                case ('B', 'C'):
                    self.moveDisk(self.peg_B, self.peg_C, 460)
                    self.peg_C.append(self.peg_B.pop(-1))
                case ('C', 'A'):
                    self.moveDisk(self.peg_C, self.peg_A, 130)
                    self.peg_A.append(self.peg_C.pop(-1))
                case ('C', 'B'):
                    self.moveDisk(self.peg_C, self.peg_B, 295)
                    self.peg_B.append(self.peg_C.pop(-1))

        except StopIteration:
            self.mainView.manualButton.setDisabled(True)
            self.mainView.automaticButton.setDisabled(True)
            self.mainView.resultButton.setDisabled(True)

    def initAutomaticButton(self):
        for move in self.moves:
            match (move):
                case ('A', 'B'):
                    self.moveDisk(self.peg_A, self.peg_B, 295)
                    self.peg_B.append(self.peg_A.pop(-1))
                case ('A', 'C'):
                    self.moveDisk(self.peg_A, self.peg_C, 460)
                    self.peg_C.append(self.peg_A.pop(-1))
                case ('B', 'A'):
                    self.moveDisk(self.peg_B, self.peg_A, 130)
                    self.peg_A.append(self.peg_B.pop(-1))
                case ('B', 'C'):
                    self.moveDisk(self.peg_B, self.peg_C, 460)
                    self.peg_C.append(self.peg_B.pop(-1))
                case ('C', 'A'):
                    self.moveDisk(self.peg_C, self.peg_A, 130)
                    self.peg_A.append(self.peg_C.pop(-1))
                case ('C', 'B'):
                    self.moveDisk(self.peg_C, self.peg_B, 295)
                    self.peg_B.append(self.peg_C.pop(-1))

    def initResultButton(self):
        pass

    def initButtons(self):
        self.mainView.backButton.clicked.connect(self.initBackButton)
        self.mainView.manualButton.clicked.connect(self.initManualButton)
        self.mainView.automaticButton.clicked.connect(self.initAutomaticButton)
        self.mainView.resultButton.clicked.connect(self.initResultButton)

    def moveDisk(self, sourcePeg, destinationPeg, destinationPeg_X):
        x = int(destinationPeg_X - (int(self.mainView.disks[sourcePeg[-1]].width().__repr__()) / 2)) + 5
        if (destinationPeg == []):
            y = 470
        else:
            y = int(int(self.mainView.disks[destinationPeg[-1]].y().__repr__()) - 25)
        self.mainView.disks[sourcePeg[-1]].move(x, y)
