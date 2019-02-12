
#! /usr/bin/python3
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout,
                             QComboBox, QCheckBox, QLabel,
                             QPushButton, QTextEdit, QScrollArea,
                             QLineEdit)

from ..math import charactergen

def tab():
    # Initializing the complete layout
    tab.layout = QHBoxLayout()

    nameLineEditLabel = QLabel("Name:")
    nameLineEdit = QLineEdit()
    # levelComboBoxLabel.setText("Level:")

    # This sets up the level scaling for the resulting character. The current
    # cap is at 30, but the algorithm should continue to function to any level.
    levelComboBoxLabel = QLabel()
    levelComboBoxLabel.setText("Level:")
    levelComboBox = QComboBox()
    for i in range(1, 31):
        levelComboBox.addItem(str(i))
        i += 1

    # This sets up the elements box
    elementsComboBoxLabel = QLabel()
    elementsComboBoxLabel.setText("Element:")
    elementsComboBox = QComboBox()
    listOfElements = ('Air', 'Earth', 'Water', 'Fire', 'Forest')
    elementsComboBox.addItems(listOfElements)

    # This sets up the elements box
    skillsComboBoxLabel = QLabel()
    skillsComboBoxLabel.setText("Skills:")
    skillsComboBox = QComboBox()
    listOfSkills = ('')
    skillsComboBox.addItems(listOfSkills)
    
    # This is a toggle modifier to increase the strength of the monster and the
    # loot it's carrying. It's entirely optional and can be removed, or the
    # strength of the modifier can be changed in the "math" folder.
    bossCheckBoxLabel = QLabel()
    bossCheckBoxLabel.setText("Boss:")
    bossCheckBox = QCheckBox()

    # These are the buttons for saving and generating new NPCs.
    saveButton = QPushButton("Save")

    bottomButtonsLayout = QHBoxLayout()
    bottomButtonsLayout.addStretch(1)
    bottomButtonsLayout.addWidget(saveButton)

    # This builds the textbox that you see the resulting character in

    mainTextBox = QTextEdit()
   # mainTextBox.moveCursor(QTextCursor.Start)
    textBoxLayout = QHBoxLayout()
    textBoxLabel = QLabel("Description: ")
    textBoxLayout.addWidget(textBoxLabel)
    textBoxLayout.addWidget(mainTextBox)

    # This creates the layout for the controls. Any new fields should
    # follow this same general convention.
    controls = QScrollArea()
    controls.setFixedHeight(100)
    controls.setWidgetResizable(False)
    controlsLayout = QHBoxLayout(controls)

    controls.setWidget(controlsLayout.widget())

    controlsLayout.addWidget(levelComboBoxLabel)
    controlsLayout.addWidget(levelComboBox)
    controlsLayout.addWidget(nameLineEditLabel)
    controlsLayout.addWidget(nameLineEdit)
    controlsLayout.addWidget(skillsComboBoxLabel)
    controlsLayout.addWidget(skillsComboBox)
    controlsLayout.addWidget(elementsComboBoxLabel)
    controlsLayout.addWidget(elementsComboBox)
    controlsLayout.addWidget(bossCheckBoxLabel)
    controlsLayout.addWidget(bossCheckBox)

    # Adds all of the disparate groups of controls to the total layout
    tab.layout.addWidget(controls)
    tab.layout.addLayout(textBoxLayout)
    tab.layout.addLayout(bottomButtonsLayout)

    # sends the layout to core.py
    return tab.layout
