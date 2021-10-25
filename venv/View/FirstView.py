from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QComboBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class FirstView(QWidget):
    def __init__(self):
        super().__init__()
        self.geometry = self.setGeometry(100, 100, 500, 450)
        self.setWindowTitle("Exhanoi")
        self.setStyleSheet("background-color: #323232;")

        self.layout = QVBoxLayout(self)

        hanoiImage = QLabel()
        hanoiImage.setPixmap(QPixmap('E:\Younes\Programming\Projects\Exhanoi\\venv\View\hanoi.jpg'))

        hanoiLabel = QLabel("Exhanoi")
        hanoiLabel.setStyleSheet("""  
            color: #F29C1F;  
            font-size: 50px;   
            margin-left: 10px;
        """)

        self.selectionMenu = QComboBox()
        self.selectionMenu.setFixedSize(225, 30)
        self.selectionMenu.setStyleSheet("""
                    color: #F29C1F;
                    background-color: #4B4B4B; 
                    padding :5px;  
                    font-size :15px;  
                """)
        self.selectionMenu.setPlaceholderText("Number of disks in each rod")
        for num in range(1, 4):
            self.selectionMenu.addItem(str(num))

        self.showButton = QPushButton("Show")
        self.showButton.setFixedSize(95, 35)
        self.showButton.setCursor(Qt.CursorShape.PointingHandCursor)
        self.showButton.setStyleSheet("""
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

        self.layout.addWidget(hanoiImage)
        self.layout.addWidget(hanoiLabel)
        self.layout.addWidget(self.selectionMenu)
        self.layout.addWidget(self.showButton)

        self.layout.addStretch(1)
        self.layout.setSpacing(20)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
