from src.view.first_page_view import FirstPageView
from src.controller.main_page_controller import MainPageController


class FirstPageController(FirstPageView):
    def __init__(self, path):
        super().__init__(path)
        self.main_controller = None
        self.view = FirstPageView(path)
        self.view.show_button.clicked.connect(self.show_main_page)
        self.view.speed_dial.valueChanged.connect(self.speed_label_change)

    def show_main_page(self):
        if self.view.selection_menu.currentText() in ('1', '2', '3', '4'):
            self.main_controller = MainPageController(int(self.view.selection_menu.currentText()),
                                                      (101 - self.view.speed_dial.value()) * 100, self.view)
            self.main_controller.main_page_view.show()
            self.view.hide()

    def speed_label_change(self):
        self.view.speed_label.setText("Speed : {}%".format(self.view.speed_dial.value()))
