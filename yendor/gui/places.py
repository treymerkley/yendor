#! /usr/bin/python3
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QComboBox,
                             QLabel, QPushButton, QTextEdit,
                             QCheckBox, QScrollArea)

def tab():
    # Initializing the complete layout
    tab.layout = QVBoxLayout()

    # The list of species to choose from. Change the values in the listOfSpecies
    # list to get different results on the page.
    placesComboBoxLabel = QLabel()
    placesComboBoxLabel.setText("Places:")
    placesComboBox = QComboBox()
    listOfPlaces = ('Village', 'City', 'Cave',
                    'Ruins')
    placesComboBox.addItems(listOfPlaces)

    # This sets up the elements box
    elementsComboBoxLabel = QLabel()
    elementsComboBoxLabel.setText("Element:")
    elementsComboBox = QComboBox()
    listOfElements = ('Plains', 'Mountain', 'Wetland', 'Volcano', 'Forest')
    elementsComboBox.addItems(listOfElements)

    # Toggle for hostile area
    hostileCheckBoxLabel = QLabel()
    hostileCheckBoxLabel.setText("Hostile:")
    hostileCheckBox = QCheckBox()

    # These are the buttons for saving and generating new NPCs.
    generateButton = QPushButton("Generate")
    saveButton = QPushButton("Save")

    bottomButtonsLayout = QHBoxLayout()
    bottomButtonsLayout.addStretch(1)
    bottomButtonsLayout.addWidget(generateButton)
    bottomButtonsLayout.addWidget(saveButton)

    # This builds the textbox that you see the resulting character in
    mainTextBox = QTextEdit()
    textBoxLayout = QHBoxLayout()
    textBoxLayout.addWidget(mainTextBox)

    controls = QScrollArea()
    controls.setFixedHeight(100)
    controls.setWidgetResizable(False)
    controlsLayout = QHBoxLayout(controls)

    # This creates the layout for the controls. Any new fields should
    # follow this same general convention.
    controls.setWidget(controlsLayout.widget())
    controlsLayout.addWidget(placesComboBoxLabel)
    controlsLayout.addWidget(placesComboBox)
    controlsLayout.addWidget(elementsComboBoxLabel)
    controlsLayout.addWidget(elementsComboBox)
    controlsLayout.addWidget(hostileCheckBoxLabel)
    controlsLayout.addWidget(hostileCheckBox)

    # Adds all of the disparate groups of controls to the total layout
    tab.layout.addWidget(controls)
    tab.layout.addLayout(textBoxLayout)
    tab.layout.addLayout(bottomButtonsLayout)

    # sends the layout to core.py
    return tab.layout
