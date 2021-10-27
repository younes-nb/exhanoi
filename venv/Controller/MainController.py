from View.MainView import MainView
from View.FirstView import FirstView
from Model.MainModel import MainModel
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import QPropertyAnimation, QPointF, QSequentialAnimationGroup
import time, sched


class MainController(MainView):
    def __init__(self, n, firstView=FirstView):
        super().__init__(n)
        self.mainView = MainView(n)
        self.firstView = firstView
        mainModel = MainModel()
        self.moves = mainModel.exhanoi(n, 'A', 'B', 'C', )
        self.groupAnime = QSequentialAnimationGroup(self)
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
        self.mainView.manualButton.setDisabled(True)
        self.mainView.automaticButton.setDisabled(True)
        self.mainView.resultButton.setDisabled(True)
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
        try:
            for move in self.moves:
                match (move):
                    case ('A', 'B'):
                        self.moveDisk(self.peg_A, self.peg_B, 295, False)
                        self.peg_B.append(self.peg_A.pop(-1))
                    case ('A', 'C'):
                        self.moveDisk(self.peg_A, self.peg_C, 460, False)
                        self.peg_C.append(self.peg_A.pop(-1))
                    case ('B', 'A'):
                        self.moveDisk(self.peg_B, self.peg_A, 130, False)
                        self.peg_A.append(self.peg_B.pop(-1))
                    case ('B', 'C'):
                        self.moveDisk(self.peg_B, self.peg_C, 460, False)
                        self.peg_C.append(self.peg_B.pop(-1))
                    case ('C', 'A'):
                        self.moveDisk(self.peg_C, self.peg_A, 130, False)
                        self.peg_A.append(self.peg_C.pop(-1))
                    case ('C', 'B'):
                        self.moveDisk(self.peg_C, self.peg_B, 295, False)
                        self.peg_B.append(self.peg_C.pop(-1))
                self.groupAnime.start()
        except Exception as e:
            print(e)

    def initResultButton(self):
        pass

    def initButtons(self):
        self.mainView.backButton.clicked.connect(self.initBackButton)
        self.mainView.manualButton.clicked.connect(self.initManualButton)
        self.mainView.automaticButton.clicked.connect(self.initAutomaticButton)
        self.mainView.resultButton.clicked.connect(self.initResultButton)

    def moveDisk(self, sourcePeg, destinationPeg, destinationPeg_X, manual=True):
        try:
            x = int(destinationPeg_X - (int(self.mainView.disks[sourcePeg[-1]].width().__repr__()) / 2)) + 5
            if (destinationPeg == []):
                y = 470
            else:
                y = int(int(self.mainView.disks[destinationPeg[-1]].y().__repr__()) - 25)
            if (manual):
                self.manualAnimation(int(self.mainView.disks[sourcePeg[-1]].x().__repr__()),
                                     int(self.mainView.disks[sourcePeg[-1]].y().__repr__()),
                                     x, y, sourcePeg[-1], 5000)
            else:
                if (destinationPeg == []):
                    y = 470
                else:
                    y = self.mainView.disks_y[destinationPeg[-1]] - 25

                self.autoAnimation(self.mainView.disks_x[sourcePeg[-1]],
                                   self.mainView.disks_y[sourcePeg[-1]],
                                   x, y, sourcePeg[-1], 1000)
        except Exception as e:
            print(e)

    def manualAnimation(self, source_x, source_y, destination_x, destination_y, disk, duration):
        self.anim = QPropertyAnimation(self.mainView.disks[disk], b"pos")
        self.anim.setDuration(duration)
        self.anim.setStartValue(QPointF(source_x, source_y))
        self.anim.setKeyValueAt(0.4, QPointF(source_x, 120))
        self.anim.setKeyValueAt(0.6, QPointF(destination_x, 120))
        self.anim.setEndValue(QPointF(destination_x, destination_y))
        self.anim.start()
        self.anim.finished.connect(self.enableButtons)

    def autoAnimation(self, source_x, source_y, destination_x, destination_y, disk, duration):
        anim = QPropertyAnimation(self.mainView.disks[disk], b"pos")
        anim.setDuration(duration)
        anim.setStartValue(QPointF(source_x, source_y))
        anim.setKeyValueAt(0.4, QPointF(source_x, 120))
        anim.setKeyValueAt(0.6, QPointF(destination_x, 120))
        anim.setEndValue(QPointF(destination_x, destination_y))
        self.mainView.disks_x[disk] = destination_x
        self.mainView.disks_y[disk] = destination_y
        self.groupAnime.addAnimation(anim)

    def enableButtons(self):
        self.mainView.manualButton.setEnabled(True)
        self.mainView.automaticButton.setEnabled(True)
        self.mainView.resultButton.setEnabled(True)
