import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLineEdit, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QTimer

from Curve import Curve, Point
from TravelScreen import TravelScreen
from CordinateAxes import CordinateAxes
from Turn import Turn
import math


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.__parameter = 10
        self.travel_screen = TravelScreen()
        self.phi = 0
        self.step = 0.5
        self.timer = QTimer()
        self.timer.timeout.connect(self.route)
        self.timer.start(1)
        self.turn = Turn()
        self.scale = 1
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Lab 1')
        self.label_a = QLabel(self)
        self.label_a.setText('a')
        self.label_a.move(90, 5)
        self.label_step = QLabel(self)

        self.label_step.setText('step')
        self.label_step.move(90, 30)
        input_a = QLineEdit(self)
        input_a.setMaximumWidth(80)
        input_step = QLineEdit(self)
        input_step.move(5, 30)
        input_step.setMaximumWidth(80)
        input_a.move(5, 5)
        input_a.textChanged[str].connect(self.onChanged)
        input_step.textChanged[str].connect(self.onChangedStep)

        btn1 = QPushButton('+', self)
        btn2 = QPushButton('-', self)
        btn1.move(200, 5)
        btn2.move(200, 30)
        btn1.clicked.connect(self.onScalePlus)
        btn2.clicked.connect(self.onScaleMinus)
        self.show()

    def onScalePlus(self):
        self.scale += 1
        self.update()

    def onScaleMinus(self):
        self.scale -= 1
        if self.scale < 1:
            self.scale = 1
        self.update()

    def onChangedStep(self, text):
        try:
            self.step = float(text) / 10
        except Exception as e:
            print('lol')
            self.step = 0.5
        if self.step <= 0:
            self.step = 0.5

        print(self.step)
        self.update()

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            end = Point(e.pos().x(), e.pos().y())
            self.travel_screen.point_start = self.travel_screen.point_end
            self.travel_screen.point_end = end
            self.travel_screen.update_travel()
            self.update()
        if e.buttons() == Qt.RightButton:
            end = e.pos().y()
            self.turn.end = end
            self.turn.update_turn()
            self.update()

    def mousePressEvent(self, e):
        if e.buttons() == Qt.LeftButton:

            start = Point(e.pos().x(), e.pos().y())
            self.travel_screen.point_start = start
            self.travel_screen.point_end = start
        if e.buttons() == Qt.RightButton:

            start = e.pos().y()
            self.turn.start = start

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
            size.width(), size.height(), self.travel_screen, self.scale * 10)
        cordinate_axes.draw(qp)

        pen = QPen(Qt.red, 2, Qt.SolidLine)
        qp.setPen(pen)

        curve = Curve(qp, size.width(), size.height(),
                      self.__parameter, self.step, self.travel_screen, self.phi, self.scale)
        curve.draw()

    def route(self):
        try:
            self.phi = (self.phi + 0.1)
        except Exception as e:
            self.phi = 0

        self.update()

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
