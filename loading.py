import math, sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Overlay(QWidget):
    def __init__(self, parent=None):

        QWidget.__init__(self, parent)
        palette = QPalette(self.palette())
        palette.setColor(palette.Background, Qt.transparent)
        self.setPalette(palette)
        print('setting')

    def paintEvent(self, event):
        #print('paintevent')
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(event.rect(), QBrush(QColor(255, 255, 255, 127)))
        painter.setPen(QPen(Qt.NoPen))

        for i in range(1, 9):
            if self.counter - i == 0:
                # painter.setBrush(QBrush(QColor(245, 240, 240)))
                painter.setBrush(QBrush(QColor(10, 10, 10)))
            elif self.counter - i == -1:
                painter.setBrush(QBrush(QColor(180, 180, 180)))
            elif self.counter - i == -2:
                painter.setBrush(QBrush(QColor(150, 150, 150)))
            elif self.counter - i == -3:
                painter.setBrush(QBrush(QColor(120, 120, 120)))
            elif self.counter - i == -4:
                painter.setBrush(QBrush(QColor(100, 100, 100)))
            elif self.counter - i == -5:
                painter.setBrush(QBrush(QColor(70, 70, 70)))
            elif self.counter - i == -6:
                painter.setBrush(QBrush(QColor(50, 50, 50)))
            elif self.counter - i == -7:
                painter.setBrush(QBrush(QColor(20, 20, 20)))
            elif self.counter - i == 1:
                painter.setBrush(QBrush(QColor(180, 180, 180)))
            elif self.counter - i == 2:
                painter.setBrush(QBrush(QColor(150, 150, 150)))
            elif self.counter - i == 3:
                painter.setBrush(QBrush(QColor(120, 120, 120)))
            elif self.counter - i == 4:
                painter.setBrush(QBrush(QColor(100, 100, 100)))
            elif self.counter - i == 5:
                painter.setBrush(QBrush(QColor(70, 70, 70)))
            elif self.counter - i == 6:
                painter.setBrush(QBrush(QColor(50, 50, 50)))
            elif self.counter - i == 7:
                painter.setBrush(QBrush(QColor(20, 20, 20)))


            painter.drawEllipse(self.width() / 2 + 40 * math.cos(2 * math.pi * i / 8.0) - 10,
                                self.height() / 2 + 40 * math.sin(2 * math.pi * i / 8.0) - 10, 25, 25)
        painter.end()

    def showEvent(self, event):
        #print ('showevent')
        self.timer = self.startTimer(80)
        self.counter = 1
        #print('showevent -> e')

    def timerEvent(self, event):
        #print('timeevent')
        #print(self.counter)
        self.counter += 1
        self.update()
        if self.counter == 60:
            self.killTimer(self.timer)
            self.hide()
        elif self.counter == 9:
            self.counter = 1


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        widget = QWidget(self)
        self.editor = QTextEdit()
        self.editor.setPlainText("0123456789" * 100)
        layout = QGridLayout(widget)
        layout.addWidget(self.editor, 0, 0, 1, 3)
        button = QPushButton("Wait")
        layout.addWidget(button, 1, 1, 1, 1)

        self.setCentralWidget(widget)
        self.overlay = Overlay(self.centralWidget())
        # self.overlay.hide()

        button.clicked.connect(self.overlay.show)

    def resizeEvent(self, event):
        self.overlay.resize(event.size())
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())