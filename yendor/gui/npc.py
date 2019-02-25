#! /usr/bin/python3

"""Create the npc tab in the UI"""

from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout,
                             QComboBox, QCheckBox, QLabel,
                             QPushButton, QTextEdit, QScrollArea)
from PyQt5.QtCore import Qt

from ..math import charactergen


class Tab:
    """Sets up the tab structure"""

    def __init__(self):
        self.tab()
        self.generate_button_pressed()

    def tab(self):
        """Sets up the tab contents"""
        # Initializing the complete layout
        self.layout = QVBoxLayout()

        # The list of species to choose from. Change the values
        # in the listOfSpecies list to get different results on the page.
        species_combo_box_label = QLabel("Species:")
        self.species_combo_box = QComboBox()
        list_of_species = ('Dragonborn', 'Dwarf', 'Eldarin', 'Elf',
                           'Halfling', 'Human', 'Tiefling', 'Goblin',
                           'Slime', 'Random Appropriate Monster')
        self.species_combo_box.addItems(list_of_species)

        # This sets up the level scaling for the resulting
        # character. The current cap is at 30, but the
        # algorithm should continue to function to any level.
        level_combo_box_label = QLabel("Level:")
        self.level_combo_box = QComboBox()
        for i in range(1, 31):
            self.level_combo_box.addItem(str(i))
            i += 1

        # This sets up the list of classes. Only four basic
        # classes are here now, but to add more, add a comma
        # after the last item and write in whatever you
        # want, as long as it's in single quotes
        classes_combo_box_label = QLabel("Class:")
        self.classes_combo_box = QComboBox()
        list_of_classes = ('Fighter', 'Ranger', 'Rogue', 'Mage', 'Cleric')
        self.classes_combo_box.addItems(list_of_classes)

        # This sets up the elements box
        elements_combo_box_label = QLabel("Element:")
        self.elements_combo_box = QComboBox()
        list_of_elements = ('Air', 'Earth', 'Water', 'Fire', 'Forest')
        self.elements_combo_box.addItems(list_of_elements)

        # This is a toggle modifier to increase the strength
        # of the monster and the loot it's carrying. It's
        # entirely optional and can be removed, or the strength
        # of the modifier can be changed in the "math" folder.
        boss_check_box_label = QLabel("Boss:")
        self.boss_check_box = QCheckBox()

        # These are the buttons for saving and generating new NPCs.

        self.generate_button = QPushButton("Generate")
        self.generate_button.clicked.connect(self.generate_button_pressed)
        self.save_button = QPushButton("Save")

        bottom_buttons_layout = QHBoxLayout()
        bottom_buttons_layout.addStretch(1)
        bottom_buttons_layout.addWidget(self.generate_button)
        bottom_buttons_layout.addWidget(self.save_button)

        # This builds the textbox that you see the resulting character in

        self.main_text_box = QTextEdit()
        text_box_layout = QHBoxLayout()
        text_box_layout.addWidget(self.main_text_box)

        # This creates the layout for the controls. Any new fields should
        # follow this same general convention.
        controls = QScrollArea()
        controls.setFixedHeight(100)
        controls.setWidgetResizable(False)
        controls_layout = QHBoxLayout(controls)

        controls.setWidget(controls_layout.widget())

        controls_layout.addWidget(level_combo_box_label)
        controls_layout.addWidget(self.level_combo_box)
        controls_layout.addWidget(species_combo_box_label)
        controls_layout.addWidget(self.species_combo_box)
        controls_layout.addWidget(classes_combo_box_label)
        controls_layout.addWidget(self.classes_combo_box)
        controls_layout.addWidget(elements_combo_box_label)
        controls_layout.addWidget(self.elements_combo_box)
        controls_layout.addWidget(boss_check_box_label)
        controls_layout.addWidget(self.boss_check_box)

        # Adds all of the disparate groups of controls to the total layout
        self.layout.addWidget(controls)
        self.layout.addLayout(text_box_layout)
        self.layout.addLayout(bottom_buttons_layout)

    def generate_button_pressed(self):
        """send variables to the charactergen.py"""
        self.local_level_string = self.level_combo_box.currentText()
        self.species_string = self.species_combo_box.currentText()
        self.classes_string = self.classes_combo_box.currentText()
        self.elements_string = self.elements_combo_box.currentText()
        if self.boss_check_box == Qt.Checked:
            self.boss_string = "true"
        else:
            self.boss_string = "false"
        result_string = charactergen.generate_character(self)
        self.main_text_box.setPlainText(result_string)
