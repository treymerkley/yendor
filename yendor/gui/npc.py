#! /usr/bin/python3
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout,
                             QComboBox, QCheckBox, QLabel,
                             QPushButton, QTextEdit)

def tab():
    # Initializing the complete layout
    tab.layout = QVBoxLayout()

    # The list of species to choose from. Change the values in the listOfSpecies
    # list to get different results on the page.
    speciesComboBoxLabel = QLabel()
    speciesComboBoxLabel.setText("Species:")
    speciesComboBox = QComboBox()
    listOfSpecies = ('Dragonborn', 'Dwarf', 'Eldarin', 'Elf',
                     'Halfling', 'Human', 'Tiefling', 'Goblin')
    speciesComboBox.addItems(listOfSpecies)

    # This sets up the level scaling for the resulting character. The current
    # cap is at 30, but the algorithm should continue to function to any level.
    levelComboBoxLabel = QLabel()
    levelComboBoxLabel.setText("Level:")
    levelComboBox = QComboBox()
    for i in range(1, 31):
        levelComboBox.addItem(str(i))
        i += 1

    # This sets up the list of classes. Only four basic classes are here now,
    # but to add more, add a comma after the last item and write in whatever you
    # want, as long as it's in single quotes
    classesComboBoxLabel = QLabel()
    classesComboBoxLabel.setText("Class:")
    classesComboBox = QComboBox()
    listOfClasses = ('Fighter', 'Ranger', 'Rogue', 'Mage', 'Cleric')
    classesComboBox.addItems(listOfClasses)

    # This sets up the elements box
    elementsComboBoxLabel = QLabel()
    elementsComboBoxLabel.setText("Element:")
    elementsComboBox = QComboBox()
    listOfElements = ('Air', 'Earth', 'Water', 'Fire', 'Forest')
    elementsComboBox.addItems(listOfElements)

    # This is a toggle modifier to increase the strength of the monster and the
    # loot it's carrying. It's entirely optional and can be removed, or the
    # strength of the modifier can be changed in the "math" folder.
    bossCheckBoxLabel = QLabel()
    bossCheckBoxLabel.setText("Boss:")
    bossCheckBox = QCheckBox()

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

    # This creates the layout for the controls. Any new fields should
    # follow this same general convention.
    controls = QHBoxLayout()
    controls.addWidget(levelComboBoxLabel)
    controls.addWidget(levelComboBox)
    controls.addWidget(speciesComboBoxLabel)
    controls.addWidget(speciesComboBox)
    controls.addWidget(classesComboBoxLabel)
    controls.addWidget(classesComboBox)
    controls.addWidget(elementsComboBoxLabel)
    controls.addWidget(elementsComboBox)
    controls.addWidget(bossCheckBoxLabel)
    controls.addWidget(bossCheckBox)

    # Adds all of the disparate groups of controls to the total layout
    tab.layout.addLayout(controls)
    tab.layout.addLayout(textBoxLayout)
    tab.layout.addLayout(bottomButtonsLayout)

    # sends the layout to core.py
    return tab.layout
