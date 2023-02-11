import sys
import os
from PyQt6.QtWidgets import QApplication
from src.controller.first_page_controller import FirstPageController


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


app = QApplication(sys.argv)
window = FirstPageController(resource_path("../media/hanoi.jpg"))
window.view.show()
sys.exit(app.exec())
