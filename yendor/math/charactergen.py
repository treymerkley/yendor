#! /usr/bin/python3
"""generates character as per npc.py"""
import random

# Choctaw names from https://mike-boucher.com/wordpress/?page_id=201
LIST_OF_NAMES = ('Kana', 'Chukma', 'Chito', 'Achukma', 'Allunsi', 'Yukpa',
                 'Nita', 'Haloka', 'Amona', 'Hatak', 'Malata', 'Nana Moma',
                 'Ishi', 'Kana', 'Minko', 'Chulosa', 'Samanta', 'Alla',
                 'Okla', 'Talako', 'Onssi', 'Humma', 'Chito', 'Isi', 'Opia',
                 'Ohoyo', 'Kostina', 'Kostini', 'Banna', 'Anli', 'Palli',
                 'Hishi', 'Shikopa', 'Ahpi', 'Onafa', 'Duquesne', 'Draconis',
                 'Zippideedoo', 'Marrrrrr', 'Hector', 'Bing Bong', 'Lavernica',
                 'Brutalitops', 'Malkavian')

LIST_OF_TITLES = ('Well-Endowed', 'Champion', 'Great', 'Lazy', 'Brutal',
                  'Monser Slayer', 'Redundant', 'Spare', 'Hero', 'Guy',
                  'Archer', 'Brave', 'Coward', 'Holy', 'Shady', 'Mystic',
                  '...Something', 'Dustroyer')


def generate_character(self):
    """does the actual generation"""
    character_name = (random.choice(LIST_OF_NAMES) +
                      ' the ' + random.choice(LIST_OF_TITLES))
    level = self.local_level_string
    abilities = {'strength': 0, 'constitution': 0, 'dexterity': 0,
                 'intelligence': 0, 'wisdom': 0, 'charisma': 0}
    abilities['strength'] = random.randint(3, 18)
    abilities['constitution'] = random.randint(3, 18)
    abilities['dexterity'] = random.randint(3, 18)
    abilities['intelligence'] = random.randint(3, 18)
    abilities['wisdom'] = random.randint(3, 18)
    abilities['charisma'] = random.randint(3, 18)
    int_level = int(level)
    bonus_multiplier = int_level // 4
    if bonus_multiplier == 0:
        bonus_multiplier += 1
    random_count = bonus_multiplier * 2
    while random_count != 0:
        random_ability = random.choice(
            list(abilities.values()))
        random_ability += 1
        random_count -= 1

    mod_strength = (abilities['strength'] * bonus_multiplier - 10) // 2
    mod_constitution = ((abilities['constitution'] * bonus_multiplier - 10)) // 2
    mod_dexterity = (abilities['dexterity'] * bonus_multiplier - 10) // 2
    mod_intelligence = (abilities['intelligence'] * bonus_multiplier - 10) // 2
    mod_wisdom = (abilities['wisdom'] * bonus_multiplier - 10) // 2
    mod_charisma = (abilities['charisma'] * bonus_multiplier - 10) // 2

    species = self.species_string
    classes = self.classes_string
    element = self.elements_string
    base_armor_class = 10 + mod_dexterity
    hit_points = (15 + mod_constitution)
    # until a table of species to hit points is made
    initiative = random.randint(1, 20)
    # spell_resistance = 'foo'
    # damage_resistance = 'bar'
    # difficulty_class = 'spam'

    my_string = str(
        character_name + ', ' +
        'A level ' + ' ' + str(level) +
        ' ' + element + ' ' + str(species) +
        ' ' + classes + '\n' + '\n' +
        'Base Armor Class: ' + str(base_armor_class) + '\n' +
        'Hit Points: ' + str(hit_points) + '\n' +
        'Initiative: ' + str(initiative) + '\n'
    )
    return my_string
