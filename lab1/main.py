import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLineEdit
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

from Curve import Curve, Point
from TravelScreen import TravelScreen
from CordinateAxes import CordinateAxes


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.__parameter = 10
        self.travel_screen = TravelScreen(0, 0)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Lab 1')
        input_a = QLineEdit(self)
        input_a.setMaximumWidth(80)
        input_a.move(5, 5)
        input_a.textChanged[str].connect(self.onChanged)
        self.show()

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            self.travel_screen.end_x = e.pos().x()
            self.travel_screen.end_y = e.pos().y()
            self.update()

    def mousePressEvent(self, e):
        if e.buttons() != Qt.RightButton:
            x, y = e.pos().x(), e.pos().y()
            self.travel_screen = TravelScreen(x, y)

    def onChanged(self, text):
        self.__takeParameter(text)
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawFigure(qp)
        qp.end()

    def drawFigure(self, qp):
        size = self.size()

        pen = QPen(Qt.white, 1, Qt.SolidLine)
        qp.setPen(pen)

        cordinate_axes = CordinateAxes(
            size.width(), size.height(), self.travel_screen)
        cordinate_axes.draw(qp)

        pen = QPen(Qt.red, 2, Qt.SolidLine)
        qp.setPen(pen)

        curve = Curve(qp, size.width(), size.height(),
                      self.__parameter, 0.5, self.travel_screen)
        curve.draw()

    def __takeParameter(self, text):
        try:
            self.__parameter = float(text)
        except Exception as e:
            self.__parameter = 10
        if self.__parameter <= 0:
            self.__parameter = 10


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
