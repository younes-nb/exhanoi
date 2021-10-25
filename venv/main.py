import sys
from PyQt6.QtWidgets import QApplication
from Controller.FirstController import FirstController

app = QApplication(sys.argv)
window = FirstController()
window.view.show()
sys.exit(app.exec())