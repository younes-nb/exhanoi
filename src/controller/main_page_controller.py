from functools import partial

from PyQt6.QtCore import QPropertyAnimation, QPointF, QSequentialAnimationGroup

from src.model.model import Model
from src.view.first_page_view import FirstPageView
from src.view.main_page_view import MainPageView


class MainPageController(MainPageView):
    def __init__(self, n, duration, first_page_view=FirstPageView):
        super().__init__(n)
        self.anim = None
        self.main_page_view = MainPageView(n)
        self.first_page_view = first_page_view
        self.duration = duration
        main_model = Model()
        self.moves = main_model.exhanoi(n, 'A', 'B', 'C', )
        self.group_anime = QSequentialAnimationGroup(self)
        self.peg_A = []
        self.peg_B = []
        self.peg_C = []
        for disk in range(self.main_page_view.disks.__len__()):
            match (int(self.main_page_view.disks[disk].x().__repr__()) + (
                    int(self.main_page_view.disks[disk].width().__repr__()) / 2) - 5):
                case 130:
                    self.peg_A.append(disk)
                case 295:
                    self.peg_B.append(disk)
                case 460:
                    self.peg_C.append(disk)

        self.init_buttons()

    def init_buttons(self):
        self.main_page_view.back_button.clicked.connect(self.init_back_button)
        self.main_page_view.manual_button.clicked.connect(self.init_manual_button)
        self.main_page_view.automatic_button.clicked.connect(self.init_automatic_button)
        self.main_page_view.result_button.clicked.connect(self.init_result_button)
        self.main_page_view.pause_button.clicked.connect(self.init_pause_button)
        self.main_page_view.resume_button.clicked.connect(self.init_resume_button)

    def init_back_button(self):
        self.main_page_view.hide()
        self.first_page_view.show()

    def init_manual_button(self):
        enable_buttons(False, self.main_page_view.manual_button)
        enable_buttons(False, self.main_page_view.automatic_button)
        enable_buttons(False, self.main_page_view.result_button)
        try:
            match next(self.moves):
                case 'A', 'B':
                    self.move_disk(self.peg_A, self.peg_B, 295)
                    self.peg_B.append(self.peg_A.pop(-1))
                case 'A', 'C':
                    self.move_disk(self.peg_A, self.peg_C, 460)
                    self.peg_C.append(self.peg_A.pop(-1))
                case 'B', 'A':
                    self.move_disk(self.peg_B, self.peg_A, 130)
                    self.peg_A.append(self.peg_B.pop(-1))
                case 'B', 'C':
                    self.move_disk(self.peg_B, self.peg_C, 460)
                    self.peg_C.append(self.peg_B.pop(-1))
                case 'C', 'A':
                    self.move_disk(self.peg_C, self.peg_A, 130)
                    self.peg_A.append(self.peg_C.pop(-1))
                case 'C', 'B':
                    self.move_disk(self.peg_C, self.peg_B, 295)
                    self.peg_B.append(self.peg_C.pop(-1))

        except StopIteration:
            enable_buttons(False, self.main_page_view.manual_button)
            enable_buttons(False, self.main_page_view.automatic_button)
            enable_buttons(False, self.main_page_view.result_button)

    def init_automatic_button(self):
        enable_buttons(False, self.main_page_view.manual_button)
        self.main_page_view.automatic_button.hide()
        self.main_page_view.pause_button.show()
        self.main_page_view.resume_button.show()
        for move in self.moves:
            match move:
                case 'A', 'B':
                    self.move_disk(self.peg_A, self.peg_B, 295, False)
                    self.peg_B.append(self.peg_A.pop(-1))
                case 'A', 'C':
                    self.move_disk(self.peg_A, self.peg_C, 460, False)
                    self.peg_C.append(self.peg_A.pop(-1))
                case 'B', 'A':
                    self.move_disk(self.peg_B, self.peg_A, 130, False)
                    self.peg_A.append(self.peg_B.pop(-1))
                case 'B', 'C':
                    self.move_disk(self.peg_B, self.peg_C, 460, False)
                    self.peg_C.append(self.peg_B.pop(-1))
                case 'C', 'A':
                    self.move_disk(self.peg_C, self.peg_A, 130, False)
                    self.peg_A.append(self.peg_C.pop(-1))
                case 'C', 'B':
                    self.move_disk(self.peg_C, self.peg_B, 295, False)
                    self.peg_B.append(self.peg_C.pop(-1))
        self.group_anime.start()

    def init_result_button(self):
        enable_buttons(False, self.main_page_view.manual_button)
        enable_buttons(False, self.main_page_view.automatic_button)
        enable_buttons(False, self.main_page_view.result_button)
        enable_buttons(False, self.main_page_view.pause_button)
        enable_buttons(False, self.main_page_view.resume_button)
        self.group_anime.stop()
        y = 470
        for disk in self.main_page_view.disks:
            x = int(460 - (int(disk.width().__repr__()) / 2)) + 5
            disk.move(x, y)
            y -= 25

    def init_pause_button(self):
        self.group_anime.pause()
        enable_buttons(True, self.main_page_view.resume_button)
        enable_buttons(False, self.main_page_view.pause_button)

    def init_resume_button(self):
        self.group_anime.resume()
        enable_buttons(False, self.main_page_view.resume_button)
        enable_buttons(True, self.main_page_view.pause_button)

    def move_disk(self, source_peg, destination_peg, destination_peg_x, manual=True):
        x = int(destination_peg_x - (int(self.main_page_view.disks[source_peg[-1]].width().__repr__()) / 2)) + 5
        if not destination_peg:
            y = 470
        else:
            y = self.main_page_view.disks_y[destination_peg[-1]] - 25
        if manual:
            self.manual_animation(self.main_page_view.disks_x[source_peg[-1]],
                                  self.main_page_view.disks_y[source_peg[-1]],
                                  x, y, source_peg[-1], self.duration)
        else:
            self.auto_animation(self.main_page_view.disks_x[source_peg[-1]],
                                self.main_page_view.disks_y[source_peg[-1]],
                                x, y, source_peg[-1], self.duration)

    def manual_animation(self, source_x, source_y, destination_x, destination_y, disk, duration):
        self.anim = QPropertyAnimation(self.main_page_view.disks[disk], b"pos")
        self.anim.setDuration(duration)
        self.anim.setStartValue(QPointF(source_x, source_y))
        self.anim.setKeyValueAt(0.4, QPointF(source_x, 120))
        self.anim.setKeyValueAt(0.6, QPointF(destination_x, 120))
        self.anim.setEndValue(QPointF(destination_x, destination_y))
        self.anim.start()
        self.main_page_view.disks_x[disk] = destination_x
        self.main_page_view.disks_y[disk] = destination_y
        self.anim.finished.connect(partial(enable_buttons, True, self.main_page_view.automatic_button))
        self.anim.finished.connect(partial(enable_buttons, True, self.main_page_view.manual_button))
        self.anim.finished.connect(partial(enable_buttons, True, self.main_page_view.result_button))

    def auto_animation(self, source_x, source_y, destination_x, destination_y, disk, duration):
        anim = QPropertyAnimation(self.main_page_view.disks[disk], b"pos")
        anim.setDuration(duration)
        anim.setStartValue(QPointF(source_x, source_y))
        anim.setKeyValueAt(0.4, QPointF(source_x, 120))
        anim.setKeyValueAt(0.6, QPointF(destination_x, 120))
        anim.setEndValue(QPointF(destination_x, destination_y))
        self.main_page_view.disks_x[disk] = destination_x
        self.main_page_view.disks_y[disk] = destination_y
        self.group_anime.addAnimation(anim)


def enable_buttons(enable, button):
    if enable:
        button.setEnabled(True)
        button.setStyleSheet("""  
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
    else:
        button.setDisabled(True)
        button.setStyleSheet("""  
            background-color:gray; 
            color: #4B4B4B; 
            font-size: 17px;  
            border-radius: 5px; 
            border:1px solid #4B4B4B; 
        """)
