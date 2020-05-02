from sys import argv
from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('USB-CAN Analyzer')
        self.setGeometry(100, 100, 800, 600)
        self.setMinimumHeight(500)
        self.setMinimumWidth(500)
        self.setMaximumHeight(800)
        self.setMaximumWidth(1000)


def main():
    myApp = QApplication(argv)
    window = Window()
    window.show()

    myApp.exec_()
    exit()


if __name__ == '__main__':
    main()