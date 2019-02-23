#! /usr/bin/python3
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout,
                             QComboBox, QCheckBox, QLabel,
                             QPushButton, QTextEdit, QScrollArea)
from PyQt5.QtCore import Qt

from ..math import charactergen


class Tab:

    def __init__(self):
        self.tab()

    def tab(self):
        # Initializing the complete layout
        self.layout = QVBoxLayout()

        # The list of species to choose from. Change the values
        # in the listOfSpecies list to get different results on the page.
        speciesComboBoxLabel = QLabel("Species:")
        self.speciesComboBox = QComboBox()
        listOfSpecies = ('Dragonborn', 'Dwarf', 'Eldarin', 'Elf',
                         'Halfling', 'Human', 'Tiefling', 'Goblin',
                         'Slime', 'Random Appropriate Monster')
        self.speciesComboBox.addItems(listOfSpecies)

        # This sets up the level scaling for the resulting
        # character. The current cap is at 30, but the
        # algorithm should continue to function to any level.
        levelComboBoxLabel = QLabel("Level:")
        self.levelComboBox = QComboBox()
        for i in range(1, 31):
            self.levelComboBox.addItem(str(i))
            i += 1

        # This sets up the list of classes. Only four basic
        # classes are here now, but to add more, add a comma
        # after the last item and write in whatever you
        # want, as long as it's in single quotes
        classesComboBoxLabel = QLabel("Class:")
        self.classesComboBox = QComboBox()
        listOfClasses = ('Fighter', 'Ranger', 'Rogue', 'Mage', 'Cleric')
        self.classesComboBox.addItems(listOfClasses)
        # self.classesComboBox.activated.connect(self.handleActivated)

        # This sets up the elements box
        elementsComboBoxLabel = QLabel("Element:")
        self.elementsComboBox = QComboBox()
        listOfElements = ('Air', 'Earth', 'Water', 'Fire', 'Forest')
        self.elementsComboBox.addItems(listOfElements)
        # self.elementsComboBox.activated.connect(self.handleActivated)

        # This is a toggle modifier to increase the strength
        # of the monster and the loot it's carrying. It's
        # entirely optional and can be removed, or the strength
        # of the modifier can be changed in the "math" folder.
        bossCheckBoxLabel = QLabel("Boss:")
        self.bossCheckBox = QCheckBox()

        # These are the buttons for saving and generating new NPCs.

        self.generateButton = QPushButton("Generate")
        self.generateButton.clicked.connect(self.GenerateButtonPressed)
        self.saveButton = QPushButton("Save")

        bottomButtonsLayout = QHBoxLayout()
        bottomButtonsLayout.addStretch(1)
        bottomButtonsLayout.addWidget(self.generateButton)
        bottomButtonsLayout.addWidget(self.saveButton)

        # This builds the textbox that you see the resulting character in

        self.mainTextBox = QTextEdit()
        textBoxLayout = QHBoxLayout()
        textBoxLayout.addWidget(self.mainTextBox)

        # This creates the layout for the controls. Any new fields should
        # follow this same general convention.
        controls = QScrollArea()
        controls.setFixedHeight(100)
        controls.setWidgetResizable(False)
        controlsLayout = QHBoxLayout(controls)

        controls.setWidget(controlsLayout.widget())

        controlsLayout.addWidget(levelComboBoxLabel)
        controlsLayout.addWidget(self.levelComboBox)
        controlsLayout.addWidget(speciesComboBoxLabel)
        controlsLayout.addWidget(self.speciesComboBox)
        controlsLayout.addWidget(classesComboBoxLabel)
        controlsLayout.addWidget(self.classesComboBox)
        controlsLayout.addWidget(elementsComboBoxLabel)
        controlsLayout.addWidget(self.elementsComboBox)
        controlsLayout.addWidget(bossCheckBoxLabel)
        controlsLayout.addWidget(self.bossCheckBox)

        # Adds all of the disparate groups of controls to the total layout
        self.layout.addWidget(controls)
        self.layout.addLayout(textBoxLayout)
        self.layout.addLayout(bottomButtonsLayout)

    def GenerateButtonPressed(self):
        self.localLevelString = self.levelComboBox.currentText()
        self.speciesString = self.speciesComboBox.currentText()
        self.classesString = self.classesComboBox.currentText()
        self.elementsString = self.elementsComboBox.currentText()
        if self.bossCheckBox == Qt.Checked:
            self.bossString = "true"
        else:
            self.bossString = "false"
        resultString = charactergen.generateCharacter(self)
        self.mainTextBox.setPlainText(resultString)
