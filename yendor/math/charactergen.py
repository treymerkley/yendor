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

    my_string = str('Name: ' + character_name + '\n' +
                    'Level: ' + level + '\n')
    return my_string
