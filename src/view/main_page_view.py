from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QPushButton, QFrame


class MainPageView(QWidget):
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
        disk_width = 150
        x = 0
        disk_y = 470
        self.disks_x = []
        self.disks_y = []
        for d in range(n * 3):
            disk_x = int(pegs_x[x] - (disk_width / 2) + 5)
            self.disks_x.append(disk_x)
            self.disks_y.append(disk_y)
            disk = QFrame(self)
            disk.setToolTip(str(d + 1))
            disk.setGeometry(disk_x, disk_y, disk_width, 20)
            disk.setFrameShape(QFrame.Shape.StyledPanel)
            disk.setStyleSheet("""  
                background-color: #F29C1F; 
                border-radius: 5px;
            """)
            self.disks.append(disk)
            disk_width -= 10
            x += 1
            if x > 2:
                x = 0
            if (d + 1) % 3 == 0:
                disk_y -= 25

        buttons_y = 540
        self.manual_button = QPushButton("Manual Move", self)
        self.manual_button.setGeometry(50, buttons_y, 120, 35)
        self.manual_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.manual_button.setStyleSheet("""  
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

        self.automatic_button = QPushButton("Start Automatic Mode", self)
        self.automatic_button.setGeometry(200, buttons_y, 185, 35)
        self.automatic_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.automatic_button.setStyleSheet("""  
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

        self.pause_button = QPushButton("Pause", self)
        self.pause_button.hide()
        self.pause_button.setGeometry(200, buttons_y, 90, 35)
        self.pause_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.pause_button.setStyleSheet("""  
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

        self.resume_button = QPushButton("Resume", self)
        self.resume_button.hide()
        self.resume_button.setGeometry(296, buttons_y, 90, 35)
        self.resume_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.resume_button.setDisabled(True)
        self.resume_button.setStyleSheet("""  
            background-color:gray; 
            color: #4B4B4B; 
            font-size: 17px;  
            border-radius: 5px; 
            border:1px solid #4B4B4B; 
        """)

        self.result_button = QPushButton("Show Result", self)
        self.result_button.setGeometry(419, buttons_y, 130, 35)
        self.result_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.result_button.setStyleSheet("""  
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

        self.back_button = QPushButton("Back", self)
        self.back_button.setGeometry(10, 10, 55, 25)
        self.back_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.back_button.setStyleSheet("""  
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
