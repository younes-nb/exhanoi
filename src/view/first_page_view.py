from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QDial


class FirstPageView(QWidget):
    def __init__(self, path):
        super().__init__()
        self.geometry = self.setGeometry(100, 100, 500, 450)
        self.setWindowTitle("Exhanoi")
        self.setStyleSheet("background-color: #323232;")

        self.layout = QVBoxLayout(self)

        hanoi_image = QLabel()
        hanoi_image.setPixmap(QPixmap(path))

        hanoi_label = QLabel("Exhanoi")
        hanoi_label.setStyleSheet("""  
            color: #F29C1F;  
            font-size: 50px;   
            margin-left: 10px;
        """)

        self.selection_menu = QComboBox()
        self.selection_menu.setFixedSize(225, 30)
        self.selection_menu.setStyleSheet("""
                    color: #F29C1F;
                    background-color: #4B4B4B; 
                    padding :5px;  
                    font-size :15px;  
                """)
        self.selection_menu.setPlaceholderText("Number of disks in each rod")
        for num in range(1, 5):
            self.selection_menu.addItem(str(num))

        self.speed_dial = QDial()
        self.speed_dial.setFixedSize(70, 70)
        self.speed_dial.setWrapping(True)
        self.speed_dial.setRange(1, 100)
        self.speed_dial.setValue(50)
        self.speed_dial.setNotchesVisible(True)
        self.speed_dial.setNotchTarget(5)
        self.speed_dial.setCursor(Qt.CursorShape.PointingHandCursor)

        self.speed_label = QLabel("Speed : {}%".format(self.speed_dial.value()))
        self.speed_label.setStyleSheet("""  
            color: #F29C1F;  
            font-size: 17px;   
        """)

        speed_section = QHBoxLayout()
        speed_section.addWidget(self.speed_dial)
        speed_section.addWidget(self.speed_label)

        self.show_button = QPushButton("Show")
        self.show_button.setFixedSize(95, 35)
        self.show_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.show_button.setStyleSheet("""
                    QPushButton:hover{
                        background-color: #F29C1F;
                        color: #4B4B4B;
                    }
                    QPushButton{
                        background-color: #4B4B4B;
                        color: #F29C1F;
                        font-size: 18px;
                        border-radius: 5px;
                        border:1px solid #4B4B4B;
                        padding: 5px;
                    }
                """)

        self.layout.addWidget(hanoi_image)
        self.layout.addWidget(hanoi_label)
        self.layout.addWidget(self.selection_menu, 1, Qt.AlignmentFlag.AlignCenter)
        self.layout.addLayout(speed_section)
        self.layout.addWidget(self.show_button, 1, Qt.AlignmentFlag.AlignCenter)

        self.layout.addStretch(1)
        self.layout.setSpacing(20)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
