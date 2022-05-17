from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

def runButton():

    print("Переход на файлы с доп. информацией")

def mainApp():

    work = QApplication(sys.argv)
    okno = QMainWindow()

    okno.setWindowTitle("Моя площадка для игры")
    okno.setGeometry(700, 300, 700, 650)

    text = QtWidgets.QLabel(okno)
    text.setText("Об авторе")
    text.move(319,10)
    text.adjustSize()


    klik =  QtWidgets.QPushButton(okno)
    klik.move(200, 200)
    klik.setText("Об работах")
    klik.setFixedWidth(300)
    klik.clicked.connect(runButton)


    klik2 =  QtWidgets.QPushButton(okno)
    klik2.move(200, 300)
    klik2.setText("Смотря что придумаю")
    klik2.setFixedWidth(300)
    klik2.clicked.connect(runButton)


    okno.show()
    sys.exit(work.exec_())








mainApp()