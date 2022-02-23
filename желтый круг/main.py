import sys
from PyQt5 import uic
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui.ui", self)

        self.flag = False
        self.pushButton.clicked.connect(self.clicked)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(255, 255, 0))
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        if self.flag:
            for i in range(randint(1, 100)):
                self.x = randint(0, 650)
                self.y = randint(0, 650)
                self.r = randint(10, 60)
                qp.drawEllipse(self.x, self.y, self.r, self.r)

    def clicked(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.exit(app.exec_())