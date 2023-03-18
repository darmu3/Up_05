import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QListWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        colors = {0: 'White', 1: 'Blue', 2: 'Green'}

        color_map = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        positions = [(i, j) for i in range(1, 12) for j in range(1, 12)]

        for position, color_map in zip(positions, color_map):
            self.grid.setSpacing(0)
            self.label = QLabel(self)
            label_name = f'{position[0]}_{position[1]}'
            self.label.setObjectName(label_name)
            self.label.setText(f'{position[0]}:{position[1]}')
            self.label.setStyleSheet(f'min-width: 50px; '
                                     f'min-height: 50px; '
                                     f'border: 1px solid #444; '
                                     f'background-color: {colors[color_map]}')
            self.label.setAlignment(Qt.AlignCenter)
            self.label.installEventFilter(self)
            self.grid.addWidget(self.label, *position)

        self.move(350, 150)
        self.setWindowTitle('Board')
        self.show()

        # label = self.findChild(QLabel, '5_5')
        # print(label.text())
        # col = f'min-width: 50px; ' f'min-height: 50px; ' f'border: 1px solid #444; ' f'background-color: {colors[0]}'
        # if label.styleSheet() == col:
        #     print(f'{colors[0]}')
        # col2 = f'min-width: 50px; ' f'min-height: 50px; ' f'border: 1px solid #444; ' f'background-color: {colors[1]}'
        # if label.styleSheet() == col2:
        #     print(f'{colors[1]}')
        # col3 = f'min-width: 50px; ' f'min-height: 50px; ' f'border: 1px solid #444; ' f'background-color: {colors[2]}'
        # if label.styleSheet() == col3:
        #     print(f'{colors[2]}')

    def eventFilter(self, obj, e):
        if e.type() == 2:
            btn = e.button()
            if btn == 1:
                # self.label.setStyleSheet("background-color: Green")
                print(obj.objectName())
                obj.setStyleSheet("background-color: Green")
            elif btn == 2:
                # self.label.setStyleSheet("background-color: Blue")
                print(obj.objectName())
                obj.setStyleSheet("background-color: Blue")
        return super(QWidget, self).eventFilter(obj, e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
