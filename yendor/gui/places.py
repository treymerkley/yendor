
#! /usr/bin/python3
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QComboBox,
                             QLabel, QPushButton, QTextEdit,
                             QCheckBox, QScrollArea)
class Tab:

    def __init__(self):
        self.tab()

    def tab(self):
        # Initializing the complete layout
        self.layout = QVBoxLayout()

        # The list of species to choose from.
        # Change the values in the listOfSpecies
        # list to get different results on the page.
        placesComboBoxLabel = QLabel("Places:")
        self.placesComboBox = QComboBox()
        listOfPlaces = ('Village', 'City', 'Cave',
                        'Ruins')
        self.placesComboBox.addItems(listOfPlaces)

        # This sets up the elements box
        elementsComboBoxLabel = QLabel("Element:")
        self.elementsComboBox = QComboBox()
        listOfElements = ('Plains', 'Mountain',
                          'Wetland', 'Volcano', 'Forest')
        self.elementsComboBox.addItems(listOfElements)

        # Toggle for hostile area
        hostileCheckBoxLabel = QLabel("Hostile:")
        self.hostileCheckBox = QCheckBox()

        # These are the buttons for saving and generating new NPCs.
        self.generateButton = QPushButton("Generate")
        self.saveButton = QPushButton("Save")
        bottomButtonsLayout = QHBoxLayout()
        bottomButtonsLayout.addStretch(1)
        bottomButtonsLayout.addWidget(self.generateButton)
        bottomButtonsLayout.addWidget(self.saveButton)

        # This builds the textbox that you see the resulting character in
        self.mainTextBox = QTextEdit()
        textBoxLayout = QHBoxLayout()
        textBoxLayout.addWidget(self.mainTextBox)

        controls = QScrollArea()
        controls.setFixedHeight(100)
        controls.setWidgetResizable(False)
        controlsLayout = QHBoxLayout(controls)

        # This creates the layout for the controls. Any new fields should
        # follow this same general convention.
        controls.setWidget(controlsLayout.widget())
        controlsLayout.addWidget(placesComboBoxLabel)
        controlsLayout.addWidget(self.placesComboBox)
        controlsLayout.addWidget(elementsComboBoxLabel)
        controlsLayout.addWidget(self.elementsComboBox)
        controlsLayout.addWidget(hostileCheckBoxLabel)
        controlsLayout.addWidget(self.hostileCheckBox)

        # Adds all of the disparate groups of controls to the total layout
        self.layout.addWidget(controls)
        self.layout.addLayout(textBoxLayout)
        self.layout.addLayout(bottomButtonsLayout)
