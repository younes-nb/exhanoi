from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QComboBox
from PyQt6.QtCore import Qt

class MainView(QWidget):
    def __init__(self):
        super().__init__()
        self.geometry = self.setGeometry(100, 100, 600, 500)
        self.setWindowTitle("Exhanoi")
        self.setStyleSheet("background-color: #323232;")