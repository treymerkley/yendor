#! /usr/bin/python3
"""Sets up the quest tab"""
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QComboBox,
                             QLabel, QPushButton, QTextEdit,
                             QScrollArea)


class Tab:

    """Tab class"""

    def __init__(self):
        self.tab()

    def tab(self):
        """actual tab layout"""
        # Initializing the complete layout
        self.layout = QVBoxLayout()

        # The list of plots to choose from. Change the values in the listOfPlot
        # list to get different results on the page.
        plot_combo_box_label = QLabel("Basic Plot:")
        self.plot_combo_box = QComboBox()
        list_of_plot = ('Go kill a monster', 'Go kill a noble', 'Go kill a god',
                        'Bad hombres moved in', 'Bad hombres at the top',
                        'Escort quest', 'Go get a thing', 'Go get some cash',
                        'Go investigate the spoopy place',
                        'Go investigate the ostensibly normal place')
        self.plot_combo_box.addItems(list_of_plot)

        # This sets up the level scaling for the
        # resulting character. The current cap is at 30,
        # but the algorithm should continue to function to any level.
        level_combo_box_label = QLabel("Level:")
        self.level_combo_box = QComboBox()
        for i in range(1, 31):
            self.level_combo_box.addItem(str(i))
            i += 1

        # These are the buttons for saving and generating new quests.
        self.generate_button = QPushButton("Generate")
        self.save_button = QPushButton("Save")
        bottom_buttons_layout = QHBoxLayout()
        bottom_buttons_layout.addStretch(1)
        bottom_buttons_layout.addWidget(self.generate_button)
        bottom_buttons_layout.addWidget(self.save_button)

        # This builds the textbox that you see the resulting character in
        self.main_text_box = QTextEdit()
        text_box_layout = QHBoxLayout()
        text_box_layout.addWidget(self.main_text_box)

        controls = QScrollArea()
        controls.setFixedHeight(100)
        controls.setWidgetResizable(False)
        controls_layout = QHBoxLayout(controls)

        # This creates the layout for the controls. Any new fields should
        # follow this same general convention.
        controls.setWidget(controls_layout.widget())
        controls_layout.addWidget(level_combo_box_label)
        controls_layout.addWidget(self.level_combo_box)
        controls_layout.addWidget(plot_combo_box_label)
        controls_layout.addWidget(self.plot_combo_box)

        # Adds all of the disparate groups of controls to the total layout
        self.layout.addWidget(controls)
        self.layout.addLayout(text_box_layout)
        self.layout.addLayout(bottom_buttons_layout)
