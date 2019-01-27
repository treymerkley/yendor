import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QVBoxLayout, QHBoxLayout, QTabWidget,
                             QComboBox, QCheckBox, QLabel)

app = QApplication(sys.argv)
from yendor import gui

layout = QVBoxLayout()

# List of tabs and their names
tabs = QTabWidget()
tab1 = QWidget()
tab2 = QWidget()
tab3 = QWidget()
tab4 = QWidget()

tabs.addTab(tab1, "NPCs")
tabs.addTab(tab2, "Places")
tabs.addTab(tab3, "Items")
tabs.addTab(tab4, "Premise")

tab1.layout = gui.npc.tab()
tab2.layout = gui.places.tab()
tab3.layout = gui.items.tab()
tab4.layout = gui.premise.tab()

sys.exit(app.exec_())
