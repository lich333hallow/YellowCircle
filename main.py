import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from UI import Ui_MainWindow


class RandomCircle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.permission = False

        self.pushButton.clicked.connect(self.paint)

    def paint(self):
        self.permission = True
        self.update()

    def paintEvent(self, event):
        if self.permission is True:
            qp = QPainter()

            qp.begin(self)
            self.draw_random_circle(qp)
            qp.end()
        self.permission = False

    def draw_random_circle(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        position_x = randint(5, self.width() - 5)
        position_y = randint(5, self.height() - 5)
        max_radius = min((self.width() - position_x, position_x, position_y, self.height() - position_y))
        radius = randint(4, max_radius)
        qp.drawEllipse(position_x, position_y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    rc = RandomCircle()
    rc.show()
    sys.exit(app.exec_())
