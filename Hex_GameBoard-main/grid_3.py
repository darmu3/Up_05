import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel

colors = {0: 'White', 1: 'Blue', 2: 'Green'}

color_map = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.actual_color = None
        self.motion = 1
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        global color_map

        positions = [(i, j) for i in range(1, 12) for j in range(1, 12)]

        for position, color_map in zip(positions, color_map):
            self.grid.setSpacing(0)
            self.label = QLabel(self)
            self.label_name = f'{position[0]}_{position[1]}'
            self.label.setObjectName(self.label_name)
            self.label.setText(f'{position[0]}:{position[1]}')
            self.label.setStyleSheet(f'min-width: 50px; '
                                     f'min-height: 50px; '
                                     f'border: 2px solid #444; '
                                     f'background-color: {colors[color_map]}')
            self.label.setAlignment(Qt.AlignCenter)
            self.label.installEventFilter(self)
            self.grid.addWidget(self.label, *position)

        self.move(350, 150)
        self.setWindowTitle('Board')
        self.show()

    # def new_map(self, obj):
    #     z = 0
    #     for i in range(1, 12):
    #         for j in range(1, 12):
    #             if f'{i}_{j}' == obj.objectName:
    #                 color_map[z] = self.actual_color
    #                 print(z)
    #             print(color_map)
    #             z += 1

    def eventFilter(self, obj, e):
        if e.type() == 2:
            btn = e.button()
            if btn == 1:
                if self.motion == 1:
                    print(obj.objectName())
                    obj.setStyleSheet(f'background-color: {colors[2]}')
                    # self.actual_color = 2
                    self.motion = 2
                else:
                    print(obj.objectName())
                    obj.setStyleSheet(f'background-color: {colors[1]}')
                    # self.actual_color = 1
                    self.motion = 1

                # self.new_map(obj)

        return super(QWidget, self).eventFilter(obj, e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
