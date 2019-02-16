#! /usr/bin/python3
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout,
                             QComboBox, QCheckBox, QLabel,
                             QPushButton, QTextEdit, QScrollArea,
                             QLineEdit)

from ..math import charactergen

class Tab:

    def __init__(self):
        self.tab()

    def tab(self):
        # Initializing the complete layout
        self.layout = QVBoxLayout()

        nameLineEditLabel = QLabel("Name:")
        self.nameLineEdit = QLineEdit()

        # This sets up the level scaling for
        # the resulting character. The current
        # cap is at 30, but the algorithm should
        # continue to function to any level.
        levelComboBoxLabel = QLabel("Level:")
        self.levelComboBox = QComboBox()
        for i in range(1, 31):
            self.levelComboBox.addItem(str(i))
            i += 1

        # This sets up the elements box
        sizeComboBoxLabel = QLabel("Size:")
        self.sizeComboBox = QComboBox()
        listOfSizes = ('Fine', 'Diminutive', 'Tiny', 'Small',
                       'Medium', 'Large', 'Huge', 'Gargantuan',
                       'Colossal')
        self.sizeComboBox.addItems(listOfSizes)

        # This sets up the elements box
        skillsComboBoxLabel = QLabel("Skills:")
        self.skillsComboBox = QComboBox()
        listOfSkills = ('Babble', 'Blindsense', 'Blindsight', 'Breath Weapon',
                        'Constrict', 'Create Spawn', 'Damage Reduction',
                        'Darkvision', 'Enslave', 'Etherealness',
                        'Fast Healing', 'Firey Aura', 'Flight',
                        'Improved Grab', 'Incorporeality', 'Invisibility',
                        'Leader', 'Low-Light Vision', 'Earth Mastery',
                        'Water Mastery', 'Fire Mastery', 'Air Mastery',
                        'Mindless', 'Natural Cunning', 'Pounce',
                        'Powerful Charge', 'Push', 'Rake', 'Regeneration',
                        'Scent', 'Snatch', 'Stonecunning', 'Swallow Whole',
                        'Torment', 'Trample', 'Tremorsense')
        self.skillsComboBox.addItems(listOfSkills)

        # This is a toggle modifier to increasethe strength
        # of the monster and the loot it's carrying. It's
        # entirely optional and can be removed, or the
        # strength of the modifier can be changed in the "math" folder.
        bossCheckBoxLabel = QLabel("Boss:")
        self.bossCheckBox = QCheckBox()

        # These are the buttons for saving and generating new NPCs.
        self.saveButton = QPushButton("Save")
        bottomButtonsLayout = QHBoxLayout()
        bottomButtonsLayout.addStretch(1)
        bottomButtonsLayout.addWidget(self.saveButton)

        # This builds the textbox that you see the resulting character in
        mainTextBox = QTextEdit()
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
        controlsLayout.addWidget(self.levelComboBox)
        controlsLayout.addWidget(nameLineEditLabel)
        controlsLayout.addWidget(self.nameLineEdit)
        controlsLayout.addWidget(skillsComboBoxLabel)
        controlsLayout.addWidget(self.skillsComboBox)
        controlsLayout.addWidget(sizeComboBoxLabel)
        controlsLayout.addWidget(self.sizeComboBox)
        controlsLayout.addWidget(bossCheckBoxLabel)
        controlsLayout.addWidget(self.bossCheckBox)

        # Adds all of the disparate groups of controls to the total layout
        self.layout.addWidget(controls)
        self.layout.addLayout(textBoxLayout)
        self.layout.addLayout(bottomButtonsLayout)
