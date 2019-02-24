#! /usr/bin/python3

"""Create the items tab in the UI"""

from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QComboBox,
                             QLabel, QPushButton, QTextEdit,
                             QScrollArea)
class Tab:
    """Sets up the tab structure"""

    def __init__(self):
        self.tab()

    def tab(self):
        """Sets up the tab contents"""
        # Initializing the complete layout
        self.layout = QVBoxLayout()

        # The list of items to choose from.
        # Change the values in the list_of_items
        # list to get different results on the page.
        items_combo_box_label = QLabel("Places:")
        self.items_combo_box = QComboBox()
        list_of_items = ('Light Weapon', 'One-Handed Weapon',
                         'Two-Handed Weapon', 'Ranged Weapon',
                         'Light Armor', 'Medium Armor',
                         'Heavy Armor', 'Shield', 'Jewelry',
                         'Potion', 'Gear', 'Specialty')
        self.items_combo_box.addItems(list_of_items)

        # This sets up the buffs box
        buffs_combo_box_label = QLabel("Buffs:")
        self.buffs_combo_box = QComboBox()
        list_of_buffs = ('None', 'Low', 'Medium', 'High', 'Legendary')
        self.buffs_combo_box.addItems(list_of_buffs)

        # This sets up the debuffs box
        debuffs_combo_box_label = QLabel("Debuffs:")
        self.debuffs_combo_box = QComboBox()
        list_of_debuffs = ('None', 'Low', 'Medium', 'High', 'Cursed')
        self.debuffs_combo_box.addItems(list_of_debuffs)

        # These are the buttons for saving and generating new NPCs.
        self.generate_button = QPushButton("Generate")
        self.save_button = QPushButton("Save")

        bottom_buttons_layout = QHBoxLayout()
        bottom_buttons_layout.addStretch(1)
        bottom_buttons_layout.addWidget(self.generate_button)
        bottom_buttons_layout.addWidget(self.save_button)

        # This builds the textbox that you see the resulting item in
        main_text_box = QTextEdit()
        text_box_layout = QHBoxLayout()
        text_box_layout.addWidget(main_text_box)

        # This creates the layout for the controls. Any new fields should
        # follow this same general convention.
        controls = QScrollArea()
        controls.setFixedHeight(100)
        controls.setWidgetResizable(False)
        controls_layout = QHBoxLayout(controls)

        controls.setWidget(controls_layout.widget())

        controls_layout.addWidget(items_combo_box_label)
        controls_layout.addWidget(self.items_combo_box)
        controls_layout.addWidget(buffs_combo_box_label)
        controls_layout.addWidget(self.buffs_combo_box)
        controls_layout.addWidget(debuffs_combo_box_label)
        controls_layout.addWidget(self.debuffs_combo_box)

        # Adds all of the disparate groups of controls to the total layout
        self.layout.addWidget(controls)
        self.layout.addLayout(text_box_layout)
        self.layout.addLayout(bottom_buttons_layout)
