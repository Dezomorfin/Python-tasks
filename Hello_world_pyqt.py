# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("First PyQt programm")
window.resize(300, 70)
label = QtWidgets.QLabel("<center>Vaggo production</center>")
btnQuit = QtWidgets.QPushButton("&Close window")
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
window.setLayot(vbox)
btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec_())