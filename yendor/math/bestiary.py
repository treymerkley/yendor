"""Primary combat beastiary"""
BEASTIARY = {
    "Aboleth": {
        'AC': '16',
        'HD': '8d8+40',
        'HP': '76',
        'Init': '+1',
        'Details': """4 tentacles +12 (1d6+9 and transformation);
        transformation, psionics, enslave; mucus cloud"""
    },
    "Achaierai": {
        'AC': '20',
        'HD': '6d8+12',
        'HP': '39',
        'Init': '+1',
        'Details': """2 claws +9 (2d6+4), bite +4 (4d6+2);
        black cloud; SR 19"""
    },
    "Allip": {
        'AC': '15',
        'HD': '4d12',
        'HP': '26',
        'Init': '+5',
        'Details': """incorporeal touch +3 (1d4 perm. MIND);
        babble, madness; undead, incorporeal, +2 turn resistance"""
    },
    "Ani. Object, Small": {
        'AC': '14',
        'HD': '1d10',
        'HP': '5',
        'Init': '+1',
        'Details': """slam +1 (1d4); construct, hardness, etc."""
    },
    "Ani. Object, Medium": {
        'AC': '14',
        'HD': '2d10',
        'HP': '11',
        'Init': '0',
        'Details': """slam +2 (1d6+1); construct, hardness, etc."""
    },
    "Ani. Object, Large": {
        'AC': '14',
        'HD': '4d10',
        'HP': '22',
        'Init': '0',
        'Details': """slam +5 (1d8+4); construct, hardness, etc."""
    },
    "Ani. Object, Huge": {
        'AC': '13',
        'HD': '8d10',
        'HP': '44',
        'Init': '-1',
        'Details': """slam +9 (2d6+7); construct, hardness, etc."""
    },
    "Ani. Object, Gargantuan": {
        'AC': '12',
        'HD': '16d10',
        'HP': '88',
        'Init': '-2',
        'Details': """slam +15 (2d8+10); construct, hardness, etc."""
    },
    "Ani. Object, Colossal": {
        'AC': '11',
        'HD': '32d10',
        'HP': '176',
        'Init': '-3',
        'Details': """slam +25 (4d6+13); construct, hardness, etc."""
    },
    "Ankheg": {
        'AC': '18',
        'HD': '3d10+9',
        'HP': '25',
        'Init': '0',
        'Details': """bite +6 (2d6+7); imp. grab, acid,
        spit acid; tremorsense"""
    },
    "Aranea": {
        'AC': '13',
        'HD': '3d8+6',
        'HP': '19',
        'Init': '+6',
        'Details': """bite +4 (1d6 & poison); poison
        (DC13, 1d6/2d6 Str), spells, web; alternate form"""
    },
    "Arrowhawk, Juv.": {
        'AC': '20',
        'HD': '3d8+3',
        'HP': '16',
        'Init': '+5',
        'Details': """electricity ray +9 (2d6), bite +9 (1d6+1);
        electricity ray; immunities, fi re and cold resistance 20"""
    },
    "Arrowhawk, Adult": {
        'AC': '21',
        'HD': '7d8+7',
        'HP': '38',
        'Init': '+5',
        'Details': """electricity ray +12 (2d8), bite +12 (1d8+2);
        electricity ray; immunities, fi re and cold resistance 20"""
    },
    "Arrowhawk, Elder": {
        'AC': '22',
        'HD': '15d8+45',
        'HP': '112',
        'Init': '+5',
        'Details': """electricity ray +19 (2d8), bite +20 (2d6+9);
        electricity ray; immunities, fi re and cold resistance 20"""
    },
    "Assassin Vine": {
        'AC': '15',
        'HD': '4d8+12',
        'HP': '30',
        'Init': '0',
        'Details': """slam +7 (1d6+7); camouflage, electricity immunity,
        cold and fire resistance 20, blindsight"""
    },
    "Basilisk": {
        'AC': '16',
        'HD': '6d10+12',
        'HP': '45',
        'Init': '-1',
        'Details': """bite +8 (1d8+3); petrifying gaze"""
    },
    "Beholder": {
        'AC': '20',
        'HD': '11d8+11',
        'HP': '60',
        'Init': '+4',
        'Details': """eye rays +7 (var.), bite +2 (2d4); eye rays;
        all-around vision, antimagic cone, fly"""
    },
    "Blink Dog": {
        'AC': '16',
        'HD': '4d10',
        'HP': '22',
        'Init': '+3',
        'Details': """bite +4 (1d6); blink, dimension door, scent"""
    },
    "Bugbear": {
        'AC': '17',
        'HD': '3d8+3',
        'HP': '16',
        'Init': '+1',
        'Details': """morningstar +4 (1d8+2), javelin +3 (1d6+2);
        darkvision 60 ft."""
    },
    "Carrion Crawler": {
        'AC': '17',
        'HD': '3d8+6',
        'HP': '19',
        'Init': '+2',
        'Details': """8 tentacles +3(par), bite -2(1d4+1); paralysis (DC13);
        scent"""
    },
    "Centaur": {
        'AC': '15',
        'HD': '4d8+8',
        'HP': '26',
        'Init': '+2',
        'Details': """greatclub +7 (1d10+4), 2 hooves +3 (1d6+2),
        mighty composite longbow +5 (1d8+4)"""
    },
    "Chimera": {
        'AC': '16',
        'HD': '9d10+27',
        'HP': '76',
        'Init': '+1',
        'Details': """bite +12 (2d6+4), bite +10 (1d8+2), butt +10 (1d8+2),
        2 claws +10 (1d6+2); breath (40 or 20 ft., DC17, 3d8); scent"""
    },
    "Cockatrice": {
        'AC': '14',
        'HD': '5d10',
        'HP': '27',
        'Init': '+3',
        'Details': """bite +4 (1d4-2); petrification; petrification immunity"""
    },
    "Devil, Imp": {
        'AC': '18',
        'HD': '3d8',
        'HP': '13',
        'Init': '+3',
        'Details': """sting +8 (1d4 &p); poison (DC13, 1d4/2d4 Dex),
        spell-like abilities; DR 5/silver, SR 5, poison immunity,
        fire resistance 20, see in darkness, polymorph, regen. 2"""
    },
    "Dino, Deinonychus": {
        'AC': '16',
        'HD': '4d10+12',
        'HP': '34',
        'Init': '+2',
        'Details': """rake +6 (2d6+4), 2 claws +1 (1d3+2), bite +1 (2d4+2);
        scent"""
    },
    "Dino, Elasmosaur.": {
        'AC': '13',
        'HD': '5d10+25',
        'HP': '52',
        'Init': '+2',
        'Details': """bite +9 (2d8+12); scent"""
    },
    "Dino, Megaraptor": {
        'AC': '16',
        'HD': '8d10+32',
        'HP': '76',
        'Init': '+2',
        'Details': """rake +9 (2d8+5), 2 claws +4 (1d4+2), bite +4 (2d6+2);
    scent"""
    },
    "Dino, Triceratops": {
        'AC': '18',
        'HD': '16d10+112',
        'HP': '200',
        'Init': '-1',
        'Details': """gore +15 (2d8+7); charge for x2 damage, trample; scent"""
    },
    "Dino, Tyrannosaur.": {
        'AC': '14',
        'HD': '18d10+72',
        'HP': '171',
        'Init': '+1',
        'Details': """bite +20 (5d8+13); improved grab, swallow whole;
    scent"""
    },
    "Dire Rat": {
        'AC': '15',
        'HD': '1d8+1',
        'HP': '5',
        'Init': '+3',
        'Details': """bite +4 (1d4 &d); disease (DC12); scent"""
    },
    "Dire Weasel": {
        'AC': '16',
        'HD': '3d8',
        'HP': '13',
        'Init': '+4',
        'Details': """bite +6 (1d6+3); attach, blood drain (2d4 Str/rnd);
    scent"""
    },
    "Dire Badger": {
        'AC': '16',
        'HD': '3d8+12',
        'HP': '25',
        'Init': '+3',
        'Details': """2 claws +4 (1d4+2), bite -1 (1d6+1); rage; scent"""
    },
    "Dire Bat": {
        'AC': '20',
        'HD': '4d8+12',
        'HP': '30',
        'Init': '+6',
        'Details': """bite +5 (1d8+4); blindsight"""
    },
    "Dire Ape": {
        'AC': '15',
        'HD': '5d8+10',
        'HP': '32',
        'Init': '+2',
        'Details': """2 claws +8 (1d6+6), bite +3 (1d8+3); rend 2d6+12; scent"""
    },
    "Dire Wolverine": {
        'AC': '16',
        'HD': '5d8+20',
        'HP': '42',
        'Init': '+3',
        'Details': """2 claws +8 (1d6+6), bite +3 (1d8+3); rage; scent"""
    },
    "Dire Wolf": {
        'AC': '14',
        'HD': '6d8+18',
        'HP': '45',
        'Init': '+2',
        'Details': """bite +10 (1d8+10); trip; scent"""
    },
    "Dire Boar": {
        'AC': '15',
        'HD': '7d8+21',
        'HP': '52',
        'Init': '0',
        'Details': """bite +12 (1d8+12); ferocity; scent"""
    },
    "Dire Lion": {
        'AC': '15',
        'HD': '8d8+24',
        'HP': '60',
        'Init': '+2',
        'Details': """2 claw +12 (1d6+7), bite +7 (1d8+3); pounce, rake
    1d6+3; scent"""
    },
    "Dire Bear": {
        'AC': '17',
        'HD': '12d8+48',
        'HP': '102',
        'Init': '+1',
        'Details': """2 claws +18 (2d4+10), bite +13 (2d8+5);
    imp. grab; scent"""
    },
    "Dire Tiger": {
        'AC': '16',
        'HD': '16d8+48',
        'HP': '120',
        'Init': '+2',
        'Details': """2 claw +18(2d4+8), bite +13 (2d6+4);
    pounce, rake 2d4+4; scent"""
    },
    "Dire Shark": {
        'AC': '17',
        'HD': '18d8+54',
        'HP': '135',
        'Init': '+2',
        'Details': """bite +17 (2d6+9); impossible grab, swallow whole;
    keen scent"""
    },
    "Doppelganger": {
        'AC': '15',
        'HD': '4d8+4',
        'HP': '22',
        'Init': '+1',
        'Details': """2 slams +4 (1d6+1); detect thoughts; alter self,
    immunities"""
    },
    "Dragon, Black, Adult": {
        'AC': '27',
        'HD': '19d12+76',
        'HP': '199',
        'Init': '0',
        'Details': """bite +24 (2d6+6), 2 claws +19 (1d8+3),
    2 wings +19 (1d6+3), tail slap +19 (1d8+9);
    breath (80 ft., DC23, 12d4), spell-like abilities, spells (3rd),
    fright (180 ft., DC20); blindsight (180 ft.),
    DR 5/+1, immunities, SR 18"""
    },
    "Dragon, Blue, Adult": {
        'AC': '28',
        'HD': '21d12+105',
        'HP': '241',
        'Init': '+4',
        'Details': """bite +26 (2d8+7), 2 claws +21 (2d6+3),
    2 wings +21 (1d8+3), tail slap +21 (2d6+10); breath (100 ft.,
    DC25, 12d8), spell-like abilities, spells (5th),
    fright (180 ft., DC23); blindsight (180 ft.),
    DR 5/+1, immunities, SR 21"""
    },
    "Dragon, Green, Adult": {
        'AC': '27',
        'HD': '20d12+100',
        'HP': '230',
        'Init': '+4',
        'Details': """bite +25 (2d8+7), 2 claws +20 (2d6+3),
    2 wings +20 (1d8+3), tail slap +20 (2d6+10);
    breath (50 ft., DC25, 12d6), spell-like abilities, spells (5th),
    fright (180 ft., DC23); blindsight (180 ft.),
    DR 5/+1, immunities, SR 21"""
    },
    "Dragon, Red, Adult": {
        'AC': '29',
        'HD': '22d12+110',
        'HP': '253',
        'Init': '+4',
        'Details': """bite +31 (2d8+11), 2 claws +26 (2d6+5),
    2 wings +26 (1d8+5), tail slap +26 (2d6+16);
    breath (50 ft., DC26, 12d10), spells (7th), fright (180 ft., DC24);
    blindsight (180 ft.), fire subtype, DR 5/+1, immunities, SR 21"""
    },
    "Dragon, White, Adult": {
        'AC': '26',
        'HD': '18d12+72',
        'HP': '189',
        'Init': '0',
        'Details': """bite +23 (2d6+6), 2 claws +18 (1d8+3),
    2 wings +18 (1d6+3), tail slap +18 (1d8+9);
    breath (40 ft., DC23, 6d6), spell-like abilities,
    spells (1st), fright (180 ft., Will DC 19); blindsight (180 ft.),
    cold subtype, DR 5/+1, immunities, SR 18"""
    },
    "Dragon, Brass, Adult": {
        'AC': '27',
        'HD': '19d12+76',
        'HP': '199',
        'Init': '0',
        'Details': """bite +24 (2d6+6), 2 claws +19 (1d8+3),
    2 wings +19 (1d6+3), tail slap +19 (1d8+9);
    breath (80 ft., DC23, 6d6 or 40 ft., sleep 1d6+6),
    spell-like abilities, spells (7th), fright (180 ft., DC21);
    blindsight (180 ft), fire s-type, DR 5/+1, immun., SR 20"""
    },
    "Dragon, Copper, Adult": {
        'AC': '28',
        'HD': '20d12+80',
        'HP': '210',
        'Init': '+4',
        'Details': """bite +25 (2d6+6), 2 claws +20 (1d8+3),
    2 wings +20 (1d6+3), tail slap +20 (1d8+9);
    breath (80 ft., DC24, 12d4 or 40 ft., slowed 1d6+6),
    spell-like abilities, spells (7th), fright (180 ft., DC23);
    blindsight (180 ft.), DR 5/+1, immunities, SR 21"""
    },
    "Dragon, Silver, Adult": {
        'AC': '29',
        'HD': '22d12+110',
        'HP': '253',
        'Init': '+4',
        'Details': """bite +28 (2d8+8), 2 claws +23 (2d6+4),
    2 wings +23 (1d8+4), tail slap +23 (2d6+12);
    breath (50 ft., DC26, 12d8 or paralyzed 1d6+6),
    spell-like abils, spells (7th), fright (180 ft., DC26);
    blindsight (180 ft.), DR 5/+1, immunities, SR 22"""
    },
    "Dryad": {
        'AC': '12',
        'HD': '2d6',
        'HP': '7',
        'Init': '+6',
        'Details': """dagger +1 (1d4); spell-like abilities; symbiosis"""
    },
    "Dwarf": {
        'AC': '16',
        'HD': '1d8+1',
        'HP': '5',
        'Init': '0',
        'Details': """waraxe +1 (1d10), short bow +1 (1d6);
    +1 attacks vs. orcs/goblins;
    +4 AC vs. giants, +2 save vs. spells/poisons, darkvision 60 ft."""
    },
    "Dwarf, Deep": {
        'AC': '16',
        'HD': '1d8+1',
        'HP': '5',
        'Init': '0',
        'Details': """waraxe +1 (1d10), short bow +1 (1d6); +4 AC vs giants,
    +3 save vs. spells/poisons, darkvision 90 ft.,
    light sensitivity (-1 attacks)"""
    },
    "Dwarf, Derro": {
        'AC': '16',
        'HD': '1d8+1',
        'HP': '5',
        'Init': '0',
        'Details': """dagger +0 (1d4), +0 (1d4),
    repetition crossbow +3 (1d8 &p); poison (DC13, 1/1d2 Con),
    +1 attacks vs orc/goblins; +4 AC vs giants,
    +2 saves vs. spells/poisons, SR 18, darkvision 30 ft.,
    light vulnerability"""
    },
    "Dwarf, Gray": {
        'AC': '16',
        'HD': '1d8+1',
        'HP': '5',
        'Init': '0',
        'Details': """heavy  pick  +1  (1d6),  light crossbow+1(1d8);
    +1 attacks vs. orc/goblins; +4 AC vs. giants,
    +2 saves vs. spells/poisons, immune to paralysis/phantasm;
    spell abilities, darkvision 120 ft., light sensitivity"""
    },
    "Elemental, Air, Small": {
        'AC': '17',
        'HD': '2d8',
        'HP': '9',
        'Init': '+7',
        'Details': """slam +5 (1d4); air mastery, whirlwind; elemental"""
    },
    "Elemental, Air, Medium": {
        'AC': '18',
        'HD': '4d8+8',
        'HP': '26',
        'Init': '+9',
        'Details': """slam +8 (1d6+1); air mastery, whirlwind; elemental"""
    },
    "Elemental, Air, Large": {
        'AC': '20',
        'HD': '8d8+24',
        'HP': '60',
        'Init': '+11',
        'Details': """slam +12/+7 (2d6+3); air mastery, whirlwind;
    elemental, DR 10/+1"""
    },
    "Elemental, Air, Huge": {
        'AC': '21',
        'HD': '16d8+64',
        'HP': '136',
        'Init': '+13',
        'Details': """slam +19/+14/+9 (2d8+6); air mastery, whirlwind;
    elemental, DR 10/+2"""
    },
    "Elemental, Air, Greater": {
        'AC': '26',
        'HD': '21d8+84',
        'HP': '178',
        'Init': '+14',
        'Details': """slam +23/+18/+13 (2d8+7); air mastery, whirlwind;
    elemental, DR 10/+2"""
    },
    "Elemental, Air, Elder": {
        'AC': '27',
        'HD': '24d8+96',
        'HP': '204',
        'Init': '+15',
        'Details': """slam +27/+22/+17/+12 (2d8+9); air mastery, whirlwind;
    elemental, DR 15/+3"""
    },
    "Elemental, Earth, Small": {
        'AC': '17',
        'HD': '2d8+2',
        'HP': '11',
        'Init': '-1',
        'Details': """slam +5 (1d6+4); earth mastery, push; elemental"""
    },
    "Elemental, Earth, Medium": {
        'AC': '18',
        'HD': '4d8+12',
        'HP': '30',
        'Init': '-1',
        'Details': """slam +8 (1d8+7); earth mastery, push; elemental"""
    },
    "Elemental, Earth, Large": {
        'AC': '18',
        'HD': '8d8+32',
        'HP': '68',
        'Init': '-1',
        'Details': """slam +12/+7 (2d8+10); earth mastery, push;
    elemental, DR 10/+1"""
    },
    "Elemental, Earth, Huge": {
        'AC': '18',
        'HD': '16d8+80',
        'HP': '152',
        'Init': '-1',
        'Details': """slam  +19/+14/+9  (2d10+13);  earth mastery, push;
    elemental, DR 10/+2"""
    },
    "Elemental, Earth, Greater": {
        'AC': '20',
        'HD': '21d8+105',
        'HP': '199',
        'Init': '-1',
        'Details': """slam +23/+18/+13 (2d10+15); earth mastery, push;
    elemental, DR 10/+2"""
    },
    "Elemental, Earth, Elder": {
        'AC': '22',
        'HD': '24d8+120',
        'HP': '228',
        'Init': '-1',
        'Details': """slam +27/+22/+17/+12 (2d10+16); earth mastery, push;
    elemental, DR 15/+3"""
    },
    "Elemental, Fire, Small": {
        'AC': '15',
        'HD': '2d8',
        'HP': '9',
        'Init': '+5',
        'Details': """slam +3 (1d4 & 1d4 fire); burn; elemental, fire subtype"""
    },
    "Elemental, Fire, Medium": {
        'AC': '16',
        'HD': '4d8+8',
        'HP': '26',
        'Init': '+7',
        'Details': """slam +6 (1d6+1 & 1d6 fire); burn;
    elemental, fire subtype"""
    },
    "Elemental, Fire, Large": {
        'AC': '18',
        'HD': '8d8+24',
        'HP': '60',
        'Init': '+9',
        'Details': """slam +10/+5 (2d6+3 & 2d6 fire); burn;
    elemental, DR 10/+1, fire subtype"""
    },
    "Elemental, Fire, Huge": {
        'AC': '19',
        'HD': '16d8+64',
        'HP': '136',
        'Init': '+11',
        'Details': """slam +17/+12/+7 (2d8+6 & 2d8 fire); burn;
    elemental, DR 10/+2, fire subtype"""
    },
    "Elemental, Fire, Greater": {
        'AC': '24',
        'HD': '21d8+84',
        'HP': '178',
        'Init': '+12',
        'Details': """slam +21/+16/+11 (2d8+7 & 2d8 fire); burn;
    elemental, DR 10/+2, fire subtype"""
    },
    "Elemental, Fire, Elder": {
        'AC': '25',
        'HD': '24d8+96',
        'HP': '204',
        'Init': '+13',
        'Details': """slam +25/+20/+15/+10 (2d8+9 & 2d8 fire); burn;
    elemental, DR 15/+3, fire subtype"""
    },
    "Elemental, Water, Small": {
        'AC': '17',
        'HD': '2d8+2',
        'HP': '11',
        'Init': '0',
        'Details': """slam +4 (1d6+3); water mastery, drench, vortex;
    elemental"""
    },
    "Elemental, Water, Medium": {
        'AC': '19',
        'HD': '4d8+12',
        'HP': '30',
        'Init': '+1',
        'Details': """slam +6 (1d8+4); water mastery, drench, vortex;
    elemental"""
    },
    "Elemental, Water, Large": {
        'AC': '20',
        'HD': '8d8+32',
        'HP': '68',
        'Init': '+2',
        'Details': """slam +10/+5 (2d8+7); water mastery, drench, vortex;
    elemental, DR 10/+1"""
    },
    "Elemental, Water, Huge": {
        'AC': '21',
        'HD': '16d8+80',
        'HP': '152',
        'Init': '+4',
        'Details': """slam +17/+12/+7 (2d10+10); water mastery, drench,
    vortex; elemental, DR 10/+2"""
    },
    "Elemental, Water, Greater": {
        'AC': '22',
        'HD': '21d8+105',
        'HP': '199',
        'Init': '+5',
        'Details': """slam +21/+16/+11 (2d10+12 ); water mastery, drench,
    vortex; elemental, DR 10/+2"""
    },
    "Elemental, Water, Elder": {
        'AC': '23',
        'HD': '24d8+120',
        'HP': '228',
        'Init': '+6',
        'Details': """slam +25/+20/+15/+10 (2d10+13); water mastery, drench,
    vortex; elemental, DR 15/+3"""
    },
    "Elf, Aquatic": {
        'AC': '15',
        'HD': '1d8',
        'HP': '4',
        'Init': '+1',
        'Details': """trident +1 (1d8), light spear +1 (1d8),
    net touch +2 (entangle); gills, low-light vision,
    +2 save vs enchantments, immune to sleep"""
    },
    "Elf, Wild": {
        'AC': '15',
        'HD': '1d8',
        'HP': '4',
        'Init': '+1',
        'Details': """longsword  +1  (1d8),  longbow  +2 (1d8);
    low-light vision, +2 saves vs. enchantment, immune to sleep"""
    },
    "Ettercap": {
        'AC': '14',
        'HD': '5d8+5',
        'HP': '27',
        'Init': '+3',
        'Details': """bite +3 (1d8 &p), 2 claws +1 (1d3);
    poison (DC13, 1d6/2d6 Dex), web, poison; low-light vision"""
    },
    "Ettin": {
        'AC': '18',
        'HD': '10d8+20',
        'HP': '65',
        'Init': '+3',
        'Details': """2  greatclubs  +12/+7  (1d10+6),  2 longspears +5/+0
    (1d8+6); superior two-weapon fighting; darkvision 90 ft."""
    },
    "Gargoyle": {
        'AC': '16',
        'HD': '4d10+16',
        'HP': '38',
        'Init': '+2',
        'Details': """2 claw +6 (1d4), bite +4 (1d6), gore +4 (1d6);
    DR 15/+1, frz."""
    },
    "Genie, Janni": {
        'AC': '18',
        'HD': '6d8+6',
        'HP': '33',
        'Init': '+6',
        'Details': """scimitar +9/+4 (1d8+4), longbow +8/+3 (1d8);
    spell-like abilities; plane shift, telepathy, fire resistance 30,
    elemental endurance"""
    },
    "Genie, Djinni": {
        'AC': '16',
        'HD': '7d8+14',
        'HP': '45',
        'Init': '+8',
        'Details': """slam +10/+5 (1d8+6); spell-like abilities, air mastery,
    whirlwind; plane shift, telepathy, acid immunity"""
    },
    "Genie, Efreeti": {
        'AC': '18',
        'HD': '10d8+20',
        'HP': '65',
        'Init': '+7',
        'Details': """slam +15/+10 (1d8+9 and 1d6 fire); spell-like abilities,
    heat; plane shift, telepathy"""
    },
    "Ghoul": {
        'AC': '14',
        'HD': '2d12',
        'HP': '13',
        'Init': '+2',
        'Details': """bite +3 (1d6+1 & par), 2 claws +0 (1d3 &par); paralysis
    (DC14), create spawn; undead, +2 turn resistance"""
    },
    "Ghast": {
        'AC': '16',
        'HD': '4d12',
        'HP': '26',
        'Init': '+2',
        'Details': """bite +4(1d8+1 & par), 2 claws +1 (1d4 & par);
    stench (10 ft., DC15, -2 to all rolls), paralysis (DC15), create spawn;
    undead, +2 turn resistance"""
    },
    "Giant, Hill": {
        'AC': '20',
        'HD': '12d8+48',
        'HP': '102',
        'Init': '-1',
        'Details': """huge greatclub +16/+11 (2d6+10), rock +8/+3 (2d6+7);
    rock throwing, rock catching"""
    },
    "Giant, Stone": {
        'AC': '25',
        'HD': '14d8+56',
        'HP': '119',
        'Init': '+2',
        'Details': """huge greatclub +17/+12 (2d6+12), rock +12/+7 (2d8+8);
    rock throwing; rock catching"""
    },
    "Giant, Frost": {
        'AC': '21',
        'HD': '14d8+70',
        'HP': '133',
        'Init': '-1',
        'Details': """huge greataxe +18/+13 (2d8+13), rock +9/+4 (2d6+9);
    rock throwing; rock catching, cold subtype"""
    },
    "Giant, Fire": {
        'AC': '21',
        'HD': '15d8+75',
        'HP': '142',
        'Init': '-1',
        'Details': """huge greatsword +20/+15/+10 (2d8+15), rock +10/+5/+0
    (2d6+10 & 2d6 fire); rock throwing; rock catching, fire subtype"""
    },
    "Giant, Cloud": {
        'AC': '21',
        'HD': '17d8+102',
        'HP': '178',
        'Init': '+1',
        'Details': """gargantuan morningstar +22/+17/+12 (4d6+18),
    rock +12/+7/+2 (2d8+12); rock throwing, spell-like abilities;
    rock catching, scent"""
    },
    "Giant Eagle": {
        'AC': '15',
        'HD': '4d10+4',
        'HP': '26',
        'Init': '+3',
        'Details': """2 claws +7 (1d6+4), bite +2 (1d8+2); evasion"""
    },
    "Giant Owl": {
        'AC': '15',
        'HD': '4d10+4',
        'HP': '26',
        'Init': '+32',
        'Details': """claws +7 (1d6+4), bite +2 (1d8+2);
    superior low-light vision"""
    },

    "Girallon": {
        'AC': '16',
        'HD': '7d10+14',
        'HP': '52',
        'Init': '+3',
        'Details': """4 claws +12 (1d4+8), bite +7 (1d8+4); rend 2d4+12;
        scent"""
    },
    "Gnoll": {
        'AC': '17',
        'HD': '2d8+2',
        'HP': '11',
        'Init': '0',
        'Details': """battleaxe +3 (1d8+2), shortbow +1 (1d6);
    darkvision 60 ft."""
    },
    "Gnome": {
        'AC': '16',
        'HD': '1d8+1',
        'HP': '5',
        'Init': '0',
        'Details': """short sword +2 (1d6-1), light crossbow+2 (1d8); spells;
    low-light vision, +2 save vs illusion, +1 attacks vs kobold/goblin,
    +4 AC vs giant"""
    },
    "Gnome, Forest": {
        'AC': '16',
        'HD': '1d8+1',
        'HP': '5',
        'Init': '0',
        'Details': """short sword +2 (1d6-1), light crossbow+2 (1d8);
    pass., low-light vision, +2 save vs illusion,
    +1 attacks vs humanoids, +4 AC vs giant"""
    },
    "Goblin": {
        'AC': '15',
        'HD': '1d8',
        'HP': '4',
        'Init': '+1',
        'Details': """morningstar +1 (1d8-1), dart +3 (1d4-1);
    darkvision 60 ft."""
    },
    "Golem, Flesh": {
        'AC': '18',
        'HD': '9d10',
        'HP': '49',
        'Init': '-1',
        'Details': """2 slams +10 (2d8+5); berserk; construct,
    magic immunity, DR 15/+1"""
    },
    "Golem, Clay": {
        'AC': '22',
        'HD': '11d10',
        'HP': '60',
        'Init': '-1',
        'Details': """2 slams +14 (2d10+7); berserk, wound; construct,
        magic immunity, DR 20/+1, immune to piercing/slashing, haste"""
    },
    "Golem, Stone": {
        'AC': '26',
        'HD': '14d10',
        'HP': '77',
        'Init': '-1',
        'Details': """2 slams +18 (2d10+9); slow; construct,
    magic immunity, DR 30/+2"""
    },
    "Golem, Iron": {
        'AC': '30',
        'HD': '18d10',
        'HP': '99',
        'Init': '-1',
        'Details': """2 slams +23 (2d10+11); breath (10 ft.,p);
    poison (DC17, 1d4 STR/death), construct, magic immunity,
    DR 50/+3, rust vulnerability"""
    },
    "Gorgon": {
        'AC': '18',
        'HD': '8d10+24',
        'HP': '68',
        'Init': '+4',
        'Details': """gore +12 (1d8+7); breath weapon (60 ft., Fort DC17, turn
    to stone), trample 1d8+7; scent"""
    },
    "Halfling": {
        'AC': '15',
        'HD': '1d8',
        'HP': '4',
        'Init': '+1',
        'Details': """light sword+2 (1d8-1), heavy crossbow +3 (1d10);
    +2 saves vs. fear"""
    },
    "Halfling, Tallfellow": {
        'AC': '15',
        'HD': '1d8',
        'HP': '4',
        'Init': '+1',
        'Details': """light sword+2 (1d8-1), heavy crossbow +3 (1d10);
    +2 saves vs. fear"""
    },
    "Halfling, Deep": {
        'AC': '15',
        'HD': '1d8',
        'HP': '4',
        'Init': '+1',
        'Details': """light sword+2 (1d8-1), heavy crossbow +3 (1d10);
    +2 saves vs. fear, darkvision 60 ft., stonecunning"""
    },
    "Harpy": {
        'AC': '13',
        'HD': '7d8',
        'HP': '31',
        'Init': '+2',
        'Details': """club +7/+2 (1d4), 2 claws +2 (1d3); captivating
    song"""
    },
    "Hell Hound": {
        'AC': '16',
        'HD': '4d8+4',
        'HP': '22',
        'Init': '+5',
        'Details': """bite +5 (1d8+1); breath (30 ft., DC13, 1d4+1);
    scent, fire subtype"""
    },
    "Hippogriff": {
        'AC': '15',
        'HD': '3d10+9',
        'HP': '25',
        'Init': '+2',
        'Details': """2 claws +5 (1d4+4), bite +0 (1d8+2)Hobgoblin 15 1d8+1 5 +1
    longsword +1 (1d8), javelin +2 (1d6); darkvision 60 ft."""
    },
    "Homunculus": {
        'AC': '14',
        'HD': '2d10',
        'HP': '11',
        'Init': '+2',
        'Details': """bite +2 (1d4-1 &p); poison (DC11, 1/ 5d6 min. sleep),
    construct"""
    },
    "Howler": {
        'AC': '17',
        'HD': '6d8+12',
        'HP': '39',
        'Init': '+7',
        'Details': """bite +10 (2d8+5), 1d4 quills +5 (1d4+2); quills, howl"""
    },
    "Hydra (5 heads)": {
        'AC': '10',
        'HD': '+25',
        'HP': '52',
        'Init': '+1',
        'Details': """5 bites +4 (1d10+3); scent"""
    },
    "Hydra (6 heads)": {
        'AC': '10',
        'HD': '+30',
        'HP': '63',
        'Init': '+1',
        'Details': """6 bites +5 (1d10+3); scent"""
    },
    "Hydra (7 heads)": {
        'AC': '10',
        'HD': '+35',
        'HP': '73',
        'Init': '+1',
        'Details': """7 bites +7 (1d10+4); scent"""
    },
    "Hydra (8 heads)": {
        'AC': '10',
        'HD': '+40',
        'HP': '84',
        'Init': '+1',
        'Details': """8 bites +8 (1d10+4); scent"""
    },
    "Hydra (9 heads)": {
        'AC': '10',
        'HD': '+45',
        'HP': '94',
        'Init': '+1',
        'Details': """9 bites +9 (1d10+5); scent"""
    },
    "Hydra (10 heads)": {
        'AC': '10',
        'HD': '+50',
        'HP': '105',
        'Init': '+1',
        'Details': """10 bites +10 (1d10+5); scent"""
    },
    "Hydra (11 heads)": {
        'AC': '10',
        'HD': '+55',
        'HP': '115',
        'Init': '+1',
        'Details': """11 bites +12 (1d10+6); scent"""
    },
    "Hydra (12 heads)": {
        'AC': '10',
        'HD': '+60',
        'HP': '126',
        'Init': '+1',
        'Details': """12 bites +13 (1d10+6); scent"""
    },
    "Invisible Stalker": {
        'AC': '17',
        'HD': '8d8+16',
        'HP': '52',
        'Init': '+8',
        'Details': """slam +10/+5 (2d6+6); elemental, natural invisibility,
    imp. track"""
    },
    "Kraken": {
        'AC': '20',
        'HD': '20d10+180',
        'HP': '290',
        'Init': '+4',
        'Details': """2 tentacle rakes +28 (2d8+12), 6 arms +23 (1d6+6),
    bite +23 (4d6+6); improved grab, constrict 2d8+12 or 1d6+6;
    jet, ink cloud, spell-like abilities"""
    },
    "Kuo-Toa": {
        'AC': '18',
        'HD': '2d8+2',
        'HP': '11',
        'Init': '0',
        'Details': """spear  +3  (1d8+1),  bite  -2  (1d4); lightning bolt,
    pincer  staff;  keen sight, slippery, adhesive, immunities,
    electricity resistance 30, light blindness, amphibious"""
    },
    "Lamia": {
        'AC': '17',
        'HD': '9d10+9',
        'HP': '58',
        'Init': '+2',
        'Details': """touch +9 (1 permanent MIND drain), dagger +11/+6
    (1d4); spell-like abilities, wisdom drain"""
    },
    "Lammasu": {
        'AC': '14',
        'HD': '7d10+21',
        'HP': '59',
        'Init': '0',
        'Details': """2 claws +12 (1d6+6); spells, pounce, rake 1d6+3;
    magic circle against evil, spell-like abilities"""
    },
    "Lizardfolk": {
        'AC': '15',
        'HD': '2d8+2',
        'HP': '11',
        'Init': '0',
        'Details': """2 claws +2 (1d4+1), bite +0 (1d4), javelin +1 (1d6+1)"""
    },
    "Locathah": {
        'AC': '14',
        'HD': '2d8',
        'HP': '9',
        'Init': '+1',
        'Details': """longspear +1 (1d8), light crossbow +2 (1d8)"""
    },
    "Magmin": {
        'AC': '14',
        'HD': '2d8',
        'HP': '9',
        'Init': '+1',
        'Details': """burning touch +1 (1d8 fire and combustion); combustion,
    fiery aura; elemental, fire subtype, melt weapon, DR 15/+1"""
    },
    "Manticore": {
        'AC': '16',
        'HD': '6d10+24',
        'HP': '57',
        'Init': '+2',
        'Details': """2 claw +9 (2d4+5), bite +7 (1d8+2), 6 spikes +6 (1d8+2);
        scent"""
    },
    "Medusa": {
        'AC': '8',
        'HD': '+6',
        'HP': '33',
        'Init': '+2',
        'Details': """shortbow +8/+3 (1d6), dagger +6/+1 (1d4),
        snakes +3 (1d4 &p); poison (DC14, 1d6/2d6 Str),
        petrifying gaze, poison"""
    },
    "Mephit, Air": {
        'AC': '17',
        'HD': '3d8',
        'HP': '13',
        'Init': '+7',
        'Details': """2 claws +4 (1d3); breath (15 ft., DC12, 1d8),
        spell-like abilities, summon mephit; fast healing 2, DR 5/+1"""
    },
    "Mephit, Dust": {
        'AC': '17',
        'HD': '3d8',
        'HP': '13',
        'Init': '+7',
        'Details': """2 claws +4(1d3); breath (10 ft.,
        DC12, 1d4 & torment), spell-like abilities, summon mephit;
        fast healing 2, DR 5/+1"""
    },
    "Mephit, Earth": {
        'AC': '16',
        'HD': '3d8+3',
        'HP': '16',
        'Init': '-1',
        'Details': """2 claws +7 (1d3+3); breath (15 ft., DC12, 1d8),
        spell-like abilities, summon mephit; fast healing 2, DR 10/+1"""
    },
    "Mephit, Fire": {
        'AC': '16',
        'HD': '3d8',
        'HP': '13',
        'Init': '+5',
        'Details': """2 claws +4 (1d3 & 2 fire); breath (15 ft., DC12, 1d8),
        spell-like abils, summon mephit; fire subtype, fast heal 2, DR 5/+1"""
    },
    "Mephit, Ice": {
        'AC': '18',
        'HD': '3d8',
        'HP': '13',
        'Init': '+7',
        'Details': """2 claws +4 (1d3 & 2 cold); breath (10 ft., DC12,
        1d4 & torment), spell-like abilities, summon mephit; cold subtype,
        fast healing 2, DR 5/+1"""
    },
    "Mephit, Magma": {
        'AC': '16',
        'HD': '3d8',
        'HP': '13',
        'Init': '+5',
        'Details': """2 claws +4 (1d3 & 2 fire); breath (10 ft., DC12,
        1d4 & torment), spell-like abilities, summon mephit; fire subtype,
        fast healing 2, DR 5/+1"""
    },
    "Mephit, Ooze": {
        'AC': '16',
        'HD': '3d8+3',
        'HP': '16',
        'Init': '0',
        'Details': """2 claws +6 (1d3+2); breath (10 ft., DC12,
        1d4 & torment), spell-like abilities, summon mephit;
        fast healing 2, DR 5/+1"""
    },
    "Mephit, Salt": {
        'AC': '16',
        'HD': '3d8+3',
        'HP': '16',
        'Init': '-1',
        'Details': """2 claws +7 (1d3+3); breath (10 ft., DC12,
        1d4 & torment), spell-like abilities, summon mephit;
        fast healing 2, DR 10/+1"""
    },
    "Merfolk": {
        'AC': '13',
        'HD': '1d8+1',
        'HP': '5',
        'Init': '+1',
        'Details': """trident +1 (1d8), heavy crossbow +2 (1d10);
        low-light visionMimic 13 7d8+21 52 +1 slam +8 (1d8+6);
        adhesive; mimic shape, acid immunity"""
    },
    "Mind Flayer": {
        'AC': '15',
        'HD': '8d8+8',
        'HP': '44',
        'Init': '+6',
        'Details': """4 tentacles +8 (1d4+1); mind blast
        (-2 to hit and defend), psionics, improved grab,
        extract thoughts; SR 25, telepathy"""
    },
    "Minotaur": {
        'AC': '14',
        'HD': '6d8+12',
        'HP': '39',
        'Init': '0',
        'Details': """huge greataxe +9/+4 (2d8+6), gore +4 (1d8+2);
        charge 4d6+6; scent, natural cunning"""
    },
    "Naga, Water": {
        'AC': '15',
        'HD': '7d8+28',
        'HP': '59',
        'Init': '+1',
        'Details': """bite +7 (2d6+4 &p); poison (DC17, 1d8 Con), spells"""
    },
    "Naga, Spirit": {
        'AC': '16',
        'HD': '9d8+36',
        'HP': '76',
        'Init': '+1',
        'Details': """bite +9 (2d6+6 &p); poison (DC18, 1d8 Con), charm gaze,
        spells"""
    },
    "Naga, Dark": {
        'AC': '14',
        'HD': '9d8+18',
        'HP': '58',
        'Init': '+2',
        'Details': """sting +7 (2d4+2 &p), bite +2 (1d4+1);
        poison (DC16, 2d4 min. sleep), detect thoughts, spells;
        poison immunity, guarded thoughts, charm resistance"""
    },
    "Naga, Guardian": {
        'AC': '18',
        'HD': '11d8+44',
        'HP': '93',
        'Init': '+2',
        'Details': """bite +12 (2d6+7 &p); poison (DC19, 2d8 Con),
        spit, spells"""
    },
    "Nymph": {
        'AC': '11',
        'HD': '3d6',
        'HP': '10',
        'Init': '+1',
        'Details': """dagger +1 (1d4); blindsight, unearthly beauty,
        spell-like abilities"""
    },
    "Ogre": {
        'AC': '16',
        'HD': '4d8+8',
        'HP': '26',
        'Init': '-1',
        'Details': """huge greatclub +8 (2d6+7), large javelin +1 (1d8+5)"""
    },
    "Ogre Mage": {
        'AC': '18',
        'HD': '5d8+15',
        'HP': '37',
        'Init': '+4',
        'Details': """huge greatsword +7 (2d8+7), huge longbow +2 (2d6);
        spell-like abilities; regeneration 2, SR 18"""
    },
    "Orc": {
        'AC': '14',
        'HD': '1d8',
        'HP': '4',
        'Init': '0',
        'Details': """greataxe +3 (1d12+3), javlin +1 (1d6+2);
        arkvision 60 ft., light sensitivity"""
    },
    "Owlbear": {
        'AC': '15',
        'HD': '5d10+20',
        'HP': '47',
        'Init': '+1',
        'Details': """2 claws +7 (1d6+5), bite +2 (1d8+2); improved grab;
        scent"""
    },
    "Pegasus": {
        'AC': '14',
        'HD': '4d10+12',
        'HP': '34',
        'Init': '+22',
        'Details': """hooves +7 (1d6+4), bite +2 (1d3+2); scent,
        spell abilities"""
    },
    "Phase Spider": {
        'AC': '15',
        'HD': '5d10+15',
        'HP': '42',
        'Init': '+7',
        'Details': """bite +7(1d6+4 & poison); poison (DC15, 2d6 STR), ethereal
        jaunt"""
    },
    "Phasm": {
        'AC': '17',
        'HD': '15d8+30',
        'HP': '97',
        'Init': '+6',
        'Details': """2 slams +12 (1d3+1); amorphous, scent, alternate form,
        telepathy, tremorsense"""
    },
    "Rakshasa": {
        'AC': '21',
        'HD': '7d8+21',
        'HP': '52',
        'Init': '+2',
        'Details': """2 claws +8 (1d4+1), bite +3 (1d6);
        detect thoughts, spells; alternate form, spell immunity,
        vulnerable to blessed crossbow bolts, DR 20/+3"""
    },
    "Roc": {
        'AC': '14',
        'HD': '18d10+126',
        'HP': '225',
        'Init': '+2',
        'Details': """2 claws +21 (2d6+12), bite +16 (2d8+6); snatch"""
    },
    "Satyr": {
        'AC': '15',
        'HD': '5d6+5',
        'HP': '22',
        'Init': '+1',
        'Details': """gore +2 (1d6), dagger -3 (1d4), shortbow +3 (1d6);
        pipes"""
    },
    "Sea Lion": {
        'AC': '18',
        'HD': '6d10+18',
        'HP': '51',
        'Init': '+1',
        'Details': """2 claws +7 (1d6+4), bite +2 (1d8+2); rend 2d6+6; scent"""
    },
    "Shadow": {
        'AC': '13',
        'HD': '3d12',
        'HP': '19',
        'Init': '+2',
        'Details': """incorporeal touch +3 (1d6 Str); strength damage,
        create spawn; undead, incorporeal, +2 turn resistance"""
    },
    "Skeleton, Medium": {
        'AC': '13',
        'HD': '1d12',
        'HP': '6',
        'Init': '+5',
        'Details': """2 claws +0 (1d4); undead, immunities"""
    },
    "Skeleton, Large": {
        'AC': '13',
        'HD': '2d12',
        'HP': '13',
        'Init': '+5',
        'Details': """2 claws +2 (1d6+2); undead, immunities"""
    },
    "Skeleton, Huge": {
        'AC': '13',
        'HD': '4d12',
        'HP': '26',
        'Init': '+5',
        'Details': """2 claws +4 (1d8+4); undead, immunities"""
    },
    "Skeleton, Gargantuan": {
        'AC': '13',
        'HD': '16d12',
        'HP': '104',
        'Init': '+5',
        'Details': """2  claws  +10  (2d6+6);  undead, immunities"""
    },
    "Skeleton, Colossal": {
        'AC': '13',
        'HD': '32d12',
        'HP': '208',
        'Init': '+5',
        'Details': """2  claws  +16  (2d8+8);  undead, immunities"""
    },
    "Slaad, Red": {
        'AC': '16',
        'HD': '7d8+21',
        'HP': '52',
        'Init': '+1',
        'Details': """bite +10 (2d8+4), 2 claws +8 (1d4+2 & implant);
        pounce, implant eggs inside victim, stunning croak,
        summon slaad; fast healing 5, resistances"""
    },
    "Slaad, Blue": {
        'AC': '18',
        'HD': '8d8+24',
        'HP': '60',
        'Init': '+2',
        'Details': """4 rakes +11 (2d6+4), bite +9 (2d8+2 &d);
        spell-like abilities, disease (DC17), summon slaad;
        fast heal. 5, resistances"""
    },
    "Slaad, Green": {
        'AC': '20',
        'HD': '9d8+27',
        'HP': '67',
        'Init': '+1',
        'Details': """2 claws +12 (1d6+4), bite +10 (2d8+2);
        spell-like abilities, summon slaad; fast healing 5, resistances"""
    },
    "Slaad, Gray": {
        'AC': '22',
        'HD': '10d8+30',
        'HP': '75',
        'Init': '+1',
        'Details': """2 claws +14 (2d4+4), bite +12 (2d8+2);
        spell-like  abilities,  summon  slaad; fast healing 5,
        DR 10/+1, resistances, alternate form"""
    },
    "Slaad, Death": {
        'AC': '26',
        'HD': '15d8+45',
        'HP': '112',
        'Init': '+8',
        'Details': """2 claws +20 (3d6+5 and stun), bite +18 (2d10+2);
        stun, spell-like abilities, summon slaad; fast healing 5, DR 20/+2,
        resistances, telepathy, alternate form"""
    },
    "Spectre": {
        'AC': '15',
        'HD': '7d12',
        'HP': '45',
        'Init': '+7',
        'Details': """incorporeal touch +6 (1d8 and energy drain);
        energy drain (x2, remove DC15), create spawn; undead, incorporeal,
        +2 turn resistance, unnatural aura, sunlight powerlessness"""
    },
    "Sprite, Grig": {
        'AC': '6',
        'HD': '+1',
        'HP': '2',
        'Init': '+4',
        'Details': """diminutive short sword +6 (1d3-3), composite
        shortbow +6 (1d4); spell-like abilities, SR 17"""
    },
    "Sprite, Nixie": {
        'AC': '14',
        'HD': '1d6',
        'HP': '3',
        'Init': '+7',
        'Details': """dagger +4 (1d4-2), light crossbow +4 (1d8);
        water breathing, charm person; SR 16"""
    },
    "Sprite, Pixie": {
        'AC': '16',
        'HD': '1d6',
        'HP': '3',
        'Init': '+4',
        'Details': """dagger +5 (1d4-2), composite shortbow +6 (1d6);
        spell-like abilities, special arrows; SR 16, natural invisibility"""
    },
    "Tarrasque": {
        'AC': '35',
        'HD': '48d10+576',
        'HP': '840',
        'Init': '+7',
        'Details': """bite +57 (4d8+17), 2 horns +52 (1d10+8),
        2 claws +52 (1d12+8), tail slap +52 (3d8+8); frightful presence (DC26),
        rush (150 ft.), improved grab, swallow whole, augmented criticals
        (18-20/x3); DR 25/+5, carapace, immunities, regeneration 40, scent,
        SR 32"""
    },
    "Treant (Ent)": {
        'AC': '8',
        'HD': '+35',
        'HP': '66',
        'Init': '-1',
        'Details': """2 slams +12 (2d6+9); animate trees,
        trample, double damage against objects; plant, fire vulnerability,
        half damage from piercing"""
    },
    "Triton": {
        'AC': '16',
        'HD': '3d8+3',
        'HP': '16',
        'Init': '0',
        'Details': """trident +4 (1d8+1), heavy crossbow +3 (1d10);
        spell-like abilities"""
    },
    "Troglodyte": {
        'AC': '15',
        'HD': '2d8+4',
        'HP': '13',
        'Init': '-1',
        'Details': """longspear +1 (1d8), bite -1 (1d4), stench
        (30 ft., DC13, -2 morale), darkvision 90 ft."""
    },
    "Troll": {
        'AC': '18',
        'HD': '6d8+36',
        'HP': '63',
        'Init': '+2',
        'Details': """2 claws +9 (1d6+6), bite +4 (1d6+3); rend
        2d6+9; regeneration 5, scent, darkvision 90 ft."""
    },
    "Umber Hulk": {
        'AC': '17',
        'HD': '8d8+32',
        'HP': '68',
        'Init': '+1',
        'Details': """2 claws +11 (2d4+6), bite +9 (2d8+3);
        confusing gaze; tremorsense"""
    },
    "Unicorn": {
        'AC': '18',
        'HD': '4d10+20',
        'HP': '42',
        'Init': '+3',
        'Details': """horn +11 (1d8+8), 2 hooves +3 (1d4+2);
        magic circle against evil, spell-like abilities, immunities"""
    },
    "Vampire Spawn": {
        'AC': '15',
        'HD': '4d12',
        'HP': '26',
        'Init': '+6',
        'Details': """slam +5 (1d6+4 & energy drain); charm,
        energy drain (remove DC14), blood drain (1d4 Con/round);
        undead, +2 turn resist., DR 10/silver, cold and electricity
        resistance 10, gaseous form, spider climb, fast healing 2"""
    },
    "Will-o’-wisp": {
        'AC': '29',
        'HD': '9d8',
        'HP': '40',
        'Init': '+13',
        'Details': """shock +16 (2d8); spell immunity, natural invisibility"""
    },
    "Winter Wolf": {
        'AC': '15',
        'HD': '6d10+18',
        'HP': '51',
        'Init': '+5',
        'Details': """bite +9 (1d8+6); breath (15 ft, DC16, 4d6), trip;
        sct, cold subtype"""
    },
    "Worg": {
        'AC': '14',
        'HD': '4d10+8',
        'HP': '30',
        'Init': '+2',
        'Details': """bite +7 (1d6+4); trip; scent"""
    },
    "Wraith": {
        'AC': '15',
        'HD': '5d12',
        'HP': '32',
        'Init': '+7',
        'Details': """incorporeal touch +5 (1d4 & 1d6 perm. STR);
        create spawn; undead, incorporeal, +2 turn resistance,
        unnatural aura, daylight powerlessness"""
    },
    "Wyvern": {
        'AC': '17',
        'HD': '7d12+14',
        'HP': '59',
        'Init': '+1',
        'Details': """sting +9 (1d6+4 &p), bite +4 (2d8+2),
        2 wings +4 (1d8+2), 2 claws +9 (1d6+4); poison (DC17, 2d6 Con),
        improved grab, snatch; scent"""
    },
    "Zombie, Tiny": {
        'AC': '12',
        'HD': '+3',
        'HP': '6',
        'Init': '-1',
        'Details': """slam +2 (1d3); undead, partial actions only"""
    },
    "Zombie, Small": {
        'AC': '11',
        'HD': '1d12+3',
        'HP': '9',
        'Init': '-1',
        'Details': """slam +1 (1d4); undead, partial actions only"""
    },
    "Zombie, Medium": {
        'AC': '11',
        'HD': '2d12+3',
        'HP': '16',
        'Init': '-1',
        'Details': """slam +2 (1d6+1); undead, partial actions only"""
    },
    "Zombie, Large": {
        'AC': '11',
        'HD': '4d12+3',
        'HP': '29',
        'Init': '-1',
        'Details': """slam +4 (1d8+4); undead, partial actions only"""
    },
    "Zombie, Huge": {
        'AC': '11',
        'HD': '8d12+3',
        'HP': '55',
        'Init': '-1',
        'Details': """slam +7 (2d6+7); undead, partial actions only"""
    },
    "Zombie, Gargantuan": {
        'AC': '11',
        'HD': '24d12+3',
        'HP': '159',
        'Init': '-1',
        'Details': """slam +15 (2d8+10); undead, partial actions only"""
    },
    "Zombie, Colossal": {
        'AC': '11',
        'HD': '48d12+3',
        'HP': '315',
        'Init': '-2',
        'Details': """slam +25 (4d6+13); undead, partial actions only"""
    },
    "Ape": {
        'AC': '14',
        'HD': '4d8+8',
        'HP': '26',
        'Init': '+2',
        'Details': """2 claws +7 (1d6+5), bite +2 (1d6+2); scent"""
    },
    "Baboon": {
        'AC': '13',
        'HD': '1d8+1',
        'HP': '5',
        'Init': '+2',
        'Details': """bite +2 (1d6+3); scent"""
    },
    "Badger": {
        'AC': '15',
        'HD': '1d8+2',
        'HP': '6',
        'Init': '+3',
        'Details': """2 claws +5 (1d2-1), bite +0 (1d3-1); rage; scent"""
    },
    "Bear, Black": {
        'AC': '13',
        'HD': '3d8+6',
        'HP': '19',
        'Init': '+1',
        'Details': """2 claws +6 (1d4+4), bite +1 (1d6+2); scent"""
    },
    "Bear, Brown": {
        'AC': '15',
        'HD': '6d8+24',
        'HP': '51',
        'Init': '+1',
        'Details': """2 claws +11 (1d8+8), bite +6 (2d8+4); improved grab;
        scent"""
    },
    "Bear, Polar": {
        'AC': '15',
        'HD': '8d8+32',
        'HP': '68',
        'Init': '+1',
        'Details': """2 claws +13 (1d8+8), bite +8 (2d8+4); improved grab;
        scent"""
    },
    "Bison": {
        'AC': '13',
        'HD': '5d8+15',
        'HP': '37',
        'Init': '0',
        'Details': """butt +6 (1d8+6); stampede; scent"""
    },
    "Boar": {
        'AC': '16',
        'HD': '3d8+9',
        'HP': '22',
        'Init': '0',
        'Details': """gore +4 (1d8+3); ferocity; scent"""
    },
    "Camel": {
        'AC': '13',
        'HD': '3d8+6',
        'HP': '19',
        'Init': '+3',
        'Details': """bite +5 (1d4+6); scent"""
    },
    "Cheetah": {
        'AC': '15',
        'HD': '3d8+6',
        'HP': '19',
        'Init': '+4',
        'Details': """bite +6 (1d6+3), 2 claws +1 (1d2+1); trip; sprint"""
    },
    "Crocodile": {
        'AC': '15',
        'HD': '3d8+9',
        'HP': '22',
        'Init': '+1',
        'Details': """bite +6 (1d8+6), tail slap +6 (1d12+6); improved grab"""
    },
    "Crocodile, Giant": {
        'AC': '16',
        'HD': '7d8+28',
        'HP': '59',
        'Init': '+1',
        'Details': """bite +11 (2d8+12), tail slap +11 (1d12+12);
        improved grab"""
    },
    "Dog": {
        'AC': '15',
        'HD': '1d8+2',
        'HP': '6',
        'Init': '+3',
        'Details': """bite +2 (1d4+1); scent"""
    },
    "Dog, Riding": {
        'AC': '16',
        'HD': '2d8+4',
        'HP': '13',
        'Init': '+2',
        'Details': """bite +3 (1d6+3); scentDonkey 13 2d8+2 11 +1 bite +1 (1d2);
        scent"""
    },
    "Eagle": {
        'AC': '14',
        'HD': '1d8+1',
        'HP': '5',
        'Init': '+2',
        'Details': """2 claws +3 (1d3), bite -2 (1d4)"""
    },
    "Elephant": {
        'AC': '15',
        'HD': '11d8+55',
        'HP': '104',
        'Init': '0',
        'Details': """slam +16 (2d6+10), 2 stamps +11 (2d6+5),
        gore +16 (2d8+15); trample 2d8+15; scent"""
    },
    "Hawk": {
        'AC': '17',
        'HD': '1d8',
        'HP': '4',
        'Init': '+3',
        'Details': """claws +5 (1d4-2)Horse, Heavy 13 3d8+6 19 +1 2 hooves +3}
        (1d6+2); scent"""
    },
    "Horse, Heavy War": {
        'AC': '14',
        'HD': '4d8+12',
        'HP': '30',
        'Init': '+1',
        'Details': """2 hooves +6 (1d6+4), bite +1 (1d4+2); scent"""
    },
    "Horse, Light": {
        'AC': '13',
        'HD': '3d8+6',
        'HP': '19',
        'Init': '+1',
        'Details': """2 hooves +2 (1d4+1); scent"""
    },
    "Horse, Light War": {
        'AC': '14',
        'HD': '3d8+9',
        'HP': '22',
        'Init': '+1',
        'Details': """2 hooves +4 (1d4+3), bite -1 (1d3+1); scent"""
    },
    "Leopard": {
        'AC': '15',
        'HD': '3d8+6',
        'HP': '19',
        'Init': '+4',
        'Details': """bite +6 (1d6+3), 2 claw +1 (1d3+1); pnce, rake 1d3+1;
        scent"""
    },
    "Lion": {
        'AC': '15',
        'HD': '5d8+10',
        'HP': '32',
        'Init': '+3',
        'Details': """2 claw +7 (1d4+5), bite +2 (1d8+2); pnce, rake 1d4+2;
        scent"""
    },
    "Lizard, Giant": {
        'AC': '15',
        'HD': '3d8+9',
        'HP': '22',
        'Init': '+2',
        'Details': """bite +5 (1d8+4)"""
    },
    "Monkey": {
        'AC': '14',
        'HD': '1d8',
        'HP': '4',
        'Init': '+2',
        'Details': """bite +4 (1d3-4)Mule 13 3d8+9 22 +1 2 hooves +4 (1d4+3)"""
    },
    "Octopus": {
        'AC': '16',
        'HD': '2d8',
        'HP': '9',
        'Init': '+3',
        'Details': """arms +5 (0), bite +0 (1d3); improved grab; ink cloud,
        jet"""
    },
    "Octopus, Giant": {
        'AC': '18',
        'HD': '8d8+8',
        'HP': '44',
        'Init': '+2',
        'Details': """8 tentacles +10 (1d4+5), bite +5 (1d8+2); improved grab,
        constrict; ink cloud, jet"""
    },
    "Owl": {
        'AC': '17',
        'HD': '1d8',
        'HP': '4',
        'Init': '+3',
        'Details': """claws +5 (1d4-2)"""
    },
    "Pony": {
        'AC': '13',
        'HD': '2d8+2',
        'HP': '11',
        'Init': '+1',
        'Details': """2 hooves +2 (1d3+1); scent"""
    },
    "Pony, War": {
        'AC': '13',
        'HD': '2d8+4',
        'HP': '13',
        'Init': '+1',
        'Details': """2 hooves +3 (1d3+2); scent"""
    },
    "Porpoise": {
        'AC': '15',
        'HD': '2d8+2',
        'HP': '11',
        'Init': '+3',
        'Details': """butt +4 (2d4); blindsight"""
    },
    "Rhinoceros": {
        'AC': '16',
        'HD': '8d8+40',
        'HP': '76',
        'Init': '0',
        'Details': """gore +13 (2d6+12)"""
    },
    "Shark, Medium": {
        'AC': '15',
        'HD': '3d8+3',
        'HP': '16',
        'Init': '+2',
        'Details': """bite +4(1d6+1); keen scent"""
    },
    "Shark, Large": {
        'AC': '15',
        'HD': '7d8+7',
        'HP': '38',
        'Init': '+2',
        'Details': """bite +7 (1d8+4); keen scent"""
    },
    "Shark, Huge": {
        'AC': '15',
        'HD': '10d8+20',
        'HP': '65',
        'Init': '+2',
        'Details': """bite +10 (2d6+7); keen scent"""
    },
    "Snake, Constrictor": {
        'AC': '15',
        'HD': '3d8+3',
        'HP': '16',
        'Init': '+3',
        'Details': """bite +5 (1d3+4); improved grab, constrict 1d3+4; scent"""
    },
    "Snake, Giant Constr.": {
        'AC': '15',
        'HD': '11d8+11',
        'HP': '60',
        'Init': '+3',
        'Details': """bite +13 (1d8+10); improved grab, constrict 1d8+10;
        scent"""
    },
    "Snake, Viper, Small": {
        'AC': '17',
        'HD': '1d8',
        'HP': '4',
        'Init': '+3',
        'Details': """bite +4 (1d2-2 &p); poison (DC11, 1d6 Con), scent"""
    },
    "Snake, Viper, Medium": {
        'AC': '16',
        'HD': '2d8',
        'HP': '9',
        'Init': '+3',
        'Details': """bite +4 (1d4-1 &p); poison (DC11, 1d6 Con), scent"""
    },
    "Snake, Viper, Large": {
        'AC': '15',
        'HD': '3d8',
        'HP': '13',
        'Init': '+3',
        'Details': """bite +4 (1d4 &p); poison (DC11, 1d6 Con), scent"""
    },
    "Snake, Viper, Huge": {
        'AC': '15',
        'HD': '4d8+4',
        'HP': '22',
        'Init': '+4',
        'Details': """bite +5 (1d4 &p); poison (DC13, 1d6 Con), scent"""
    },
    "Squid": {
        'AC': '16',
        'HD': '3d8',
        'HP': '13',
        'Init': '+3',
        'Details': """arms +5 (0), bite +0 (1d6+1); imp., grab;
        ink cloud, jet"""
    },
    "Squid, Giant": {
        'AC': '17',
        'HD': '12d8+12',
        'HP': '66',
        'Init': '+3',
        'Details': """10 tentacles +15 (1d6+8), bite +10 (2d8+4);
        improved grab, constrict 1d6+8; ink cloud, jet"""
    },
    "Tiger": {
        'AC': '14',
        'HD': '6d8+18',
        'HP': '45',
        'Init': '+2',
        'Details': """2 claw +9 (1d8+6), bite +4 (2d6+3);
        pounce, grab, rake 1d8+3"""
    },
    "Weasel": {
        'AC': '14',
        'HD': '1/2 d8',
        'HP': '2',
        'Init': '+2',
        'Details': """bite +4 (1d3-4); attach; scent"""
    },
    "Whale, Baleen": {
        'AC': '16',
        'HD': '12d8+72',
        'HP': '126',
        'Init': '+1',
        'Details': """tail slap +17 (1d8+18); blindsight"""
    },
    "Whale, Cachalot": {
        'AC': '16',
        'HD': '12d8+84',
        'HP': '138',
        'Init': '+1',
        'Details': """bite +17 (4d6+12), tail slap +12 (1d8+6); blindsight"""
    },
    "Whale, Orca": {
        'AC': '16',
        'HD': '9d8+45',
        'HP': '85',
        'Init': '+2',
        'Details': """bite +12 (2d6+12); blindsight"""
    },
    "Wolf": {
        'AC': '14',
        'HD': '2d8+4',
        'HP': '13',
        'Init': '+2',
        'Details': """bite +3 (1d6+1); trip; scent"""
    },
    "Wolverine": {
        'AC': '14',
        'HD': '3d8+12',
        'HP': '25',
        'Init': '+2',
        'Details': """2 claws +4 (1d4+2), bite -1 (1d6+1); rage; scent"""
    },
    "Giant Ant, Worker": {
        'AC': '17',
        'HD': '2d8',
        'HP': '9',
        'Init': '0',
        'Details': """bite +1 (1d6); improved grab; vermin"""
    },
    "Giant Ant, Soldier": {
        'AC': '17',
        'HD': '2d8+2',
        'HP': '11',
        'Init': '0',
        'Details': """bite +3 (2d4+3); improved grab, acid sting; vermin"""
    },
    "Giant Ant, Queen": {
        'AC': '17',
        'HD': '4d8+4',
        'HP': '22',
        'Init': '-1',
        'Details': """bite +5 (2d6+4); improved grab; vermin"""
    },
    "Giant Bee": {
        'AC': '14',
        'HD': '3d8',
        'HP': '13',
        'Init': '+2',
        'Details': """sting +2 (1d4 &p); poison (DC13, 1d6 Con), vermin"""
    },
    "Giant Beetle, Bom.": {
        'AC': '16',
        'HD': '2d8+4',
        'HP': '13',
        'Init': '0',
        'Details': """bite +2 (1d4+1); acid spray; vermin"""
    },
    "Giant Beetle, Stag": {
        'AC': '19',
        'HD': '7d8+21',
        'HP': '52',
        'Init': '0',
        'Details': """bite +10 (4d6+9); trample 2d8+3; vermin"""
    },
    "Giant Pray. Mantis": {
        'AC': '14',
        'HD': '4d8+8',
        'HP': '26',
        'Init': '-1',
        'Details': """claws +6 (1d8+4), bite +1 (1d6+2); imp grab, squeeze;
        vermin"""
    },
    "Giant Wasp": {
        'AC': '14',
        'HD': '5d8+10',
        'HP': '32',
        'Init': '+1',
        'Details': """sting +6 (1d3+6 &p); poison (DC18, 1d6 Dex), vermin"""
    },
    "Centipde, Medium": {
        'AC': '14',
        'HD': '1d8',
        'HP': '4',
        'Init': '+2',
        'Details': """bite +2 (1d6-1 &p); poison (DC13, 1d3 Dex), vermin"""
    },
    "Centipde, Large": {
        'AC': '14',
        'HD': '2d8',
        'HP': '9',
        'Init': '+2',
        'Details': """bite +2 (1d8+1 &p); poison (DC16, 1d4 Dex), vermin"""
    },
    "Centipde, Huge": {
        'AC': '16',
        'HD': '4d8',
        'HP': '18',
        'Init': '+2',
        'Details': """bite +4 (2d6+4 &p); poison (DC18, 1d6 Dex), vermin"""
    },
    "Centipde, Gargantuan": {
        'AC': '18',
        'HD': '16d8',
        'HP': '72',
        'Init': '+2',
        'Details': """bite +13 (2d8+7 &p); poison (DC26, 1d8 Dex), vermin"""
    },
    "Centipde, Colossal": {
        'AC': '20',
        'HD': '32d8',
        'HP': '144',
        'Init': '+2',
        'Details': """bite +23 (4d6+10 &p); poison (DC36, 2d6 Dex), vermin"""
    },
    "Scorpion, Tiny": {
        'AC': '8',
        'HD': '+2',
        'HP': '4',
        'Init': '0',
        'Details': """2 claws +2 (1d2-4), sting -3 (1d2-4 &p);
        poison (DC11, 1d2 Str), improved grab; vermin"""
    },
    "Scorpion, Small": {
        'AC': '14',
        'HD': '1d8+2',
        'HP': '6',
        'Init': '0',
        'Details': """2 claws +1 (1d3-1), sting -4 (1d3-1 &p);
        poison (DC11, 1d3 Str), improved grab, squeeze; vermin"""
    },
    "Scorpion, Medium": {
        'AC': '14',
        'HD': '2d8+4',
        'HP': '13',
        'Init': '0',
        'Details': """2 claws +2 (1d4+1), sting -3 (1d4 &p);
        poison (DC15, 1d4 Str), improved grab, squeeze; vermin"""
    },
    "Scorpion, Large": {
        'AC': '14',
        'HD': '4d8+8',
        'HP': '26',
        'Init': '0',
        'Details': """2 claws +5 (1d6+3), sting +0 (1d6+1 &p);
        poison (DC18, 1d6 Str), improved grab, squeeze; vermin"""
    },
    "Scorpion, Huge": {
        'AC': '16',
        'HD': '16d8+32',
        'HP': '104',
        'Init': '0',
        'Details': """None"""
    },
    "Scorpion, Gargantuan": {
        'AC': '18',
        'HD': '32d8+64',
        'HP': '208',
        'Init': '0',
        'Details': """None"""
    },
    "Scorpion, Colossal": {
        'AC': '20',
        'HD': '64d8+128',
        'HP': '416',
        'Init': '0',
        'Details': """None"""
    },
    "Spider, Small": {
        'AC': '14',
        'HD': '1d8',
        'HP': '4',
        'Init': '+3',
        'Details': """bite +4 (1d4-2 &p); poison (DC11, 1d3 Str), web; vermin"""
    },
    "Spider, Medium": {
        'AC': '14',
        'HD': '2d8+2',
        'HP': '11',
        'Init': '+3',
        'Details': """bite +4 (1d6 &p); poison (DC14, 1d4 Str), web; vermin"""
    },
    "Spider, Large": {
        'AC': '14',
        'HD': '4d8+4',
        'HP': '22',
        'Init': '+3',
        'Details': """bite +4 (1d8+3 &p); poison (DC17, 1d6 Str), web; vermin"""
    },
    "Spider, Huge": {
        'AC': '16',
        'HD': '10d8+10',
        'HP': '55',
        'Init': '+3',
        'Details': """bite +9 (2d6+6 &p); poison (DC22, 1d8 Str), web; vermin"""
    },
    "Spider, Gargantuan": {
        'AC': '18',
        'HD': '24d8+24',
        'HP': '132',
        'Init': '+3',
        'Details': """bite +20 (2d8+9 &p); poison (DC31, 2d6 Str), web;
        vermin"""
    },
    "Spider, Colossal": {
        'AC': '20',
        'HD': '48d8+48',
        'HP': '264',
        'Init': '+3',
        'Details': """bite +36 (4d6+12 &p); poison (DC35, 2d8 Str), web;
        vermin"""
    }
}
