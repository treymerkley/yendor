#! /usr/bin/python3
"""Sets up the monster builder page"""
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout,
                             QComboBox, QCheckBox, QLabel,
                             QPushButton, QTextEdit, QScrollArea,
                             QLineEdit)

# from ..math import charactergen


class Tab:

    "Tab class"

    def __init__(self):
        self.tab()

    def tab(self):
        """sets up the actual tab layout"""
        # Initializing the complete layout
        self.layout = QVBoxLayout()

        name_line_edit_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        # This sets up the level scaling for
        # the resulting character. The current
        # cap is at 30, but the algorithm should
        # continue to function to any level.
        level_combo_box_label = QLabel("Level:")
        self.level_combo_box = QComboBox()
        for i in range(1, 31):
            self.level_combo_box.addItem(str(i))
            i += 1

        # This sets up the elements box
        size_combo_box_label = QLabel("Size:")
        self.size_combo_box = QComboBox()
        list_of_sizes = ('Fine', 'Diminutive', 'Tiny', 'Small',
                         'Medium', 'Large', 'Huge', 'Gargantuan',
                         'Colossal')
        self.size_combo_box.addItems(list_of_sizes)

        # This sets up the elements box
        skills_combo_box_label = QLabel("Skills:")
        self.skills_combo_box = QComboBox()
        list_of_skills = ('Babble', 'Blindsense', 'Blindsight', 'Breath Weapon',
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
        self.skills_combo_box.addItems(list_of_skills)

        # This is a toggle modifier to increasethe strength
        # of the monster and the loot it's carrying. It's
        # entirely optional and can be removed, or the
        # strength of the modifier can be changed in the "math" folder.
        boss_check_box_label = QLabel("Boss:")
        self.boss_check_box = QCheckBox()

        # These are the buttons for saving and generating new NPCs.
        self.save_button = QPushButton("Save")
        bottom_buttons_layout = QHBoxLayout()
        bottom_buttons_layout.addStretch(1)
        bottom_buttons_layout.addWidget(self.save_button)

        # This builds the textbox that you see the resulting character in
        main_text_box = QTextEdit()
        text_box_layout = QHBoxLayout()
        text_box_label = QLabel("Description: ")
        text_box_layout.addWidget(text_box_label)
        text_box_layout.addWidget(main_text_box)

        # This creates the layout for the controls. Any new fields should
        # follow this same general convention.
        controls = QScrollArea()
        controls.setFixedHeight(100)
        controls.setWidgetResizable(False)
        controls_layout = QHBoxLayout(controls)

        controls.setWidget(controls_layout.widget())

        controls_layout.addWidget(level_combo_box_label)
        controls_layout.addWidget(self.level_combo_box)
        controls_layout.addWidget(name_line_edit_label)
        controls_layout.addWidget(self.name_line_edit)
        controls_layout.addWidget(skills_combo_box_label)
        controls_layout.addWidget(self.skills_combo_box)
        controls_layout.addWidget(size_combo_box_label)
        controls_layout.addWidget(self.size_combo_box)
        controls_layout.addWidget(boss_check_box_label)
        controls_layout.addWidget(self.boss_check_box)

        # Adds all of the disparate groups of controls to the total layout
        self.layout.addWidget(controls)
        self.layout.addLayout(text_box_layout)
        self.layout.addLayout(bottom_buttons_layout)
