# -*- coding: utf-8 -*-

"""
Author: Tarren Peterson
Last edited: March 2018
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Demo App')


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
