#! /usr/bin/python
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QVBoxLayout, QHBoxLayout, QTabWidget,
                             QRadioButton, QComboBox)

# pylint: disable=too-many-instance-attributes
# muting this until I learn how to sequester different
# aspects of the UI into different classes/files

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Yendor'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.table_widget = TableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.show()

class TableWidget(QWidget):

    def __init__(self, parent):
        super(TableWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # List of tabs and their names
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.addTab(self.tab1, "NPCs")
        self.tabs.addTab(self.tab2, "Places")
        self.tabs.addTab(self.tab3, "Items")
        self.tabs.addTab(self.tab4, "Premise")

        # Contents of tabs
        ## NPC tab (tab1)
        self.tab1.layout = QHBoxLayout(self)

        self.speciesComboBox = QComboBox()
        listOfSpecies = ('Dragonborn', 'Dwarf', 'Eldarin', 'Elf',
                         'Halfling', 'Human', 'Tiefling', 'Goblin')
        self.speciesComboBox.addItems(listOfSpecies)

        self.levelComboBox = QComboBox()
        for i in range(1, 31):
            self.levelComboBox.addItem(str(i))
            i += 1

        self.classesComboBox = QComboBox()
        listOfClasses = ('Fighter', 'Rogue', 'Mage', 'Cleric')
        self.classesComboBox.addItems(listOfClasses)

        # adding widgets to layout
        self.tab1.layout.addWidget(self.levelComboBox)
        self.tab1.layout.addWidget(self.speciesComboBox)
        self.tab1.layout.addWidget(self.classesComboBox)

        # adding layout to tab
        self.tab1.setLayout(self.tab1.layout)

        ## Places tab (tab2)

        ## Items tab (tab3)

        ## Premise tab (tab4)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
