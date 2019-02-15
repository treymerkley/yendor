#! /usr/bin/python3
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QComboBox,
                             QLabel, QPushButton, QTextEdit,
                             QScrollArea)
class Tab:

    def __init__(self):
        self.tab()

    def tab(self):
        # Initializing the complete layout
        self.layout = QVBoxLayout()
        
        # The list of items to choose from. Change the values in the listOfItems
        # list to get different results on the page.
        itemsComboBoxLabel = QLabel()
        itemsComboBoxLabel.setText("Places:")
        self.itemsComboBox = QComboBox()
        listOfItems = ('Light Weapon', 'One-Handed Weapon', 'Two-Handed Weapon',
                       'Ranged Weapon', 'Light Armor', 'Medium Armor',
                       'Heavy Armor', 'Shield', 'Jewelry', 'Potion',
                       'Gear', 'Specialty')
        self.itemsComboBox.addItems(listOfItems)

        # This sets up the buffs box
        buffsComboBoxLabel = QLabel()
        buffsComboBoxLabel.setText("Buffs:")
        self.buffsComboBox = QComboBox()
        listOfBuffs = ('None', 'Low', 'Medium', 'High', 'Legendary')
        self.buffsComboBox.addItems(listOfBuffs)

        # This sets up the debuffs box
        debuffsComboBoxLabel = QLabel()
        debuffsComboBoxLabel.setText("Debuffs:")
        self.debuffsComboBox = QComboBox()
        listOfDebuffs = ('None', 'Low', 'Medium', 'High', 'Cursed')
        self.debuffsComboBox.addItems(listOfDebuffs)

        # These are the buttons for saving and generating new NPCs.
        self.generateButton = QPushButton("Generate")
        self.saveButton = QPushButton("Save")

        bottomButtonsLayout = QHBoxLayout()
        bottomButtonsLayout.addStretch(1)
        bottomButtonsLayout.addWidget(self.generateButton)
        bottomButtonsLayout.addWidget(self.saveButton)

        # This builds the textbox that you see the resulting item in
        mainTextBox = QTextEdit()
        textBoxLayout = QHBoxLayout()
        textBoxLayout.addWidget(mainTextBox)

        # This creates the layout for the controls. Any new fields should
        # follow this same general convention.
        controls = QScrollArea()
        controls.setFixedHeight(100)
        controls.setWidgetResizable(False)
        controlsLayout = QHBoxLayout(controls)

        controls.setWidget(controlsLayout.widget())

        controlsLayout.addWidget(itemsComboBoxLabel)
        controlsLayout.addWidget(self.itemsComboBox)
        controlsLayout.addWidget(buffsComboBoxLabel)
        controlsLayout.addWidget(self.buffsComboBox)
        controlsLayout.addWidget(debuffsComboBoxLabel)
        controlsLayout.addWidget(self.debuffsComboBox)

        # Adds all of the disparate groups of controls to the total layout
        self.layout.addWidget(controls)
        self.layout.addLayout(textBoxLayout)
        self.layout.addLayout(bottomButtonsLayout)

