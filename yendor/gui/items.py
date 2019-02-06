#! /usr/bin/python3
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QComboBox,
                             QLabel, QPushButton, QTextEdit)

def tab():
    # Initializing the complete layout
    tab.layout = QVBoxLayout()

    # The list of items to choose from. Change the values in the listOfItems
    # list to get different results on the page.
    itemsComboBoxLabel = QLabel()
    itemsComboBoxLabel.setText("Places:")
    itemsComboBox = QComboBox()
    listOfItems = ('Light Weapon', 'One-Handed Weapon', 'Two-Handed Weapon',
                   'Ranged Weapon', 'Light Armor', 'Medium Armor',
                   'Heavy Armor', 'Shield', 'Jewelry', 'Potion',
                   'Gear', 'Specialty')
    itemsComboBox.addItems(listOfItems)

    # This sets up the buffs box
    buffsComboBoxLabel = QLabel()
    buffsComboBoxLabel.setText("Buffs:")
    buffsComboBox = QComboBox()
    listOfBuffs = ('None', 'Low', 'Medium', 'High', 'Legendary')
    buffsComboBox.addItems(listOfBuffs)

    # This sets up the debuffs box
    debuffsComboBoxLabel = QLabel()
    debuffsComboBoxLabel.setText("Debuffs:")
    debuffsComboBox = QComboBox()
    listOfDebuffs = ('None', 'Low', 'Medium', 'High', 'Cursed')
    debuffsComboBox.addItems(listOfDebuffs)

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
    controls.addWidget(itemsComboBoxLabel)
    controls.addWidget(itemsComboBox)
    controls.addWidget(buffsComboBoxLabel)
    controls.addWidget(buffsComboBox)
    controls.addWidget(debuffsComboBoxLabel)
    controls.addWidget(debuffsComboBox)

    # Adds all of the disparate groups of controls to the total layout
    tab.layout.addLayout(controls)
    tab.layout.addLayout(textBoxLayout)
    tab.layout.addLayout(bottomButtonsLayout)

    # sends the layout to core.py
    return tab.layout
