from PyQt5.QtWidgets import (QHBoxLayout, QComboBox, QCheckBox, QLabel)
def tab():
    tab.layout = QHBoxLayout()

    speciesComboBoxLabel = QLabel()
    speciesComboBoxLabel.setText("Species")
    speciesComboBox = QComboBox()
    listOfSpecies = ('Dragonborn', 'Dwarf', 'Eldarin', 'Elf',
                     'Halfling', 'Human', 'Tiefling', 'Goblin')
    speciesComboBox.addItems(listOfSpecies)

    levelComboBoxLabel = QLabel()
    levelComboBoxLabel.setText("Level")
    levelComboBox = QComboBox()
    for i in range(1, 31):
        levelComboBox.addItem(str(i))
        i += 1

    classesComboBoxLabel = QLabel()
    classesComboBoxLabel.setText("Class")
    classesComboBox = QComboBox()
    listOfClasses = ('Fighter', 'Rogue', 'Mage', 'Cleric')
    classesComboBox.addItems(listOfClasses)
    
    elderCheckBoxLabel = QLabel()
    elderCheckBoxLabel.setText("Elder")
    elderCheckBox = QCheckBox()

    # adding widgets to layout
    tab.layout.addWidget(levelComboBoxLabel)
    tab.layout.addWidget(levelComboBox)
    tab.layout.addWidget(speciesComboBoxLabel)
    tab.layout.addWidget(speciesComboBox)
    tab.layout.addWidget(classesComboBoxLabel)
    tab.layout.addWidget(classesComboBox)
    tab.layout.addWidget(elderCheckBoxLabel)
    tab.layout.addWidget(elderCheckBox)
