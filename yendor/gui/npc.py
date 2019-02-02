from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QComboBox, QCheckBox, QLabel)
def tab():
    tab.layout = QVBoxLayout()

    speciesComboBoxLabel = QLabel()
    speciesComboBoxLabel.setText("Species: ")
    speciesComboBox = QComboBox()
    listOfSpecies = ('Dragonborn', 'Dwarf', 'Eldarin', 'Elf',
                     'Halfling', 'Human', 'Tiefling', 'Goblin')
    speciesComboBox.addItems(listOfSpecies)

    levelComboBoxLabel = QLabel()
    levelComboBoxLabel.setText("Level: ")
    levelComboBox = QComboBox()
    for i in range(1, 31):
        levelComboBox.addItem(str(i))
        i += 1

    classesComboBoxLabel = QLabel()
    classesComboBoxLabel.setText("Class: ")
    classesComboBox = QComboBox()
    listOfClasses = ('Fighter', 'Rogue', 'Mage', 'Cleric')
    classesComboBox.addItems(listOfClasses)

    elderCheckBoxLabel = QLabel()
    elderCheckBoxLabel.setText("Elder: ")
    elderCheckBox = QCheckBox()

    controls = QHBoxLayout()

    # adding widgets to layout
    controls.addWidget(levelComboBoxLabel)
    controls.addWidget(levelComboBox)
    controls.addWidget(speciesComboBoxLabel)
    controls.addWidget(speciesComboBox)
    controls.addWidget(classesComboBoxLabel)
    controls.addWidget(classesComboBox)
    controls.addWidget(elderCheckBoxLabel)
    controls.addWidget(elderCheckBox)

    tab.layout.addLayout(controls)

    return tab.layout
