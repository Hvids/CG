import sys
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QLineEdit, QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

from Wedge import Wedge
from TravelScreen import TravelScreen
from CordinateAxes import CordinateAxes
from Turn import Turn
from Point import Point
from Vector import Vector
import math
# from Action import Action


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.a = 100
        self.b = 50
        self.c = 70
        self.h = 70
        self.travel_screen = TravelScreen()
        self.vector_see = Vector(-1, -1, 1)
        self.turn = Turn()
        # self.Action()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('Lab 2')

        orthographic_projection = QCheckBox('Ортографическая проекция')
        orthographic_projection.move(5, 5)
        orthographic_projection.toggle()
        self.show()

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            end = Point(e.pos().x(), e.pos().y())
            self.travel_screen.point_end = end
            self.travel_screen.update_travel()
            self.update()
            self.travel_screen.point_start = end
        if e.buttons() == Qt.RightButton:
            end = e.pos().y()
            self.turn.end = end
            self.turn.update_turn()
            self.update()
            self.turn.start = end

    def mousePressEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            start = Point(e.pos().x(), e.pos().y())
            self.travel_screen.point_start = start
        if e.buttons() == Qt.RightButton:
            start = e.pos().y()
            self.turn.start = start

    def on_changed_a(self, text):
        self.a = self.__takeParameter(text)
        self.update()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawFigure(qp)
        qp.end()

    def drawFigure(self, qp):
        size = self.size()
        width = size.width()
        height = size.height()
        # pen = QPen(Qt.white, 1, Qt.SolidLine)
        # qp.setPen(pen)
        #
        # cordinate_axes = CordinateAxes(
        #     size.width(), size.height(), self.travel_screen)
        # cordinate_axes.draw(qp)

        pen = QPen(Qt.red, 2, Qt.SolidLine)
        qp.setPen(pen)

        wedge = Wedge(self.a, self.b, self.c, self.h)
        wedge.to_scale(k_x=width / 270, k_y=width / 280, k_z=1)
        wedge.to_turn_oz(phi=self.turn.phi)
        # wedge.to_turn_ox(phi=self.turn.phi)
        # wedge.to_turn_oy(phi=self.turn.phi)

        wedge.move(d_x=width / 4 - self.travel_screen.travel_x,
                   d_y=height / 4 - self.travel_screen.travel_y, d_z=1)

        wedge.clear(self.vector_see)
        wedge.to_isometric_transform(phi=math.pi / 5, tetta=math.pi / 5)

        # wedge.to_orthographic_projection_z()
        wedge.draw(qp)

    def __takeParameter(self, text):
        try:
            res = float(text)
        except Exception as e:
            res = 10
        if res <= 0:
            res = 10
        return res


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
