from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtCore import Qt, QRect


class MainView(QWidget):
    def __init__(self, count):
        super().__init__()
        self.geometry = self.setGeometry(100, 100, 600, 500)
        self.setWindowTitle("Exhanoi")
        self.setStyleSheet("background-color: #323232;")

        rods_x = (130, 295, 460)
        for x in rods_x:
            rod = QFrame(self)
            rod.setGeometry(x, 100, 10, 250)
            rod.setFrameShape(QFrame.Shape.StyledPanel)
            rod.setStyleSheet(""" 
            background-color: lightgray; 
            border-radius: 5px; 
            """)

        ground = QFrame(self)
        ground.setGeometry(50, 345, 500, 25)
        ground.setFrameShape(QFrame.Shape.StyledPanel)
        ground.setStyleSheet(""" 
                background-color: #4C4C4C; 
                border-radius: 5px; 
                """)

        self.disks = []
        diskWidth = 120
        for disk_x in rods_x:
            disk_y = 320
            for d in range(count):
                disk = QFrame(self)
                x = int(disk_x - (diskWidth / 2)+5)
                disk.setGeometry(x, disk_y, diskWidth, 20)
                disk.setFrameShape(QFrame.Shape.StyledPanel)
                disk.setStyleSheet("""  
                    background-color: #F29C1F; 
                    border-radius: 5px;
                """)
                self.disks.append(disk)
                diskWidth -= 10
                disk_y -= 25
