from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtCore import Qt, QRect


class MainView(QWidget):
    def __init__(self, n):
        super().__init__()
        self.geometry = self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle("Exhanoi")
        self.setStyleSheet("background-color: #323232;")

        pegs_x = (130, 295, 460)
        pegs_y = 150
        for x in pegs_x:
            peg = QFrame(self)
            peg.setGeometry(x, pegs_y, 10, 350)
            peg.setFrameShape(QFrame.Shape.StyledPanel)
            peg.setStyleSheet(""" 
            background-color: lightgray; 
            border-radius: 5px; 
            """)

        ground = QFrame(self)
        ground.setGeometry(50, 495, 500, 25)
        ground.setFrameShape(QFrame.Shape.StyledPanel)
        ground.setStyleSheet(""" 
                background-color: #4C4C4C; 
                border-radius: 5px; 
                """)

        self.disks = []
        diskWidth = 150
        x = 0
        disk_y = 470
        self.disks_x = []
        self.disks_y = []
        for d in range(n * 3):
            disk_x = int(pegs_x[x] - (diskWidth / 2) + 5)
            self.disks_x.append(disk_x)
            self.disks_y.append(disk_y)
            disk = QFrame(self)
            disk.setToolTip(str(d + 1))
            disk.setGeometry(disk_x, disk_y, diskWidth, 20)
            disk.setFrameShape(QFrame.Shape.StyledPanel)
            disk.setStyleSheet("""  
                background-color: #F29C1F; 
                border-radius: 5px;
            """)
            self.disks.append(disk)
            diskWidth -= 10
            x += 1
            if (x > 2):
                x = 0
            if ((d + 1) % 3 == 0):
                disk_y -= 25

        buttons_y = 540
        self.manualButton = QPushButton("Manual Move", self)
        self.manualButton.setGeometry(50, buttons_y, 120, 35)
        self.manualButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.manualButton.setStyleSheet("""  
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

        self.automaticButton = QPushButton("Start Automatic Mode", self)
        self.automaticButton.setGeometry(200, buttons_y, 185, 35)
        self.automaticButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.automaticButton.setStyleSheet("""  
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

        self.resultButton = QPushButton("Show Result", self)
        self.resultButton.setGeometry(419, buttons_y, 130, 35)
        self.resultButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.resultButton.setStyleSheet("""  
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

        self.backButton = QPushButton("Back", self)
        self.backButton.setGeometry(10, 10, 55, 25)
        self.backButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.backButton.setStyleSheet("""  
            QPushButton:hover{  
                background-color: #F29C1F; 
                color: #4B4B4B;
            }    
            QPushButton{  
            background-color: #4B4B4B; 
            color: lightgray; 
            font-size: 16px;  
            border-radius: 5px; 
            border:1px solid #4B4B4B; 
            } 
        """)
