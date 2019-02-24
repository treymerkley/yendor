#! /usr/bin/python3
import random

# Choctaw names from https://mike-boucher.com/wordpress/?page_id=201
list_of_names = ('Kana', 'Chukma', 'Chito', 'Achukma', 'Allunsi', 'Yukpa',
                 'Nita', 'Haloka', 'Amona', 'Hatak', 'Malata', 'Nana Moma',
                 'Ishi', 'Kana', 'Minko', 'Chulosa', 'Samanta', 'Alla',
                 'Okla', 'Talako', 'Onssi', 'Humma', 'Chito', 'Isi', 'Opia',
                 'Ohoyo', 'Kostina', 'Kostini', 'Banna', 'Anli', 'Palli',
                 'Hishi', 'Shikopa', 'Ahpi', 'Onafa', 'Duquesne', 'Draconis',
                 'Zippideedoo', 'Marrrrrr', 'Hector', 'Bing Bong', 'Lavernica',
                 'Brutalitops', 'Malkavian')

list_of_titles = ('Well-Endowed', 'Champion', 'Great', 'Lazy', 'Brutal',
                  'Monser Slayer', 'Redundant', 'Spare', 'Hero', 'Guy',
                  'Archer', 'Brave', 'Coward', 'Holy', 'Shady', 'Mystic',
                  '...Something', 'Dustroyer')

def generateCharacter(self):
    character_name = (random.choice(list_of_names) +
                      ' the ' + random.choice(list_of_titles))
    level = self.localLevelString
    
    myString = str('Name: ' + character_name + '\n' +
                   'Level: ' + level + '\n')
    return myString
