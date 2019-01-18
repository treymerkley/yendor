
#! /usr/bin/python
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Yendor')
    w.show()
    # label = QLabel('Hello World!')
    # label.show()

    sys.exit(app.exec_())
