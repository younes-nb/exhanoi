from View.MainView import MainView

class MainController(MainView):
    def __init__(self,count):
        super().__init__(count)
        self.mainView = MainView(count)
