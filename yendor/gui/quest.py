#! /usr/bin/python3
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QComboBox,
                             QLabel, QPushButton, QTextEdit,
                             QScrollArea)

def tab():
    # Initializing the complete layout
    tab.layout = QVBoxLayout()

    # The list of plots to choose from. Change the values in the listOfPlot
    # list to get different results on the page.
    plotComboBoxLabel = QLabel()
    plotComboBoxLabel.setText("Basic Plot:")
    plotComboBox = QComboBox()
    listOfPlot = ('Go kill a monster', 'Go kill a noble', 'Go kill a god',
                  'Bad hombres moved in', 'Bad hombres at the top',
                  'Escort quest', 'Go get a thing', 'Go get some cash',
                  'Go investigate the spoopy place',
                  'Go investigate the ostensibly normal place')
    plotComboBox.addItems(listOfPlot)

    # This sets up the level scaling for the resulting character. The current
    # cap is at 30, but the algorithm should continue to function to any level.
    levelComboBoxLabel = QLabel()
    levelComboBoxLabel.setText("Level:")
    levelComboBox = QComboBox()
    for i in range(1, 31):
        levelComboBox.addItem(str(i))
        i += 1

    # These are the buttons for saving and generating new quests.
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
    controlsLayout.addWidget(levelComboBoxLabel)
    controlsLayout.addWidget(levelComboBox)
    controlsLayout.addWidget(plotComboBoxLabel)
    controlsLayout.addWidget(plotComboBox)

    # Adds all of the disparate groups of controls to the total layout
    tab.layout.addWidget(controls)
    tab.layout.addLayout(textBoxLayout)
    tab.layout.addLayout(bottomButtonsLayout)

    # sends the layout to core.py
    return tab.layout
