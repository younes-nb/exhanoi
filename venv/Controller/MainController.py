from View.MainView import MainView
from View.FirstView import FirstView
from Model.MainModel import MainModel
from PyQt6.QtWidgets import QFrame
from PyQt6.QtCore import QPropertyAnimation, QPointF, QSequentialAnimationGroup
from functools import partial


class MainController(MainView):
    def __init__(self, n, duration, firstView=FirstView):
        super().__init__(n)
        self.mainView = MainView(n)
        self.firstView = firstView
        self.duration = duration
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

    def initButtons(self):
        self.mainView.backButton.clicked.connect(self.initBackButton)
        self.mainView.manualButton.clicked.connect(self.initManualButton)
        self.mainView.automaticButton.clicked.connect(self.initAutomaticButton)
        self.mainView.resultButton.clicked.connect(self.initResultButton)
        self.mainView.pauseButton.clicked.connect(self.initPuaseButton)
        self.mainView.resumeButton.clicked.connect(self.initResumeButton)

    def initBackButton(self):
        self.mainView.hide()
        self.firstView.show()

    def initManualButton(self):
        self.enableButtons(False, self.mainView.manualButton)
        self.enableButtons(False, self.mainView.automaticButton)
        self.enableButtons(False, self.mainView.resultButton)
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
            self.enableButtons(False, self.mainView.manualButton)
            self.enableButtons(False, self.mainView.automaticButton)
            self.enableButtons(False, self.mainView.resultButton)

    def initAutomaticButton(self):
        self.enableButtons(False, self.mainView.manualButton)
        self.mainView.automaticButton.hide()
        self.mainView.pauseButton.show()
        self.mainView.resumeButton.show()
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

    def initResultButton(self):
        self.enableButtons(False, self.mainView.manualButton)
        self.enableButtons(False, self.mainView.automaticButton)
        self.enableButtons(False, self.mainView.resultButton)
        self.enableButtons(False, self.mainView.pauseButton)
        self.enableButtons(False, self.mainView.resumeButton)
        self.groupAnime.stop()
        y = 470
        for disk in self.mainView.disks:
            x = int(460 - (int(disk.width().__repr__()) / 2)) + 5
            disk.move(x, y)
            y -= 25

    def initPuaseButton(self):
        self.groupAnime.pause()
        self.enableButtons(True, self.mainView.resumeButton)
        self.enableButtons(False, self.mainView.pauseButton)

    def initResumeButton(self):
        self.groupAnime.resume()
        self.enableButtons(False, self.mainView.resumeButton)
        self.enableButtons(True, self.mainView.pauseButton)

    def moveDisk(self, sourcePeg, destinationPeg, destinationPeg_X, manual=True):
        x = int(destinationPeg_X - (int(self.mainView.disks[sourcePeg[-1]].width().__repr__()) / 2)) + 5
        if (destinationPeg == []):
            y = 470
        else:
            y = self.mainView.disks_y[destinationPeg[-1]] - 25
        if (manual):
            self.manualAnimation(self.mainView.disks_x[sourcePeg[-1]],
                                 self.mainView.disks_y[sourcePeg[-1]],
                                 x, y, sourcePeg[-1], self.duration)
        else:
            self.autoAnimation(self.mainView.disks_x[sourcePeg[-1]],
                               self.mainView.disks_y[sourcePeg[-1]],
                               x, y, sourcePeg[-1], self.duration)

    def manualAnimation(self, source_x, source_y, destination_x, destination_y, disk, duration):
        self.anim = QPropertyAnimation(self.mainView.disks[disk], b"pos")
        self.anim.setDuration(duration)
        self.anim.setStartValue(QPointF(source_x, source_y))
        self.anim.setKeyValueAt(0.4, QPointF(source_x, 120))
        self.anim.setKeyValueAt(0.6, QPointF(destination_x, 120))
        self.anim.setEndValue(QPointF(destination_x, destination_y))
        self.anim.start()
        self.mainView.disks_x[disk] = destination_x
        self.mainView.disks_y[disk] = destination_y
        self.anim.finished.connect(partial(self.enableButtons, True, self.mainView.automaticButton))
        self.anim.finished.connect(partial(self.enableButtons, True, self.mainView.manualButton))
        self.anim.finished.connect(partial(self.enableButtons, True, self.mainView.resultButton))

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

    def enableButtons(self, enable, button):
        if (enable):
            button.setEnabled(True)
            button.setStyleSheet("""  
                QPushButton:hover{  
                    background-color: #F29C1F; 
                    color: #4B4B4B;
                }    
                QPushButton{  
                background-color: #4B4B4B; 
                color: lightgray; 
                font-size: 17px;  
                border-radius: 5px; 
                border:1px solid #4B4B4B; 
                } 
            """)
        else:
            button.setDisabled(True)
            button.setStyleSheet("""  
                background-color:gray; 
                color: #4B4B4B; 
                font-size: 17px;  
                border-radius: 5px; 
                border:1px solid #4B4B4B; 
            """)
